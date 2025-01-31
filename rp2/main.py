from time import sleep_ms

from firefly import Firefly
from machine import PWM, Pin
from probability import gauss

pins = [1, 5, 9, 22, 28, 25]
fireflies = []
for pin in pins:
    # generate a random firefly
    # Based on data about P. carolinus sourced from https://www.nature.com/articles/s41598-024-53671-3/figures/4
    cycles_per_minute = gauss(mu=12, sigma=1)
    number_of_flashes = gauss(mu=6, sigma=1, rounding=1)
    interflash_gap = gauss(mu=0.45, sigma=0.025)
    flash_duration = gauss(mu=0.15, sigma=0.01)  # increase mean duration for warm-up and cool-down
    max_brightness = gauss(mu=63, sigma=16)

    # setup hardware
    led = PWM(Pin(pin))
    led.freq(1024)

    firefly = Firefly(
        led,
        cycles_per_minute,
        number_of_flashes,
        interflash_gap,
        flash_duration,
        max_brightness,
    )

    fireflies.append(firefly)

    print(str(firefly))


def brightness_to_duty_cycle(duty_cycle: int) -> int:
    """
    Map the brightness to a duty cycle value to linearise the LED brightness.

    Source: https://electronics.stackexchange.com/a/443689
    """
    # fmt: off
    ledLookupTable = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 
        4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 13, 
        14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 23, 23, 24, 24, 25, 26, 
        26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 38, 39, 40, 41, 42, 42, 
        43, 44, 45, 46, 47, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 56, 57, 58, 59, 60, 61, 62, 63, 
        64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 
        89, 91, 92, 93, 94, 95, 97, 98, 99, 100, 102, 103, 104, 105, 107, 108, 109, 111, 112, 113, 
        115, 116, 117, 119, 120, 121, 123, 124, 126, 127, 128, 130, 131, 133, 134, 136, 137, 139, 
        140, 142, 143, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 160, 162, 163, 165, 166, 
        168, 170, 171, 173, 175, 176, 178, 180, 181, 183, 185, 186, 188, 190, 192, 193, 195, 197, 
        199, 200, 202, 204, 206, 207, 209, 211, 213, 215, 217, 218, 220, 222, 224, 226, 228, 230, 
        232, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255
    ] 
    # fmt: on
    return ledLookupTable[duty_cycle] * 256


while True:
    for firefly in fireflies:
        brightness = firefly.fly()
        firefly.led.duty_u16(brightness_to_duty_cycle(brightness))
    sleep_ms(10)
