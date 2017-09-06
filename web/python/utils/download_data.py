# -*- coding: utf-8 -*-
from you_get.common import *
from you_get.extractors import sina,qq,iqiyi,acfun,cntv,ifeng,bilibili,youku,tudou,sohu
import pymongo
import time,random
import os
import datetime
import json
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





def export_video():
	connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
	db = connection[DB]
	collection = db[COLLECTION]
	today = datetime.date.today()
	today = today.strftime('%Y-%m-%d')
	# urls = collection.find({'content':'特朗普','status':{'$ne':0}},{'url':1,'site':1,'videoname':1})
	urls = collection.find({'keyword': '习近平', 'status': {'$ne': 0}},{"_id":0,"status":0})
	# print (type(urls))
	# print(urls)
	# output_dir = "../../static/视频抓取/文在寅/"+today+"/"
	# makepath.mkdir(output_dir)
	# print(output_dir)
	func_dict = {'sina':sina,'qq':qq,'iqiyi':iqiyi,'acfun':acfun,'cntv':cntv,'ifeng':ifeng,'bilibili':bilibili,'youku':youku,'tudou':tudou,'sohu':sohu}
	i = 0
	# today = datetime.date.today()
	# today = today.strftime('%Y-%m-%d')
	# print(today)
	title = ""
	sum = 0
	for x in urls:
		print(x)
		if i <= 100:
			pass
			try:
				func = func_dict[x['site_name']]
				if func==sina:
					i = i + 1
					print(i)
					upload_time = x['upload_time'][0:10]
					print(upload_time)
					collection.update({"url": x['url']}, {"$set": {'spider_time': today,'upload_time':upload_time,'keywords':[x['keyword']],'title_cn':x['title'],'site_name_cn':x['site_name'],'info_cn':x['info']}})
					print("000000000000000")
				elif func == iqiyi:
					# iqiyi.download(x['url'], output_dir)
					collection.update({"url":x['url']},{"$set":{'status':0}})
				logger.info("success {url}".format(url=x['url']))
				time.sleep(random.random())
				# 	outfile.close()
			except Exception as e:
				print("hghjgjghjgjgjghj")
				print(e)
				logger.debug(e)
				# continue
		else:
			break
		#add or change collection's field






if __name__ == '__main__':
	export_video()


