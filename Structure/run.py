
# =============================================================================
# Triggering the entire project
# Do this by python run.py in the terminal
# =============================================================================

import constants as c
# Helpers goes with NO PATH because they are on the same directory import helpers
# Other way could be import as:
#   from helpers import *, or
#   from helpers import calculate_primes
# & so I should avoid to refer file name
from helpers import *


def run():
    primes = calculate_primes(c.START, c.FINISH)
    print(primes)


if __name__ == '__main__':
    run()
