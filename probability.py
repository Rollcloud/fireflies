import random

from math import log10, floor


def round_sig(x, sig=3):
    """Round to significant figures.

    Source: https://stackoverflow.com/a/3413529
    """
    return round(x, sig - int(floor(log10(abs(x)))) - 1)


# redefine gauss to accept a rounding parameter
def gauss(mu: float, sigma: float, rounding: int = 3) -> float:
    """Return a random number from a Gaussian distribution.

    Args:
        mu: The mean of the distribution.
        sigma: The standard deviation of the distribution.
        rounding: The number of significant figures to round the result to.
    """
    gauss_ish = random.uniform(
        mu - 3 * sigma, mu + 3 * sigma
    )  # random.gauss(mu=mu, sigma=sigma)
    return round_sig(gauss_ish, rounding)
