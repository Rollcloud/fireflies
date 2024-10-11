import random
from math import floor, log, log10


def round_sig(x, sig=3):
    """
    Round to significant figures.

    Source: https://stackoverflow.com/a/3413529
    """
    return round(x, sig - int(floor(log10(abs(x)))) - 1)


def normal_inverse_transform_method() -> float:
    """
    Return a standard normal random variable in the range (-3,3).

    Source: https://codefying.com/2015/02/25/transforming-uniform-random-variables-to-normal/
    """
    x = random.uniform(0, 1)

    a0, a1, a2, a3 = 2.50662823884, -18.61500062529, 41.39119773534, -25.44106049637
    b0, b1, b2, b3 = -8.47351093090, 23.08336743743, -21.06224101826, 3.13082909833
    c0, c1, c2, c3, c4, c5, c6, c7, c8 = (
        0.3374754822726147,
        0.9761690190917186,
        0.1607979714918209,
        0.0276438810333863,
        0.0038405729373609,
        0.0003951896511919,
        0.0000321767881768,
        0.0000002888167364,
        0.0000003960315187,
    )

    y = x - 0.5
    if abs(y) < 0.42:
        r = y * y
        res = (
            y
            * (((a3 * r + a2) * r + a1) * r + a0)
            / ((((b3 * r + b2) * r + b1) * r + b0) * r + 1.0)
        )
    else:
        r = x if y > 0 else 1 - x
        r = log(-log(r))
        res = c0 + r * (
            c1 + r * (c2 + r * (c3 + r * (c4 + r * (c5 + r * (c6 + r * (c7 + r * c8))))))
        )
        if y < 0:
            res = -res

    return res


# redefine gauss to accept a rounding parameter
def gauss(mu: float, sigma: float, rounding: int = 3) -> float:
    """
    Return a random number over a Gaussian distribution.

    Args:
        mu: The mean of the distribution.
        sigma: The standard deviation of the distribution.
        rounding: The number of significant figures to round the result to.
    """
    gauss_ish = normal_inverse_transform_method() * sigma + mu  # random.gauss(mu=mu, sigma=sigma)
    return round_sig(gauss_ish, rounding)
