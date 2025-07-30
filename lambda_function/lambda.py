from functools import reduce

add = lambda x: x+10
print(add(2))
#the above is equivalent to 
def add_func(x):
    return x+10

#we can also pass multiple inputs in lambda fnc
mul = lambda x,y,q: x*y*q

print(mul(2,5,9))

#sorted things
list = [(1,2), (8,0) ,(3,5), (4,7)]
list_sorted = sorted(list, key=lambda x: x[1])
print(list_sorted)

#map function
a=[1,2,4,5,6,7,8]
p = map(lambda x: x*x, a)
print(*p)

# the same can be done using list comprehension
listt = [i*i for i in a]
print(listt)

#filter
ages=[10, 18, 90, 45, 89]

filtered_list=[]

for x in ages:
    if x <19:
        filtered_list.append(x)
print(filtered_list)


#filter(func, seq)
p = filter(lambda x: x%2==0 ,ages)
print(*p)

#reduce
p = reduce(lambda x,y: x*y, a)
print(p)
