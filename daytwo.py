#understanding conditional statements
n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
if n2>0:
    print("division result is:",n1/n2)
else: print("division not possible")

#understanding loops

#1. table of 2
for i in range(0,11):
    print("2 X",i,"=",2*i)



#factorial of a number
n=int(input("enter  number: "))
f=1
for i in range(1,n+1):
    f=f*i
print ("factorial of",n,"is",f)


#largest of (20,21,70,80,64,36)
numbers=[20,21,70,80,64,36]
largest=numbers[0]
for i in numbers:
   if i>=largest:
     largest=i
print(largest)  

#OR
numbers=[20,21,70,80,64,36]
print(max(numbers))

#avg of above numbers 
numbers=[20,21,70,80,64,36]
s=0
for i in numbers:
    s+=i
average=s/len(numbers)
print(average)

#OR
numbers=[20,21,70,80,64,36]
total= sum(numbers)
print("average is ",total/len(numbers))  


#print
# *
# **
# ***
# ****
# *****
# ******
for i in range(1,7):
    print("*"*i)

#print
#    *
#   ***
#  *****
# *******
for i in range(0,5):
    print(" "*(5-i),"*"*(2*i-1))

#print
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
for i in range(1,7):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)

#perimeter of circle if r=7
r=7
perimeter=3.14*2*r
print(perimeter)


#prime no between 1 to 100
for n in range(2,101):
 c=0
 for i in range(1,n+1):
     if n%i==0:
         c+=1

 if c==2:
     print(n)

#even nos btw 1 to 100
for i in range(1,101):
    if i%2==0:
        print(i)
