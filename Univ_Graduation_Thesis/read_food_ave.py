#python read_food_ave.py | sort -n -k 2 | uniq > _dissim.txt

min_dist = 1.0
count = 1
result = 0

FOOD_NAME = 'tyanpon'

#soba_food_pairs.txt
#sushi_food_pairs.txt
#tyanpon_food_pairs.txt

dd = dict()
fp = open(FOOD_NAME + '_food_pairs.txt', encoding='utf8')
for line in fp:
    fields = line.strip().split()
    if True:
        #print(fields[0])
        if len(fields) == 3:
            dist = float(fields[2])
            #result += dist
            #count += 1
            if not fields[1] in dd:
                dd[fields[1]] = dist
            else:
                if dd[fields[1]] < dist:
                    dd[fields[1]] = dist

result = 0.0
count = 0
for k in dd:
    result += dd[k]
    count += 1
average = result/count
#print('average = {:.5f}'.format(average))

for k in dd:
    #if dd[k] < average and dd[k] > average * 0.3:
    if dd[k] < average:
        print(k, dd[k])


"""
fp2 = open(FOOD_NAME + '_food_pairs.txt', encoding='utf8')
for line in fp2:
    fields = line.strip().split()
    if True:
        if len(fields) == 3:
            dist = float(fields[2])
            if dist < average and dist > average * 0.5:
            #if dist < average:
 #               print(dist)
                print(fields[1], dist)
"""
