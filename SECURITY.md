# Security Policy

envgap is a diagnostic tool. It should never require real secrets in bug reports, tests, examples, screenshots, or issue comments.

## Supported Versions

Security fixes are considered for the latest published version.

## Reporting a Vulnerability

Please do not open a public issue for sensitive reports.

Email the maintainer listed on the GitHub profile with:

- a short description of the issue
- the affected version
- steps to reproduce with fake/redacted values
- any suggested mitigation

## Secret Handling

When sharing examples, replace secrets with placeholders such as:

```dotenv
DATABASE_URL=postgres://user:password@example.invalid/app
OPENAI_API_KEY=sk-redacted
```

envgap masks secret-like values in reports, but users should still avoid posting real credentials.
