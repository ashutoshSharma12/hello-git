import numpy as np
from collections import defaultdict
#Answer Number1:
x = input("Enter the year : ")
if x % 4 ==0:
    print" The Year is a Leap year"
else:
    print "The year is not a leap Year"
#Answer Number2:
y =  input("Enter the length of the figure")
z =  input("Enter the breadth of the figure")
if y == z:
    print "It is a square"
else:
    print "It is a rectange"
#Answer Number3:
a = input("Enter the Age of first Person: ")
b = input("Enter the Age of Second Person: ")
c = input("Enter the Age of Third Person: ")
if (a >= b) and (b >= c):
    print "The First Person is Oldest:", a
elif (b >= a) and (b >= c):
   print "Second person is Oldest: ", b
else:
    print "The Oldest person is third one:", c
if (b >= a) and (c >= b):
    print "The First Person is Youngest:", a
elif (a >= b) and (c >= b):
   print "Second person is Youngest: ", b
else:
    print "The Youngest person is third one:", c
#Answer Number4:
print "Enter age"
age = input()
print "SEX? (M or F)"
sex = raw_input()
print "MARRIED? (Y or N)"
marry = raw_input()
if sex == "F" and age>=20 and age<=60:
  print "Urban areas only"
elif sex == "M" and age>=20 and age<=40:
  print "You can work anywhere"
elif sex == "M" and age>40 and age<=60:
  print "Urban areas only"
else:
  print "ERROR"
#Answer Number5:
print "Enter quantity"
quantity = input()
if quantity*100 > 1000:
  print "Cost is",((quantity*100)-(.1*quantity*100))
else:
  print "Cost is",quantity*100

#Answer Number6:
sum = 0

i = 10
while i>0:
  print "Enter number"
  num = input()
  sum = sum + num
  i = i-1
print "average is",sum/10.0
#Answer Number7:
#while True:
  #print "INFINITE"
 #Answer Number8:
number  = input("Enter the list") #enter the int list as (1,2) format
a = np.square(number)
print a
#Answer Number9:
myList = (12,13,13.55,14.67,14,'a','b','c')
print "Original list is", myList
d = defaultdict(list)
for x in myList:
    d[type(x)].append(x)
print d[int]
print d[str]
print d[float]
#Answer Number10:
prime=[]
for j in range(1,102):
    X=[]
    a=j
    for i in range(a-1,1,-1):
        c= a%i
        X.append(c)
    if all ([c!=0 for c in X]):
        prime.append(a)
print("The list of all prime number between 1 to 101", prime)
#Answer Number11:
for i in range(1,5):
    print("*"*i)
#Answer Number12:
Vim = []
o=10
for o in range(0,10):
    q=int(input("element : "))
    Vim.append(q)
print(Vim)
X=int(input("Enter Any Element which you want to find and remove"))
for o in range(0,10):
    if(Vim[o]==X):
        Vim.remove(X)
print(Vim)
