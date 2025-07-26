mySet={1,2,4,52,2}
print(mySet)

mySet={}
print(type(mySet))

mySet=set()
print(type(mySet))

mySet=set("Hello Traan")
print(mySet)

mySet={0, "taran", True}
print(mySet)

# 0 == false and 1 is True

mySet.clear()
print(mySet)

mySet.add(1)
mySet.add(2)
mySet.add(4)

mySet.discard(0)
print(mySet)

list=[]
for i in mySet:
    list.append(i*i)
newset=set(list)
print(newset)