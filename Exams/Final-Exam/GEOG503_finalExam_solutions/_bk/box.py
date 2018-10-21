# box.py
# Purpose:  Determine if a point is within the box bounded by (0,0) and (1,1)
# Usage: x_value, y_value
# Example: 0.2 0.4
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])

if 0 <= x <= 1 and 0 <= y <= 1:
    print '({0},{1}) is in the box.'.format(x, y)
else:
    print '({0},{1}) is outside the box.'.format(x, y)
