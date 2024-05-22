#write a program to find the sum of digits of a given number'
num=int(input("enter number:"))
n=str(num)

num_sum=0
for i in n:
    num_sum+=int(i)
print(num_sum) 
