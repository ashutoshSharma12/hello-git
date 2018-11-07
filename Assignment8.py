def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

'''
Get a list of keys from dictionary which has value that matches with any value in given list of values
'''
def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys

name = input("Enter the Key")

score = int(input("Enter the Value"))

class_list = {}

class_list[name] = score

print(class_list)


print("Original Dictionary")
print(class_list)

'''
Get list of keys with value 100
'''
listOfKeys = getKeysByValue(class_list, '100')

print("Keys with value equal to 100")
    #Iterate over the list of keys
for key  in listOfKeys:
    print(key)

    print("Keys with value equal to 100")

    '''
    Get list of keys with value 43 using list comprehension
    '''
    listOfKeys = [key  for (key, value) in class_list.items() if value == 100]

    #Iterate over the list of keys
    for key  in listOfKeys:
            print(key)

    print("Keys with value equal to any one from the list [100] ")

    '''
    Get list of keys with any of the given values
    '''
    listOfKeys = getKeysByValues(class_list, [43, 97,100] )

    #Iterate over the list of values
    for key  in listOfKeys:
        print(key)




#Answer Number2:
num_students = int(raw_input("Please enter number of students:"))
print "you entered %s students" %num_students
student_info = {}
student_data = ['Math marks : ', 'Physics marks : ', 'Chemistry marks : ']
for i in range(0,num_students):
    student_name = raw_input("Name :")
    student_info[student_name] = {}
    for entry in student_data:
        student_info[student_name][entry] = int(raw_input(entry)) #storing the marks entered as integers to perform arithmetic operations later on.
#print student_info
print"Please enter student name ?"
name = raw_input("Student name : ")
if name in student_info.keys():
    print "student with marks : ", student_info[student_name], student_info[name].values()
else:
    print"please enter valid name"
