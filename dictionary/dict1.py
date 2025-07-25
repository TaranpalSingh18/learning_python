mydict = {"name":"Taran", "age":20, "city":"delhi"}

for i in mydict:
    print({i: mydict[i]})

for key, values in mydict.items():
    print(key, values)

#copying a dictionary
mydictionary = mydict.copy()
mydictionary["email"]="taran23100@iiitnr.edu.in"
print(mydictionary)
print(mydict)