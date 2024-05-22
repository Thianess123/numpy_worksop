#write a program to find the factorial of a nummber
n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
