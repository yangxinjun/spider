# import json
# import codecs
# data = [{"a":"aaa","b":"bbb","c":[1,2,3,(4,5,6)]},33,'研发',True]
# task = {"title":5,"time":4,"keyword":3,"file_number":"杨新建","file_size":1}
# data2 = json.dumps(data,ensure_ascii=False)
# print(task)
# f = codecs.open('./tt.json','a',encoding='utf8')
# task=json.dumps(task, ensure_ascii=False).encode('utf8')
# print(task)
# print(data2)
# # json.dump(task,f)
# json.dump(data2,f)
# f.writelines('\n')


# contentByPage = {}
# contentByPage['document'] = shortName
# contentByPage['content'] = text
# contentByPage['pageNumber'] = pageNumber
# jsonFile = io.open(shortName+"--"+str(pageNumber)+".json",'w', encoding='utf8')
# jsonFile.write(json.dumps(contentByPage, ensure_ascii=False).decode('utf8'))
# jsonFile.flush()
# jsonFile.close()
# f = lambda