[![python](https://img.shields.io/badge/MicroPython-1.23-blue?style=for-the-badge&logo=python&logoColor=FFD43B)](https://docs.micropython.org/en/v1.23.0/)

# Fireflies

Use real-world data to simulate fireflies realistically with a Pico and LEDs.

The LEDs simulate individual fireflies using characteristics described in the following papers:

- Martin, O., Nguyen, C., Sarfati, R. et al. Embracing firefly flash pattern variability with data-driven species classification. Sci Rep 14, 3432 (2024). https://doi.org/10.1038/s41598-024-53671-3
- Goh, K.-S.; Lee, C.-M.; Wang, T.-Y. Species-Specific Flash Patterns Track the Nocturnal Behavior of Sympatric Taiwanese Fireflies. Biology 2022, 11, 58. https://doi.org/10.3390/biology11010058

_Demonstration showing the built-in Pico LED in green, and four additional SMD LEDs in orange._

![Flashing LEDs](lights.gif)

## Hardware Setup

- Pico
- LEDs (preferably yellow-green, but light-blue, or orange would work too)

## Software Setup

Install MicroPython on the Pico and copy the files in `rp2/` across to the Pico's root directory.

Setup software on the host machine for linting:

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
