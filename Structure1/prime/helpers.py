
# =============================================================================
# Functions that are going to help culculate prime numbers
# =============================================================================
# To add a feature that skips the calculation of primes for a specific range
# I should add a condition based on a couple of constants added in constants.py
# from Structure1.prime import constants as
# from constants import *
# from Structure1.prime import constants as c

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



