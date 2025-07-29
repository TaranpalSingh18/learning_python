# we will be learning about product, permutations, combinations, etc etc
from itertools import product

a={1,3}
b={7,4}
prod = product(a,b)
print(prod) #--> returns the address

print(list(prod))
# basically a one to one mapping 
