Dict1 = {
"name": "Arman",
"age":21,
"salary": 80000,
"city": "Ranchi",
"country": "India"}
Key = {Dict1.get("name"), Dict1.get("salary")}
print(Key)



key_to_remove = Dict1
key_to_remove.pop("age")
key_to_remove.pop("country")
print(key_to_remove)


Dict1['loaction'] = Dict1.pop('city')
print(Dict1)

