print("Enter the number")
n = int(input())
temp = n
rev = 0
while(temp!=0):
    rev = rev*10 + (temp%10)
    temp = temp//10

if(rev==n):
    print("This is a palidrome number")
else:
    print("This is not a palindrome number")