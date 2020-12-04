import os
import csv
import random
import time
import datetime
import json
import requests
from threading import Thread

class MaoYan():
    def __init__(self):
        self.USER_AGENTS = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
               "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]

        self.headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Host": "m.maoyan.com",
        # "Referer": "http://m.maoyan.com/movie/342903/comments?_v_=yes",
        'Connection': 'keep-alive',
         'Cookie': '_lxsdk_cuid=16c3d7812f1c8-0db1acfb715153-c343162-144000-16c3d7812f1c8; '
                   'iuuid=80F48AB0B1F311E9ACE911BDFB2B4D59DA83DDDBFDEC474896AD9C1C6B04A7E0; _'
                   'lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; webp=true; __mta=121011895.'
                   '1564399381347.1569984019227.1569984446772.16; __mta=121011895.1564399381347.1569986804187.1569986816408.25;'
                   ' ci=224%2C%E6%BD%8D%E5%9D%8A; _lxsdk=80F48AB0B1F311E9ACE911BDFB2B4D59DA83DDDBFDEC474896AD9C1C6B04A7E0;'
                   ' _lxsdk_s=16d94106b96-682-5dd-a93%7C%7C11'
    }
        self.data = [None, None, None, None, None]

 # 发送get请求
    def get_json(self, url, headers):
        # 发送get请求
        try:
            response_comment = requests.get(url, headers=headers)
        except Exception as err:
            print(err)
            return None
        json_comment = response_comment.text
        try:
            json_comment = json.loads(json_comment)
            print(json_comment)
        except:
            print("error")
            return None
        return json_comment

    def save_title(self, index):
        title = ['cityName', 'content', 'gender', 'nickName', 'userLevel', 'score', 'time', 'date']
        with open('SHBL_new_{}.csv'.format(index), 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, title)
            writer.writeheader()


    def save_data(self, data, index):
        with open('SHBL_new_{}.csv'.format(index), 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            title = ['cityName','content','gender','nickName','userLevel','score','time','date', 'evaluate']
            writer.writerow([data[i] for i in title])
        print('*' * 10 + '保存成功' + '*' * 10)


    # 获取数据并存储
    def get_data(self, json_comment, index):
        json_response = json_comment["cmts"]  # 列表
        # print(json_response)
        print(len(json_response))
        list_info = {}
        for self.data[index] in json_response:
            list_info['cityName'] = self.data[index].get("cityName")
            list_info['content'] = self.data[index].get("content").replace("\r\n","").replace("\n","")
            if "gender" in self.data[index]:
                list_info['gender'] = self.data[index].get("gender")
            else:
                list_info['gender'] = 0
            list_info['nickName'] = self.data[index].get("nickName")
            list_info['userLevel'] = self.data[index].get("userLevel")
            list_info['score'] = self.data[index].get("score")
            list_info['time'] = self.data[index].get("startTime")
            list_info['date'] = self.data[index].get("startTime").split()[0]
            # print(data.get('tagList')['fixed'][0]['name'])

            try:
                list_info['evaluate'] = self.data[index].get('tagList')['fixed'][0]['name']
            except TypeError as e:
                list_info['evaluate'] = 'unkown'
            self.save_data(list_info, index)
            print(self.data)

        # return data


    def spider_maoyan(self, spread, index):
        start_time, end_time = spread.split(',')
        # start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # end_time = '2019-09-30 09:00:00'
        self.save_title(index)
        offset = 0
        print(start_time, end_time)
        local_time = start_time
        while start_time > end_time:
            comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1210778.json?_v_=yes&offset={}&startTime={}'.format(offset, start_time.replace(' ', '%20'))
            print(comment_api)
            if offset == 1005:
                start_time = self.data[index].get("startTime")
                offset = 15
                continue
            json_comment = self.get_json(url=comment_api, headers=self.headers)
            if(json_comment == None):
                continue
            self.get_data(json_comment, index)
            if self.data[index].get("startTime") <= end_time:
                break

            # start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=-1)
            # start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')
            print(start_time)
            offset += 15
            time.sleep(1)


    def multiThread(self):
        data_range = ['2020-09-15 18:19:00,  2019-09-15 08:30:00',
                      '2020-09-16 18:32:00,  2019-09-16 08:30:00',


                      ]
        #   '2019-10-02 08:30:00, 2019-10-01 20:30:00',
        #                       '2019-10-01 20:30:00, 2019-10-01 08:30:00',
        #                       '2019-10-01 08:30:00, 2019-09-30 20:30:00',
        #                       '2019-09-30 20:30:00, 2019-09-30 09:00:00'

        threads = []
        for i in range(len(data_range)):
            print(data_range[i])
            thread = Thread(target=self.spider_maoyan,
                            args=(data_range[i], i))
            threads.append(thread)

        for i in range(len(data_range)):
            threads[i].start()

        for i in range(len(data_range)):
            threads[i].join()


if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.multiThread()