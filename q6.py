size = int(input("Enter size of lists: "))
list1 = []
list2 = []
list3 = []
for i in range(size):
    n1 = int(input("Enter element {} : ".format(i+1)))
    list1.append(n1)
    n2 = int(input("Enter element {} : ".format(i+1)))
    list2.append(n2)
    if(i%2 != 0):
        list3.append(list1.pop(i))
    else:
        list3.append(list2.pop(i))
print(list3)               
