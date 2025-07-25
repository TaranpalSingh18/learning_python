#slicing in tuples
mytuple = ("Taran", 1,2 ,4, 5,6 , "Gaurav", False)
t1=mytuple[:6]
t2=mytuple[-1:]

reversed_tuple = mytuple[::-1]
step_size_tuple = mytuple[::3]
print(step_size_tuple)
print(reversed_tuple)

final_tuple = t1+t2
print(final_tuple)

#unpacking
*name, random, bool = mytuple
print(name)