# currency.py
# Purpose: Converts US Dollars to Euros and vice versa.
# Usage: numerical_value {currency}
# Example: 45.32 E

import sys

numArgs = len(sys.argv)

# If no user arguments are given, exit the script and warn the user.
if numArgs == 1:
        print 'Usage: number {currency (US or E)}'
        print 'Example: 100 US'
        sys.exit(0)  # Exit the script.

amount = float(sys.argv[1])  # Assume user supplies at least one input.
if numArgs >= 3:
    currency = sys.argv[2]
else:
    currency = 'US'
    print "Since you didn't specify a currency, I'm assuming US to Euros."

if currency == 'US':
    rc = euros = 0.7*amount
    print amount, 'US dollars is equivalent to', rc, 'Euros'
else:
    rc = usdollars = (10.0/7)*amount
    print amount, 'Euros is equivalent to', rc, 'US Dollars'
