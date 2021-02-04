import glob

FOOD_NAME = 'sushi'

f_namelist = glob.glob('index.html?use_type=0&amp;smp=*')

#soba_dissim.txt
#sushi_dissim.txt
#tyanpon_dissim.txt
fp = open(FOOD_NAME + '_dissim.txt', encoding='utf8')

#soba_review_dissim.txt
#sushi_review_dissim.txt
#tyanpon_review_dissim.txt
fp2 = open(FOOD_NAME + '_review_dissim.txt', encoding='utf8')

w_dict = dict()
for line in fp:
    fields = line.strip().split()
    word = fields[0]
    word2 = fields[1]
    w_dict[word] = word2

www = w_dict.keys()


r_dict = dict()
for line in fp2:
    fields = line.strip().split()
    word = fields[1]
    word2 = fields[2]
    r_dict[word] = word2

rrr = r_dict.keys()

for x in f_namelist:
    f2 = open(x)
    X_words = f2.read().split('\n')
    f2.close()
    #print(X_words)
    count = 0
    sum1 = 0.0
    for w in X_words:
        if w in www: 
            count += 1
            w_val = w_dict[w]
            sum1 = sum1 + float(w_val)
            #print(w)
            
        else:
            r_val = r_dict[x]
            #print(r_val)
          
    if count > 0:
        r_val = r_dict[x]


        #soba0.14428 sushi0.04051 tyanpon0.02185
        ave1 = float(r_val) + (0.04051 - (sum1/count))*5
        print('{:d} {:s} {:.8f}'.format(count, x, ave1))

    else:
        ave2 = float(r_val)
        #print('NULL', r_val, sum1)
        print('NULL {:s} {:.8f}'.format(x, ave2))

fp.close()
fp2.close()
