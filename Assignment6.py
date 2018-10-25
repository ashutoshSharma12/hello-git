#Answer Number1:
side = input("Enter the Side of The Square: ")
Area = side**2
print Area
#Answer Number2:
def isPerfect( n ):


    sum = 1


    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1


    return (True if sum == n and n!=1 else False)


print("Below are all perfect numbers till 10000")
n = 2
for n in range (10000):
    if isPerfect (n):
        print(n , " is a perfect number")
#Answer Number3:
num = input("Enter the number for the Table: ")
for i in range(1, 11):
   print(num,"x",i,"=",num*i)
#Answer Number4:
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
