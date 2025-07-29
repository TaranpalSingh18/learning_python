# COLLECTIONS: counter, namedTuple, ordereddict, defaultdict, deque
from collections import Counter
s ="taaaaaarrrrrrrrrrrran"
print(Counter(s))

my_counter = Counter(s)
print(my_counter.keys())

print(my_counter.values())

print(my_counter.items())

print(my_counter.most_common(2))

print(my_counter.most_common(1)[0][1])