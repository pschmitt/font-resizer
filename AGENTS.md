# Agent instructions

`font-resizer` is a FontForge-powered font resizing utility. Keep font transformations consistent with the documented CLI behavior and avoid unrelated changes to generated font assets.

## Working and validation

- Follow the README and `pyproject.toml` for package usage and development checks.
- Test changes with small local font fixtures; do not overwrite user font files during validation.
- Before changing GitHub Actions, check whether [pschmitt/ci-workflows](https://github.com/pschmitt/ci-workflows) provides a reusable workflow or action. Preserve current behavior and check coverage, and use `@main` for shared workflow or action references.
