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

    def fly(self):
        """Return the brightness of the LED at the current time."""
        self.t += 0.01
        if self.t >= self.period:
            self.t = 0

        # Calculate the brightness of the LED
        brightness = 0
        for i in range(self.number_of_flashes):
            if self.t < i * self.interflash_gap:
                pass
            elif self.t < i * self.interflash_gap + self.flash_duration:
                brightness = self.max_brightness
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
