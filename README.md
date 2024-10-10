[![python](https://img.shields.io/badge/MicroPython-1.23-blue?style=for-the-badge&logo=python&logoColor=FFD43B)](https://docs.micropython.org/en/v1.23.0/)

# Fireflies

Realistically simulate fireflies with a Pico and LEDs.

## Hardware Setup

- Pico
- LEDs (preferably yellow-green, but light-blue, or orange would work too)

## Software Setup

Install MicroPython on Pico and copy across the Python files.

Setup software on the host machine for linting.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Confirm LED pins match those attached to hardware LEDs.

### Lint

```sh
python -m ruff check --fix
```
