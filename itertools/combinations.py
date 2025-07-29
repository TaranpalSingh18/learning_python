from itertools import combinations, combinations_with_replacement

a = [1,7,2,3,5]
comb = combinations(a,2)
combi = combinations_with_replacement(a,2)
print(list(comb))
print(list(combi))

