"""Payoff and NAV functions used in the article (Equations 1, 3 and A-1 to A-4)."""
import numpy as np


def intrinsic(s, k):
    """Intrinsic value of a call with strike k at underlying price s (Equation 3)."""
    return np.maximum(np.asarray(s, dtype=float) - k, 0.0)


def long_call(s, k, c):
    """Profit at expiration of a long call bought for premium c (Equation A-1)."""
    return intrinsic(s, k) - c


def naked_short_call(s, k, c):
    """Profit at expiration of a naked short call written for premium c (Equation A-2)."""
    return c - intrinsic(s, k)


def long_stock(s, p0):
    """Profit of a long position in the underlying bought at p0."""
    return np.asarray(s, dtype=float) - p0


def covered_call(s, p0, k, c):
    """Profit at expiration of a covered call (Equations 1 and A-4)."""
    return long_stock(s, p0) + c - intrinsic(s, k)


def covered_call_nav(s, k, c):
    """NAV at expiration of a covered-call position: equity plus premium minus the
    short-call liability, which at expiration equals intrinsic value (Equations 2a and 4)."""
    return np.asarray(s, dtype=float) + c - intrinsic(s, k)
