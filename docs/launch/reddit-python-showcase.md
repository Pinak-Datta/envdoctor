# r/Python Showcase Comment

```markdown
**envgap - find gaps between `.env`, `.env.example`, shell env, and Python code**

What my project does:

envgap is a small Python CLI for diagnosing environment config drift. It compares `.env`, `.env.example`, the current shell environment, and Python code using `os.environ` / `os.getenv`, then reports missing keys, placeholder values, duplicate keys, undocumented variables, and likely typos like `DB_URL` vs `DATABASE_URL`.

Why I built it:

I kept seeing the same boring failure mode: local dev works because a variable exists in the shell, but CI, Docker, or another developer's machine fails because `.env.example` is stale or `.env` has a slightly different key.

Target audience:

Python backend developers, FastAPI/Django/Flask users, AI/data app builders with API keys, and maintainers who want config checks in CI.

Install:

```bash
pip install envgap
envgap check
```

GitHub: https://github.com/Pinak-Datta/envgap

Feedback I would especially like:

- false positives from real projects
- Pydantic Settings / FastAPI patterns it should detect next
- Docker or CI env drift cases that are worth supporting
```
