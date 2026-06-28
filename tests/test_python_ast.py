from pathlib import Path

from envgap.extractors.python_ast import scan_python_env_usage


def test_scan_python_env_usage_classifies_required_and_optional(tmp_path: Path) -> None:
    app = tmp_path / "app.py"
    app.write_text(
        "\n".join(
            [
                "import os",
                'DATABASE_URL = os.environ["DATABASE_URL"]',
                'REDIS_URL = os.getenv("REDIS_URL")',
                'DEBUG = os.getenv("DEBUG", "false")',
                'CACHE_URL = os.environ.get("CACHE_URL", "memory://")',
            ]
        ),
        encoding="utf-8",
    )

    usages = scan_python_env_usage(tmp_path)
    by_key = {usage.key: usage for usage in usages}

    assert by_key["DATABASE_URL"].required is True
    assert by_key["REDIS_URL"].required is True
    assert by_key["DEBUG"].required is False
    assert by_key["CACHE_URL"].required is False
    assert by_key["DATABASE_URL"].line == 2


def test_scan_python_env_usage_detects_pydantic_base_settings_fields(tmp_path: Path) -> None:
    app = tmp_path / "settings.py"
    app.write_text(
        "\n".join(
            [
                "from typing import ClassVar",
                "from pydantic import Field",
                "from pydantic_settings import BaseSettings",
                "",
                "class Settings(BaseSettings):",
                "    database_url: str",
                "    openai_api_key: str = Field(...)",
                "    redis_url: str = Field(default=...)",
                '    debug: bool = False',
                '    cache_url: str = Field("memory://")',
                "    retries: int = Field(default=3)",
                "    tags: list[str] = Field(default_factory=list)",
                '    model_name: ClassVar[str] = "Settings"',
                '    _private: str = "ignored"',
            ]
        ),
        encoding="utf-8",
    )

    usages = scan_python_env_usage(tmp_path)
    by_key = {usage.key: usage for usage in usages}

    assert by_key["DATABASE_URL"].required is True
    assert by_key["OPENAI_API_KEY"].required is True
    assert by_key["REDIS_URL"].required is True
    assert by_key["DEBUG"].required is False
    assert by_key["CACHE_URL"].required is False
    assert by_key["RETRIES"].required is False
    assert by_key["TAGS"].required is False
    assert by_key["DATABASE_URL"].line == 6
    assert by_key["DATABASE_URL"].source == "Settings.database_url (Pydantic BaseSettings)"
    assert "MODEL_NAME" not in by_key
    assert "_PRIVATE" not in by_key


def test_scan_python_env_usage_applies_pydantic_env_prefix_and_aliases(tmp_path: Path) -> None:
    app = tmp_path / "settings.py"
    app.write_text(
        "\n".join(
            [
                "from pydantic import AliasChoices, Field",
                "from pydantic_settings import BaseSettings, SettingsConfigDict",
                "",
                "class Settings(BaseSettings):",
                '    model_config: SettingsConfigDict = SettingsConfigDict(env_prefix="APP_")',
                "",
                "    database_url: str",
                '    openai_api_key: str = Field(alias="OPENAI_KEY")',
                '    anthropic_api_key: str = Field(validation_alias="ANTHROPIC_KEY")',
                '    preferred_key: str = Field(alias="PREFERRED_ALIAS", validation_alias="PREFERRED_VALIDATION_ALIAS")',
                '    fallback_key: str = Field(validation_alias=AliasChoices("FALLBACK_KEY", "LEGACY_FALLBACK_KEY"))',
                '    optional_token: str = Field("", alias="OPTIONAL_TOKEN")',
            ]
        ),
        encoding="utf-8",
    )

    usages = scan_python_env_usage(tmp_path)
    by_key = {usage.key: usage for usage in usages}

    assert by_key["APP_DATABASE_URL"].required is True
    assert by_key["OPENAI_KEY"].required is True
    assert by_key["ANTHROPIC_KEY"].required is True
    assert by_key["PREFERRED_VALIDATION_ALIAS"].required is True
    assert by_key["FALLBACK_KEY"].required is True
    assert by_key["LEGACY_FALLBACK_KEY"].required is True
    assert by_key["OPTIONAL_TOKEN"].required is False
    assert "DATABASE_URL" not in by_key
    assert "APP_MODEL_CONFIG" not in by_key
    assert "APP_OPENAI_API_KEY" not in by_key
    assert "PREFERRED_ALIAS" not in by_key
