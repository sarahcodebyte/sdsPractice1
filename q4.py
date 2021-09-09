x = 1
n = int(input('Enter the range: '))

for i in range(0,n):   
     x = 1
     for j in range(0, i+1):   
         print(x, end = " ")           
         x = x + 1
         print('\r')