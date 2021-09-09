S = 'Hello@World#How are(! you? *&'
spl_symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for x in S:
    if x in spl_symbols:
        S = S.replace(x, " ")
print(S)
               