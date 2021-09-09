list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
output = {(a, b) for a in list1
          for b in list2 if a*a == b}
print(output)
        