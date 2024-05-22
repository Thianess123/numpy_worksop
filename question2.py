# find if the given number is a palindrome or not?
n=int(input("enter number:"))
n_str=str(n)
if n_str==n_str[::-1]:
      print("palindrome")
else:
    print("not palindrome")
