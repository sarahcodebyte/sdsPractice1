size = int(input("Enter the size of the list : "))
sum_odd = 0
list = []
for i in range(size):
    n = int(input("Enter element {} : ".format(i+1)))
    list.append(n)
for i in range(size):
    if(list[i] % 2 != 0):
        sum_odd += list[i]
        
print("Sum of odd numbers : {} ".format(sum_odd))