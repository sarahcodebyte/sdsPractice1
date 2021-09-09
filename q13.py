S = 'Python-is-a-programming-language'
char = '-'
k = 0
while(k < len(S)):
    for i in S:
        if(i == char):
            print(S[:k])
       
        