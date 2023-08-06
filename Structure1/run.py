
# =============================================================================
# Triggering the entire project
# Do this by python run.py in the terminal
# =============================================================================

# Helpers goes with NO PATH because they are on the same directory import helpers
# Other way could be import as:
#   from helpers import *, or
#   from helpers import calculate_primes
# & so I should avoid to refer file name
from prime.prime import Prime
import prime.constants as c
from Structure1.prime.helpers import *

from email.email import Email


def run():
    p = Prime(start=c.START, finish=c.FINISH)
    prettier = p.prettify()
    print(prettier)
    # print(primes)
    # I'm going to add a functionality that will emulate the ability to send
    # the results of prime calculations to a remote destination by email.
    # It's not convenient that the functions name's has the same name that
    # the directory where they seat
    # prettier = primes.prettify()
    new_mail = Email()
    new_mail.to = 'john_doe@email.com'
    new_mail.subject = f'Prime numbers execution form {c.START} to {c.FINISH}'
    new_mail.body = prettier
    new_mail.send()


if __name__ == '__main__':
    run()
