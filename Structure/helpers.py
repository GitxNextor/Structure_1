
# =============================================================================
# Functions that are going to help culculate prime numbers
# =============================================================================
# To add a feature that skips the calculation of primes for a specific range
# I should add a condition based on a cuople of constants addes in constants.py
import constants as c
# from constants import *


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if num % n != 0:
                # Keep checking
                continue
            else:
                # Get out & return false
                return False
    return True


def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n) and n not in c.SKIP_RANGE:
            primes.append(n)
    return primes


