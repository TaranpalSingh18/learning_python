#update function of dict

mydict={"name":"Taran", "age":20, "city":"delhi"}
mydict2=dict(email="taranxyz@gmail.com")
mydict.update(mydict2)
print(mydict)


#keys
dict= {2:6,7:3, 8:6}
print(dict[2])

# we can also append a tuple 
mydict= {(8,10,19):90}
dict.update(mydict)
print(dict)

#there's a diff between tuple key and integer key..though tuple key has 8 and 8 is also an integer kye, but python treats them uniquely only, no duplicates

