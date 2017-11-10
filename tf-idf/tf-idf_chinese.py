#coding: utf-8
import jieba
from collections import Counter
import math

text1 = '关于文学图书，集团旗下北京十月文艺出版社长期立足“原创的、当代的”精品战略，' \
        '2017年又添新品力作。如肖复兴的《我们的老院》、高建群的《我的菩提树》、王凯的《沉默的中士》、' \
        '马笑泉的《迷城》等。特别是《人民的名义》，于2017年开年“横空出世”，突破了传统反腐题材文艺创作的套路，' \
        '以宏大的格局、深刻的思想与动人的情节，书写出了我们这个时代的精神风骨与正气之歌，目前累计销量已突破150余万册。' \
        '另外一部值得期待的还有作家宁肯的最新长篇小说《中关村笔记》。在这部作品中，宁肯将视线聚拢于中国改革开放缩影的北京' \
        '中关村地区，以20多万字的笔墨，书写了中关村几十年里的风云激荡。选取中关村如柳传志、王选、冯康、吴甘沙、程维等不同时代、' \
        '成就卓著的代表人物，通过各自不同的侧重点，有如编织不同的乐章，展现每位先进人物怀抱理想、搏击奋斗的艰辛历程，' \
        '展现大国崛起与不断创新的精神，展现一代人的中国梦如何一步步成为现实。另外，继《世间已无陈金芳》之后，' \
        '青年作家石一枫再推新作品集《特别能战斗》。书中的主人公是一位精力旺盛、嫉恶如仇的北京大妈。上班时不断和领导斗，和同事斗，' \
        '和她看不惯的一切行为斗，退休后又和物业斗，在无休无止的战斗中，演绎了一段人生悲喜剧。《特别能战斗》的出版也为北京十月文艺出版社' \
        '“70后作家群”再添新品，甫一推出就获得媒体好评，荣登各大媒体好书推荐榜。纪实文学方面，记述57年前从北坡成功登上世界之巅的珠穆朗玛峰' \
        '震撼世界这一传奇历史的《珠峰北坡·极地使命》惊艳亮相，该书史料翔实，文字质朴，是目前我国首次从北坡登顶珠峰题材图书中资料最为完整的一部纪实文学作品。'

text2 = '在人文社科类方面，本次出展，北京出版集团集中展现了“大家小书”整体风貌的“大家小书”精装典藏箱装版。' \
        '自2002年“大家小书”首辑出版以来，经过十多年的沉淀与积累，“大家小书”目前已成为国学普及类体量最大的丛书，' \
        '并于2015年全品种入选了国家新闻出版广电总局“首届向全国推荐中华优秀传统文化普及图书名单”，' \
        '其中的《苏辛词说》荣膺中国图书评论学会“2015中国好书”，《中国古代建筑概说》获选“2016中国好书”，' \
        '2016年“大家小书”系列被评为中国出版协会“2016年度中国30本好书”。该套箱装收录了大家小书最经典的100本佳作，' \
        '并根据书的学科和市场读者的不同喜好将此百种佳作分七大类呈现。另外，作为“大家小书”系列的新成员，' \
        '“大家小书·译馆”系列第一辑也隆重上市，该系列秉承“大家小书”的理念，不忘“大家写给大家看的书”的初衷，' \
        '精选有代表性的外国文化的优秀读物，所选作品均出自各国大家，题材各异，体裁不限。如《书的故事》，名作名译，相得益彰，' \
        '作者是大名鼎鼎的《十万个为什么》的作者伊林，译者是“最后的闺秀”、张家“二姐”张允和。作为张允和本人唯一的一部译作，本书用一个又一个的小故事引出主题，介绍了文字和书籍的发展史，可读性强。'

text3 = '在生活类图书方面，北京出版集团联合中山大学附属第三医院各科专家合力编写的“专家细说常见病”全辑共13册，每一分册针对一常见病种,' \
        '如高血压、胆囊炎、颈椎病等，详实介绍这些常见病的基础知识、发病机制、诊断与治疗方法，诊治过程中注意事项以及家庭养护要点，内容权威实用。' \
        '由集团旗下父母必读育儿传媒出版的、引爆欧洲的育儿畅销书《童年清单》首次亮相，该书给中国家长带来69项体验清单，涉及生活实践、社会意识、身体运动机能、' \
        '生理认知和审美观等方面，清晰实用，不仅为中国早期教育研究提供了一个新的研究理念和视角，也为儿童认知世界提供了一种新的眼光和思路。' \
        '集团旗下的京版梅尔杜蒙公司推出了《一路向心——在空气稀薄地带骑行》，作者是80后非典型理工男，程序“猿”，更是穷游网热帖博主、蚂蜂窝旅行家专栏作家，' \
        '他一个人一辆单车骑行川藏线、阿里北线、阿里南线、中尼公路，总里程达到6000公里。书中的24个故事，记录了骑行过程中遇到的人、发生的事，充满浪漫和感动。'

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



texts = [text1,text2,text3]

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

