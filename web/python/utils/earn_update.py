# -*- coding: utf-8 -*-
from you_get.common import *
from you_get.extractors import sina,qq,iqiyi,acfun,cntv,ifeng,bilibili,youku,tudou,sohu
import pymongo
import time,random
import os
import datetime
import json
import  web.python.utils.mkpath as makepath
#add sys.path
import logging.config
path = os.path.abspath(__file__).replace('\\','/').split('/')
logfile = os.path.join( '/'.join(path[:-2]),"logger.conf")
logging.config.fileConfig(logfile)
logger = logging.getLogger("video")


#db setting
MONGODB_SERVER = '127.0.0.1'
MONGODB_PORT = 27017
DB = 'video'
COLLECTION = 'urlinfo'


#view model path
print (os.path.dirname(sina.__file__))






def earn(x):
    connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = connection[DB]
    collection = db[COLLECTION]
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    t = collection.find({'keyword': '文在寅', 'upload_time': x['upload_time'], 'play_count': x['play_count'],'spider_time': x['spider_time']}, {"_id": 0, "status": 0})
    output_dir = "../../static/视频抓取/文在寅/" + today + "/"
    makepath.mkdir(output_dir)
    print(output_dir)
    print(t)
    print("oooooooo")
    for x in t:
        print(x)
        y = x
        # x = str(x) 字典id不是json序列，所以去掉id项
        x = json.dumps(x)
        print(x)
        title = y['keyword']
        outfile = open(output_dir + y['title'] + '.json', 'a')
        print(outfile)
        json.dump(x, outfile)
        print("11111111111")
        outfile.write('\n')
        print("22222222222222")
        outfile.close()










