S = "MISSISSIPPI"
frequencies = {}
for i in S: 
   if i in frequencies: 
      frequencies[i] += 1
   else: 
      frequencies[i] = 1
print(frequencies)