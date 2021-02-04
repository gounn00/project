#python read_review_word_seq.py | sort -n -r -k 3 > _review_dissim.txt
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
for line in open('review_word_seq.txt', encoding='utf-8'):
    food, text = eval(line)
    foods.append(food)
    corpus.append(text)

#max_df=
vectorizer = CountVectorizer(max_df=0.1, min_df = 1)
X = vectorizer.fit_transform(corpus)
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(X).toarray()

#1.1559 1967soba
#1.1399 1397sushi
#1.1157 1439tyanpon
review_file_name = 'index.html?use_type=0&amp;smp=1.1397'

i = foods.index(review_file_name)
doc_num = tfidf.shape[0]
for j in range(doc_num):
    print('{:s} {:s} {:.8f}'.format(foods[i], foods[j], dot(tfidf[i], tfidf[j]))) #co#sine類似度

"""
doc_num = tfidf.shape[0]
for i in range(doc_num - 1):
    for j in range(i + 1, doc_num):
        print('{:s} {:s} {:.8f}'.format(foods[i], foods[j], dot(tfidf[i], tfidf[j]))) #co#sine類似度
"""
