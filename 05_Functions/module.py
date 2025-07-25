# module = a file containing code you want to include in your
# progrsm use 'import' to include a module

import math
print(math.pi) # 3.141592...

import math as m # m is shortcut for math
print(m.pi)

from math import pi
print(pi)

# but the problem is if our variable is of the same name
from math import e
a, b, c, d, e= 1, 2, 3, 4, 5
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e) # so here main problem occurs

# so instead use just import math and then do furthur steps
print(math.e ** a)

### we can create our own module 
# suppose in a file named example.py we had defined our all the functions
# and in main.py we have used it