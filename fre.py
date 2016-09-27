a = raw_input("Please enter a string: ")

d = {}

for x in a.lower():
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print d   




