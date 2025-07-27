set1={1,2,4,5,7}
set2={1,2,4,5,7, 8, 9 , 0}

set3=set1.union(set2)
print(set3)

set4= set1.intersection(set2)
print(set4)

set5= set1.difference(set2)
print(set5)

symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)

set_all = set1.union(set2)-set4
print(set_all)

print(set1.issubset(set2))