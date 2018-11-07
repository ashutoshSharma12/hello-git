#Answer Number1:
import re
s = 'Hello from ashutoshsharma6151@icloud.com to priya@yahoo.com about the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)
#Answer Number2:
def isValid(s):

    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)

# Driver Code
s = input("Enter a Phone Number: ")
if (isValid(s)):
    print ("Valid Number")
else :
    print ("Invalid Number")
