#Q1. Write a Python program to read last n lines of a file.
l=[]
with open('f1.txt','r') as f:
    l+=(f.readlines())
    print("Total lines in file:",len(l))
    n=int(input("Enter value of n: "))
    print("Content:---\n")
    for i in range(n,len(l)):
         print (l[i])

#Q2. Write a Python program to count the frequency of words in a file.
l=[]
with open('f1.txt','r') as f:
    data = f.readlines()
    word=[]
    for line in data:
        word+=line.split()

    d={}
    for k in word:
        if k in d:
            d[k]+=1
        else:
            d[k]=1
    print(d)


#Q3. Write a Python program to copy the contents of a file to another file
with open('f1.txt','r') as f1:
    with open('f2.txt','r+') as f2:
       f2.write(f1.read())


#Q4. Write a Python program to combine each line from first file with the corresponding line in second file.
l1=[]
l2=[]
s=str()
with open('textfile.txt','r') as f1:
    with open('textfile1.txt','r') as f2:
       l1+=f1.readlines()
       l2+=f2.readlines()
       for i,j in zip(l1,l2):
           print(i)
           print(j)
           s+=i+j#making one string of info
with open('f3.txt','w') as f3:
      f3.write(s)


#Q5. Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
with open('f4.txt','w') as f:
   for i in range(5):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('f4.txt','r') as f:
   data=f.readlines()
  # print(data)
   for no in data:
      l=no.split()
   l.sort()

with open('f5.txt','w') as f:
   for i in l:
      f.write("%s "%(i))
