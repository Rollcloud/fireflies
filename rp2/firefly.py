import math


class Firefly:
    """A thinly disguised state-machine class for controlling a firefly LED."""

    def __init__(
        self,
        led,
        cycles_per_minute,
        number_of_flashes,
        interflash_gap,
        flash_duration,
        max_brightness=255,
    ):
        self.led = led
        self.cycles_per_minute = cycles_per_minute
        self.number_of_flashes = number_of_flashes
        self.interflash_gap = interflash_gap
        self.flash_duration = flash_duration
        self.period = 60 / cycles_per_minute  # seconds
        self.max_brightness = max_brightness

        self.t = 0

    def flash(self, t: float) -> int:
        """
        Simulate a firefly flash with gradually increasing and decreasing brightness.

        Returns the brightness of the LED at the specified time.

        Inspired by the flash intensity graphs at:
            https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773436/figure/biology-11-00058-f001/
        """
        # Using a sinusoidal approximation
        brightness = self.max_brightness * (
            0.5 * (1 - math.cos(2 * math.pi * t / self.flash_duration))
        )

        return int(brightness)

    def fly(self, delta_t: float = 0.01) -> int:
        """
        Return the brightness of the LED at the current time.

        Args:
            delta_t: The time step to advance the simulation by (in seconds).
        """
        self.t += delta_t
        if self.t >= self.period:
            self.t = 0

        # Calculate the brightness of the LED
        brightness = 0
        for i in range(self.number_of_flashes):
            if self.t < i * self.interflash_gap:
                pass
            elif self.t < i * self.interflash_gap + self.flash_duration:
                brightness = self.flash(self.t - i * self.interflash_gap)
            elif self.t < (i + 1) * self.interflash_gap:
                pass
            else:
                brightness = 0

        return int(brightness)

    def __repr__(self) -> str:
        return (
            "Firefly(led={}, cycles_per_minute={}, number_of_flashes={}, "
            "interflash_gap={}, flash_duration={}, max_brightness={})".format(
                self.led,
                self.cycles_per_minute,
                self.number_of_flashes,
                self.interflash_gap,
                self.flash_duration,
                self.max_brightness,
            )
        )
