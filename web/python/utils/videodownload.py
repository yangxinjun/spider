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






def export_video():
	connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
	db = connection[DB]
	collection = db[COLLECTION]
	today = datetime.date.today()
	today = today.strftime('%Y-%m-%d')
	# urls = collection.find({'content':'特朗普','status':{'$ne':0}},{'url':1,'site':1,'videoname':1})
	urls = collection.find({'keyword': '文在寅', 'status': {'$ne': 0}},{"_id":0})
	print (type(urls))
	print(urls)
	output_dir = "../../static/视频抓取/文在寅/"+today+"/"
	makepath.mkdir(output_dir)
	print(output_dir)
	func_dict = {'sina':sina,'qq':qq,'iqiyi':iqiyi,'acfun':acfun,'cntv':cntv,'ifeng':ifeng,'bilibili':bilibili,'youku':youku,'tudou':tudou,'sohu':sohu}
	i = 0
	today = datetime.date.today()
	today = today.strftime('%Y-%m-%d')
	print(today)
	title = ""
	sum = 0
	for x in urls:
		print(x)
		if i <= 10:
			try:
				func = func_dict[x['site']]
				if func==sina:
					i = i + 1
					# info, size = sina.download(x['url'], output_dir)
					size = sina.download(x['url'], output_dir)
					size = round(size, 2)
					print("11111111111")
					sum =sum +size
					print(sum)
					print(i)
					# collection.update({"url": x['url']}, {"$set": {'status': 0,'spidertime':today}})
					collection.update({"url": x['url']}, {"$set": {'status': 0,'spidertime': today,'size':size}})
					# collection.update({"url":x['url']},{"$set":{'tag':info[0],'introduction':info[1],'from':info[2],'channel':info[3],'size':size,'status':0}})
				elif func == iqiyi:
					iqiyi.download(x['url'], output_dir)
					collection.update({"url":x['url']},{"$set":{'status':0}})
				logger.info("success {url}".format(url=x['url']))
				# f=open(output_dir+x['title']+".txt",'w')
				# print (output_dir+x['title']+".txt")
				# # f.write(x)
				y = x
				# x = str(x) 字典id不是json序列，所以去掉id项
				x=json.dumps(x,ensure_ascii=False)
				title = y['keyword']
				outfile =open(output_dir+y['title'] + '.json', 'a')
				json.dump(x, outfile)
				outfile.write('\n')
				time.sleep(random.random())
				outfile.close()
			except Exception as e:
				print("hghjgjghjgjgjghj")
				print(e)
				logger.debug(e)

				continue
		else:
			break
	print(sum)
	task = {"title":title,"time":today,"keyword":title,"file_number":i,"file_size":sum}
	f = open(output_dir+'task_info.json', 'a')
	task = json.dumps(x)
	json.dump(task,f)
	f.close()
		#add or change collection's field






if __name__ == '__main__':
	export_video()


