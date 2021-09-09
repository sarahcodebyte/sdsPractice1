n = int(input('Enter 4 digit number: '))
temp = n
rev = 0
while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10    
if(temp == rev):
    print("The number is palindrome")
else:  
    print("Not a palindrome")    