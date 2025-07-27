string1="     Taran Pal Singh     "
string1= string1.strip()
#removes the white spaces
print(string1)

string2= "taran"
print(string2.upper())
#similarly for lower

string3 = "humesha"
print(string3.startswith('hmm'))
print(string3.endswith('sha'))

#to find some character
string4 = "bhool jaaa"
print(string4.find('a'))
#works for characters only

#to count some characters
string5= "hehehehe"
print(string5.count('h'))
#basically a hashmap inside it

#replacing some words of a string
string6="hello world"
print(string6.replace("hello","satsrikal")) #--> this returns a new string, does not update the first string, as strings are immutable in nature
print(string6)

#using split operation
stringx="how. are you?"
list = stringx.split('w')
#i can split the string according to the letter i need--> if i put nothing, my defaults splits by spaces
print(list)




