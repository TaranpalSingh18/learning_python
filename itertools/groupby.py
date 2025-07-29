from itertools import groupby

def smaller_than_3(x):
    return x<3

a=[1,2,4,6,7,0]
groups = groupby(a, key=smaller_than_3)

for key, values in groups:
    print(key, list(values))

