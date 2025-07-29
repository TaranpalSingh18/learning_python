from itertools import accumulate
from operator import mul
import operator

a=[1,15,3,10]

acc = accumulate(a)
print(list(acc))
# prefix sum type ka hai ig

acc = accumulate(a, func=operator.mul)
print(list(acc))

acc = accumulate(a, func=max)
print(list(acc))



