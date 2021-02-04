import io
import sys
from numpy import dot
from numpy.linalg import norm
from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

foods = list()
corpus = list()
for line in open('word_seq.txt', encoding='utf-8'):
    food, text = eval(line)
    foods.append(food)
    corpus.append(text)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(X).toarray()

#すし
#そば
#ちゃんぽん
food_name = 'そば'

doc_num = tfidf.shape[0]
for i in range(doc_num):
    if food_name in foods[i]:
        for j in range(doc_num):
            print('{:s} {:s} {:.8f}'.format(foods[i], foods[j], dot(tfidf[i], tfidf[j]))) #co#sine類似度
