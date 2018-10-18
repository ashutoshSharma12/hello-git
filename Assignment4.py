import string
# Asnwer Number1:
a = ['aa', 'bb', 'cc']
print "a = ", a
#Answer Number2:
b = ['dd','ee','ff']
print "b = ", b
c = a + b
print "a + b = ", c
#Answer Number3:
d = [1,2,3,3,3,2,2,1,1,11,19]
print "d = ", d
e = [1,2,3,3,3,2,2,1,1,11,19].count(3)
print "occourrence of 3 in list d is = ", e
#Answer Number4:
vowels = ['i','o','a','e','u']
print "Unsorted list = ", vowels
vowels.sort()
print "Sorted list ", vowels
#Answer Number5:
f = ['q', 'w', 'e', 'r', 't', 'y']
g = ['a', 's', 'd', 'f', 'g', 'h']
print "f = ", f
print "g = ", g
h = f + g
h.sort()
print "Contacinated and sorted lists are = ", h
#Answer Number6:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
#Answer Number7:
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))



#Answer Number8:
digits = (1,2,3,4,5,6,7,77,88,99,100) #Decalration of tuples
i = max(digits)
print i
j = min(digits)
print j
#Answer Number9:
k = "Hello"
l = k.upper()
print l
j = "World!"
m = j.lower()
print m
#Answer Number10:
n = "1223Ashu"
o =n.isdigit()
print o
#Answer Number11:
str = "Hello World!!"
print str
new_str = string.replace(str, 'World', 'Ashutosh_Sharma')
print(new_str)
