# -*- coding: utf-8 -*-
from you_get.common import *
from you_get.extractors import sina,qq,iqiyi,acfun,cntv,ifeng,bilibili,youku,tudou,sohu
import pymongo
import time,random
import os
import datetime
import json
import  mkpath as makepath
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
	today = "2017-08-31"
	# urls = collection.find({'content':'特朗普','status':{'$ne':0}},{'url':1,'site':1,'videoname':1})
	# urls = collection.find({'keyword': '文在寅', 'status': {'$ne': 0}},{"_id":0,"status":0})
	urls = collection.find({'site_name_cn':{"$exists": 1},'title_cn':{"$exists": 1},'keywords': '金正恩', 'status': {'$ne': 0}}, {"_id": 0, "status": 0,"keyword":0})
	print (type(urls))
	print(urls)
	output_dir = "../../static/视频抓取/金正恩/"+today+"/"
	makepath.mkdir(output_dir)
	print(output_dir)
	func_dict = {'sina':sina,'qq':qq,'iqiyi':iqiyi,'acfun':acfun,'cntv':cntv,'ifeng':ifeng,'bilibili':bilibili,'youku':youku,'tudou':tudou,'sohu':sohu}
	i = 0
	title = ""
	sum = 0
	for x in urls:
		print(x)
		if i <= 95:
			try:
				func = func_dict[x['site_name']]
				if func==sina:

					# info, size = sina.download(x['url'], output_dir)
					# size = sina.download(x['url'], output_dir)
					# size = round(size, 2)
					# print("11111111111")
					# sum =sum +size
					# print(sum)
					# print(i)
					i = i + 1
					# collection.update({"url": x['url']}, {"$set": {'spider_time': today,'title_on':x['title'],'site_name_cn':x['site_name'],'info_cn':x['info']}})
					# collection.
					# earn.earn(x)
					# collection.update({"url": x['url']}, {"$set": {'status': 0,'spidertime':today}})
					# collection.update({"url":x['url']},{"$set":{'tag':info[0],'introduction':info[1],'from':info[2],'channel':info[3],'size':size,'status':0}})
					# t = collection.find({'keyword': '文在寅', 'upload_time': x['upload_time'], 'play_count': x['play_count'],'spider_time': x['spider_time']}, {"_id": 0, "status": 0})
					# print(t)
					# print("oooooooo")
					# for x in t:
					# print(x)
					# y = x
					# # x = str(x) 字典id不是json序列，所以去掉id项
					# x = json.dumps(x)
					# print(x)
					# title = y['keyword']
					# outfile = open(output_dir + y['title'] + '.json', 'a')
					# print(outfile)
					# json.dump(x, outfile)
					# print("11111111111")
					# outfile.write('\n')
					# print("22222222222222")
					# time.sleep(random.random())
					# outfile.close()
				elif func == iqiyi:
					iqiyi.download(x['url'], output_dir)
					collection.update({"url":x['url']},{"$set":{'status':0}})
				logger.info("success {url}".format(url=x['url']))
				# f=open(output_dir+x['title']+".txt",'w')
				# print (output_dir+x['title']+".txt")
				# # f.write(x)
				# t = collection.find({'keyword': '文在寅','upload_time': x['upload_time'],'play_count':x['play_count'],'spider_time':x['spider_time']},{"_id":0,"status":0})
				# print(t)
				# print("oooooooo")
				# for x in t:
				print(x)
				y = x
				# x = str(x) 字典id不是json序列，所以去掉id项
				x=json.dumps(x)
				print(x)
				title = y['keywords']
				outfile =open(output_dir+y['title'] + '.json', 'w+')
				outfile.write(x)
				outfile.write('\n')
				time.sleep(random.random())
				outfile.close()
			except Exception as e:
				print("hghjgjghjgjgjghj")
				print(e)
				logger.debug(e)
				# continue
		else:
			break
	# i = i-1
	# print(sum)
	# sum = str(sum)
	# sum = sum +"M"
	# task = {"title":title,"time":today,"keywords":title,"file_number":i,"file_size":sum}
	# f = open(output_dir+'task_info.json', 'w+')
	# task = json.dumps(task)
	# f.write(task)
	# f.close()
	print("11111111111111111111111")
		#add or change collection's field






if __name__ == '__main__':
	export_video()


