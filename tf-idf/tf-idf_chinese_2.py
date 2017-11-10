#coding: utf-8
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer



texts=[]
for i in range(3):
    with open('text'+str(i+1)+'.txt') as fr:
        texts+=fr.readlines()
# print(texts[0])
def creadstoplist():
    stwlist = [line.strip()
               for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
    return stwlist
stwlist = creadstoplist()
def deletestop(wordlist):
    outlist = []
    for word in wordlist:
        if word not in stwlist:
            outlist.append(word)
    return outlist

def fenci(text):
    doc = jieba.cut(text,cut_all=False)
    return doc

docs = [fenci(i) for i in texts]
docs_1 = [deletestop(i) for i in docs]
# print(list(docs_1))
texts = []
for i, count in enumerate(docs_1):
    count = ' '.join(count)
    texts.append(count)
# print(texts)
vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
tfidf = transformer.fit_transform(vectorizer.fit_transform(texts))
weight = tfidf.toarray()
word = vectorizer.get_feature_names()
for i in range(len(weight)):
    print('第'+str(i+1)+'个文档中词语对应的TF-IDF值：')
    score = dict(zip(word, weight[i]))
    # print(score)
    print('dddddddddddddddddddddddddddddddddddddd')
    sorted_words = sorted(score.items(), key=lambda x: x[1], reverse=True)  # x: x[1]根据第二个元素排序
    # print(sorted_words)
    for i in sorted_words[:3]:
        print(i)

