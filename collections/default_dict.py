from collections import defaultdict
d = defaultdict(int)

d['a']=4
d['b']=7
print(d['a'])
print(d['c'])

d = defaultdict(float) #--> mentioning the datatype is important

d['a']=4
d['b']=7
print(d['a'])
print(d['c'])