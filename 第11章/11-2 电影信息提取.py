import re

data = open("电影.txt", 'r', encoding='utf-8').read()

# 定义正则：匹配电影名称/评分/排名
title = r'"title":"(.*?)"'
rating = r'"rating":\["(.*?)","\d+"\]'
rank = r'"rank":(\d+)'

# 预编译正则表达式
pattern_title = re.compile(title)
pattern_rating = re.compile(rating)
pattern_rank = re.compile(rank)

# 匹配结果
data_title = pattern_title.findall(data)
data_rating = pattern_rating.findall(data)
data_rank = pattern_rank.findall(data)

for i in range(20):
    print("排名：", data_rank[i] + "\t\t" + "电影名：" + data_title[i] + "\t\t" + "评分：" + data_rating[i])
