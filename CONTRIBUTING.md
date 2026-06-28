# Contributing Guide

Thank you for contributing to Offline Invoice Intelligence System. This project is built for offline-first, CPU-only invoice extraction using free and open-source technologies.

## Contribution Principles

- Preserve offline execution.
- Do not introduce cloud AI APIs.
- Do not add OpenAI, Gemini, Anthropic, Claude, Groq, or similar services.
- Do not add CUDA-only or GPU-required dependencies.
- Prefer simple, maintainable, local-first design.
- Keep documentation accurate when implementation changes.
- Protect invoice privacy and avoid committing real customer data.

## Development Workflow

1. Create a branch for the change.
2. Review the project specification in `specs/001-offline-invoice-intelligence/spec.md`.
3. Make a focused change.
4. Update documentation when behavior, setup, or architecture changes.
5. Run local checks before opening a merge request.
6. Request review from the relevant teammate.

## Branch Naming

| Branch Type | Format | Example |
| ----------- | ------ | ------- |
| Feature | `feature/<short-description>` | `feature/invoice-history-search` |
| Fix | `fix/<short-description>` | `fix/pdf-ocr-error-handling` |
| Docs | `docs/<short-description>` | `docs/offline-setup-guide` |
| Chore | `chore/<short-description>` | `chore/ci-license-check` |

## Merge Request Checklist

- The change supports offline execution.
- No cloud AI dependency was added.
- No secrets, tokens, or real invoices are committed.
- Tests and checks pass locally.
- Documentation is updated.
- The change is scoped and reviewable.
- License compatibility has been considered for new dependencies.

## Documentation Standards

- Write documentation in Markdown.
- Prefer clear headings and concise explanations.
- Use diagrams where architecture or workflow clarity matters.
- Keep setup steps reproducible.
- Call out offline requirements explicitly.

## Issue Standards

Every GitLab issue should include:

- Title
- Description
- Assignee
- Priority
- Estimate
- Due date
- Acceptance criteria
- Dependencies

## Commit Message Guidance

Use clear, action-oriented commit messages:

```text
docs: add offline setup guide
fix: handle missing tesseract dependency
feature: add invoice history search
```

## Security and Privacy

Invoice documents may contain sensitive financial and personal data. Use synthetic samples for demos and tests. Do not commit private invoices, customer names, tax identifiers, bank details, or secrets.
