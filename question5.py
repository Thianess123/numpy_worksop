#write a program to find if the given number is prime no or not
n=int(input("enter the number:"))
prime=0
for i in range(2,n):
 if n%i==0:
     prime=1
 if prime==1:
     print("not a prime number")
else:
    print("prime number")
