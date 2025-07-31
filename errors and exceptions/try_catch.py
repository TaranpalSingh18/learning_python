a = 9
try:
    if a%3==0:
        p =f"{a} is divisible by 3"
        print(p)
except:
    print("wrong")

#zero division error

try:
    a = 5/2
    print(a)
except ZeroDivisionError:
    print("division by 0 is not possible")
except TypeError as e:
    print("this is a type error")
else:
    print("everything is running fine")
finally:
    print("cleaning up...")



    

