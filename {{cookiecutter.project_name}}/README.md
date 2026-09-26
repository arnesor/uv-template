# {{ cookiecutter.friendly_name }}

[![Tests](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_name}}/actions/workflows/tests.yml/badge.svg)][tests]
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization}}_{{cookiecutter.project_name}}&metric=coverage)][sonarcov]
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project={{cookiecutter.github_organization}}_{{cookiecutter.project_name}}&metric=alert_status)][sonarquality]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

[tests]: https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[sonarcov]: https://sonarcloud.io/summary/overall?id={{cookiecutter.github_organization}}_{{cookiecutter.project_name}}
[sonarquality]: https://sonarcloud.io/summary/overall?id={{cookiecutter.github_organization}}_{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit

## Features

- TODO

## Requirements

- TODO

## Usage

Please see the [Contributor Guide] for details on running development tasks.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

## Credits

This project was generated with the [Python uv project template].

[python uv project template]: https://github.com/arnesor/uv-template
[file an issue]: https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_name}}/issues
<!-- github-only -->

[license]: https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_name}}/blob/main/LICENSE
[contributor guide]: https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_name}}/blob/main/CONTRIBUTING.md
