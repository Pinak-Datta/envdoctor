# Changelog

## 0.2.0

- Add Pydantic `BaseSettings` field detection.
- Classify settings fields without defaults as required.
- Classify settings fields with defaults or default factories as optional.
- Add FastAPI/Pydantic example coverage.

## 0.1.1

- Fix PyPI README rendering by using an absolute screenshot URL.
- Declare README Markdown content type in package metadata.

## 0.1.0

- Initial MVP with `envgap check`.
- Dotenv and `.env.example` parsing.
- Python AST scanning for common `os.environ` and `os.getenv` usage.
- Missing, duplicate, placeholder, undocumented, and possible-typo findings.
- Terminal and JSON reporters.
