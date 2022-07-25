Nanachan no Toshokan (backend)
==============================

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/Japan7/nanachan-no-toshokan-backend/blob/main/LICENSE)
[![Tests status](https://github.com/Japan7/nanachan-no-toshokan-backend/actions/workflows/build.yml/badge.svg?branch=main&event=push)](https://github.com/Japan7/nanachan-no-toshokan-backend/actions?query=workflow%3ABuild+branch%3Amain+event%3Apush)
[![Code version](https://img.shields.io/github/v/tag/Japan7/nanachan-no-toshokan-backend?color=blue&label=version&sort=semver)](https://github.com/Japan7/nanachan-no-toshokan-backend/actions?query=workflow%3ARelease)
[![Python version](https://img.shields.io/badge/python-3.10-orange)](https://docs.python.org/3.10/)

Installation
------------

NNT is firstly made to run inside a GNU/Linux environment, so most part of the instructions here are designed to work on
this platform only. For others, you'll need to adapt them to your configuration.

### Poetry

Poetry is used for this project as virtual environment manager. If you don't have it yet,
you'll need to install it:

```bash
curl -sSL https://install.python-poetry.org | python -
```

You may need to update your `PATH` environment variable. Be sure to follow the instructions displayed during
installation.  
You can also set up completion by following the installation instruction
[here](https://poetry.eustace.io/docs/#enable-tab-completion-for-bash-fish-or-zsh).

Don't hesitate to configure it too using

```bash
poetry config --list
poetry config KEY VALUE
```

### Docker

In production mode, this project will run inside a Docker container. To be able to do tests in
production-like conditions, you need to have Docker installed on your computer. It will also help
you to manage the services on which the project depends in an easier way. Especially, the setup
script uses it.

All you need is to install it. The installation way may depend on your distribution if you are
on Linux. You will find more information [here](https://docs.docker.com/install/).

### Setup `local_settings.py`

Copy `local_settings_example.py` to `local_settings.py`, and complete it:

- Generate a secret key
- Complete the login info in `DATABASE_LOGIN` (with info of the container)

### Add DNS rules in your system `hosts` file

On Linux, edit `/etc/hosts` as root and add the following rules:

```
127.0.0.1   nnt_db  nnt_db
```

On Windows, edit `C:\Windows\System32\drivers\etc\hosts` as administrator and add the following
rules:

```
127.0.0.1   nnt_db
```

### Development environment

If you use Linux, then everything is already done for you in the `manage` script. But it
requires the following GNU tools that you need to install first. Please refer to your
distribution to know how to install them.

- `jq`, a command-line JSON processor,
- `pyenv`, a simple Python version management tool,

Once these programs are installed, you can simply run the following command:

```bash
./manage setup
```
