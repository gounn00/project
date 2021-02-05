import io
import sys
import MeCab

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

m = MeCab.Tagger()

for line in open('food_data.txt', encoding='utf-8'):
    l = eval(line)
    title = l[0]
    print('["{:s}","'.format(title), end='')
    result = m.parse(l[1]).split('\n')
    for l in result:
        if len(l.split('\t')) > 1:
            word, pos_data = l.split('\t')
            pos_data = pos_data.split(',')
            pos = pos_data[0]
            stem = pos_data[6]
            if stem == "*":
                stem = word
            if pos != "記号" and pos != "助詞" and pos != "助動詞":
                print('{:s}'.format(stem), end=' ')
    print('"]')
