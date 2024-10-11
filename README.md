[![python](https://img.shields.io/badge/MicroPython-1.23-blue?style=for-the-badge&logo=python&logoColor=FFD43B)](https://docs.micropython.org/en/v1.23.0/)

# Fireflies

Realistically simulate fireflies with a Pico and LEDs.

![Flashing LEDs](lights.gif)

_Demonstration showing the built-in Pico LED in green, and four additional SMD LEDs in orange._

## Hardware Setup

- Pico
- LEDs (preferably yellow-green, but light-blue, or orange would work too)

## Software Setup

Install MicroPython on Pico and copy the files in `rp2/` across to the Pico.

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
