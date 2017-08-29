# -*- coding: utf-8 -*-
from you_get.common import *
from you_get.extractors import sina,qq,iqiyi,acfun,cntv,ifeng,bilibili,youku,tudou,sohu
import pymongo
import time,random
import os

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
	urls = collection.find({'content':'金正恩','status':{'$ne':0}},{'url':1,'site':1,'videoname':1})
	print (type(urls))
	output_dir = "../../static/jinzhengen/"
	func_dict = {'sina':sina,'qq':qq,'iqiyi':iqiyi,'acfun':acfun,'cntv':cntv,'ifeng':ifeng,'bilibili':bilibili,'youku':youku,'tudou':tudou,'sohu':sohu}
	i = 0
	for x in urls:

		if i <= 99:
			print("22222222222222222")
			try:
				func = func_dict[x['site']]
				if func==sina:
					print("1333333")
					# info, size = sina.download(x['url'], output_dir)
					# sina.download(x['url'], output_dir)
					sina.download(x['url'], output_dir)
					# collection.update({"url":x['url']},{"$set":{'tag':info[0],'introduction':info[1],'from':info[2],'channel':info[3],'size':size,'status':0}})
					print("555555555")
				else:
					func.download(x['url'], output_dir)
					collection.update({"url":x['url']},{"$set":{'status':0}})
				logger.info("success {url}".format(url=x['url']))
				print("244444444444")
				print(x['videoname']+".txt")
				f=open(output_dir+x['videoname']+".txt",'w')
				print (x)
				x = str(x)
				print (type(x))
				f.write(x)
				time.sleep(random.random())
				i = i+1
			except Exception as e:
				print("hghjgjghjgjgjghj")
				logger.debug(e)
				continue
		else:
			break
		#add or change collection's field
	f.close()





if __name__ == '__main__':
	export_video()


