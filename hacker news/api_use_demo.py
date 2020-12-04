
#! /usr/bin/python <br> # -*- coding: utf8 -*-
import requests
from operator import itemgetter


#! /usr/bin/python <br> # -*- coding: utf8 -*-
import requests
import pandas as pd
def gethtml(url):
  i = 0
  while i < 5:
    try:
      html = requests.get(url, timeout=5)
      return html
    except requests.exceptions.RequestException:
      i += 1


#执行API调用并储存响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code : ",r.status_code)

submisssion_dicts = []
#获取news的id
submisssion_ids = r.json()
# print(submisssion_ids)
print(submisssion_ids)
shuixng = ['by', 'descendants', 'id', 'kids', 'score', 'time', 'title', 'type', 'url']
for submisssion_id in submisssion_ids:
    # 处理有关每篇文章的信息
    url = 'https://hacker-news.firebaseio.com/v0/item/'+str(submisssion_id)+'.json'

    try:
        submisssion_r = gethtml(url)
    except Exception:
        print(url)
    response_dict = submisssion_r.json()
    submisssion_dicts.append(response_dict)
    print(submisssion_id)

data_df = pd.DataFrame(submisssion_dicts)
data_df.to_csv('data.csv')
