#Q1. Name and handle the exception occured in the following program:
'''
a=3
 if a<4:
    a=a/(a-3)
     print(a)
'''
#Ans. Error occured is ZeroDivisionError(i.e. division by zero) for which we use try-except block
a=3
try:
  if a<4:
    a=a/(a-3)
    print(a)

except ZeroDivisionError as e:
  print("Error occured: ",e)

#Q2. Name and handle the exception occurred in the following program:
'''
l=[1,2,3]
print(l[3])
'''
#Ans. Error occured is IndexError(i.e. index out of range) for which we use try-except block
try:
  l=[1,2,3]
  print(l[3])

except IndexError as e:
  print("Error occured: ",e)
#Q3. What will be the output of the following code:

# Program to depict Raising Exception
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or n
'''
Output:-
An exception
Traceback (most recent call last):
  File "hello.py", line 2, in <module>
    raise NameError("Hi there")  # Raise Error
NameError: Hi there
'''



#Q4. What will be the output of the following code:

# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
Output:-
-5.0
a/b result in 0
'''


#Q5. Write a program to show and handle following exceptions:
#1. Import Error
try:
  from threading import ABC
  print(ABC)
except ImportError as e:
  print("Error occured:",e)

#2. Value Error
try:
  a=int(input("Enter number: "))
  print(a)
except ValueError as e:
  print("Error occured:",e)

#3. Index Error
l=[0,1,2]
try:
  print(l[3])
except IndexError as e:
  print("Error occured:",e)
