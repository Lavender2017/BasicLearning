#coding: utf-8
import jieba
from collections import Counter
import math

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

def tf(word, count):
    # print(count[word])
    return count[word] / sum(count.values())

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)



docs = [fenci(i) for i in texts]
print(docs)
docs_1 = [deletestop(i) for i in docs]
# print(docs_1)
for i, count in enumerate(docs_1):
    print("Top words in document {}".format(i + 1))
    count = Counter(count)
    scores = {word: tfidf(word, count, docs_1) for word in count}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)#x: x[1]根据第二个元素排序
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

