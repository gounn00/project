import random
result = 0
ave2 = 0 

df = dict()
for i in range(1, 1995):
    fp = open('index.html?use_type=0&amp;smp=1.' + str(i), encoding='utf8')
    df2 = dict()
    for x in fp:
        x = x.strip()
        df2[x] = 1
    for x in df2:
        if not x in df:
            df[x] = df2[x]
        else:
            df[x] = df[x] + df2[x]
for x in df:
    print(x, df[x])
exit(0)

for i in range(100):
    print(i)
    num = random.randint(1, 1994)
    num2 = random.randint(1, 1994)
    #print(num, num2)
    
    fp = open('index.html?use_type=0&amp;smp=1.' + str(num), encoding='utf8')
    fp2 = open('index.html?use_type=0&amp;smp=1.' + str(num2), encoding='utf8')
    
    ave = 0
    count = 0
    count2 = 0
    for x in fp:
        count += 1
        fp2.seek(0)
        for x2 in fp2:
            if x == x2:
                count2 += 1
    if count2 > 0:  
        ave = count2/count

    result += ave
    print(result)

ave2 = result/100
print(ave2)
