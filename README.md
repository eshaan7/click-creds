# click-creds

[![pypi](https://img.shields.io/pypi/v/click-creds)](https://pypi.org/project/click-creds/)
[![Build Status](https://github.com/Eshaan7/click-creds/workflows/Linter%20&%20Tests/badge.svg?branch=main)](https://github.com/Eshaan7/click-creds/actions?query=workflow%3A%22Linter+%26+Tests%22)
[![codecov](https://codecov.io/gh/Eshaan7/click-creds/branch/main/graph/badge.svg?token=AeUhwwnaRW)](https://codecov.io/gh/Eshaan7/click-creds)
[![CodeFactor](https://www.codefactor.io/repository/github/eshaan7/click-creds/badge)](https://www.codefactor.io/repository/github/eshaan7/click-creds)
<a href="https://lgtm.com/projects/g/Eshaan7/click-creds/context:python">
  <img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/Eshaan7/click-creds.svg?logo=lgtm&logoWidth=18"/>
</a>


Pluggable credentials storage and management for [click](https://github.com/pallets/click/) CLI applications.

Uses [`~/.netrc` file method](https://www.mkssoftware.com/docs/man4/netrc.4.asp) which is used by popular CLI applications like [Heroku CLI](https://devcenter.heroku.com/articles/authentication#netrc-file-format), AWS CLIs, etc.

## Installation

Requires python version `>=3.6`.

```bash
$ pip install click-creds
```

## Quickstart

Here's an example `cli.py` file.

```python
#!/usr/bin/env python3
import click
import click_creds

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click_creds.use_netrcstore(
    name="myawesomeapp",
    mapping={"login": "username", "password": "api_key", "account": "url"},
)
def cli():
    pass

# Register "config" group
cli.add_command(click_creds.config_group)

# Entrypoint
if __name__ == "__main__":
    cli()
```

Now, if we execute `./cli.py config`,

```bash
$ ./cli.py config
Usage: cli.py config [OPTIONS] COMMAND [ARGS]...

  Set or view config variables

Options:
  -h, --help  Show this message and exit.

Commands:
  get  Echo config variables
  set  Update config variables
```

## Documentation

Please see the [`example_project`](https://github.com/Eshaan7/click-creds/tree/main/example_project).


## Changelog / Releases

All releases should be listed in the [releases tab on GitHub](https://github.com/Eshaan7/click-creds/releases).

See [CHANGELOG](https://github.com/Eshaan7/click-creds/blob/main/.github/CHANGELOG.md) for a more detailed listing.

## License

This project is published with the [BSD License](LICENSE). See [https://choosealicense.com/licenses/bsd/](https://choosealicense.com/licenses/BSD/) for more information about what this means.

## Credits

- [tinynetrc](https://github.com/sloria/tinynetrc)