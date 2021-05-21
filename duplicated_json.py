from collections import Counter
with open('test.txt','r') as f:
    data = f.readlines()

results = Counter(data)

# for key,value in results.items():
#     print(key+': '+str(value))

with open('ntest.txt','w') as fn:
    for key,value in results.items():
        if value == 1:
            fn.write(key)
            print(key)

