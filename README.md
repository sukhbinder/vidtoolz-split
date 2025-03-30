# vidtoolz-split

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-split.svg)](https://pypi.org/project/vidtoolz-split/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-split?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-split/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-split/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-split/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-split/blob/main/LICENSE)

Split a video into two

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-split
```
## Usage

type ``vid split --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-split
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
