#join operation in strings
from timeit import default_timer as timer

string1="hello how are you? I am doing good!"
my_list = string1.split()
print(my_list)
string1=' '.join(my_list)
print(string1)

## good way 
start= timer()
my_list=['a']*100000
s = ''.join(my_list)
stop=timer()
print(stop-start)


## bad way cause takes much time than .join method
my_string=''
start=timer()
for i in my_list:
    my_string+=i
stop=timer()
print(stop-start)

#formating in string

string1 = "hey there"
my_string = "{}, I am Taran Pal Singh".format(string1)
print(my_string)

# printing using f-string --> use this only (modern method)
height=91
weight=89.5

my_string=f"My height is about {height*2}cm and Weight is about : {weight}kgs"
print(my_string)