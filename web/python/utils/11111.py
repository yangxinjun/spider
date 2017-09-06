
import json

def add():
    out = "../../static/视频抓取/默克尔/2017-08-31/"
    output_dir = "../../static/视频抓取/默克尔/2017-08-31/默克尔.txt"
    filename = open(output_dir)
    for x in filename.readlines():
        # print(type(x))
        x= x.strip()
        x = x+'.json'
        name = out +x
        # print(name)
        qingxi(name)
        # with open out as f:

def qingxi(out):
    y = {}
    try:
        with open(out) as f:
            str = f.readlines()
            # print(type(str)
            str = str[0]
            print(str)
            x = eval(str)
            print(x)
            print(type(x))
            x['keywords'] = ['默克尔']
            print(x)
            y =x
            # x = json.dumps(x)
            # f.write(x)
            # t = '['
            # print(t)
            # if str.find(t)>0:
            #     print("000000")
            #     pass
            # else:
            #     print("112111")
            #     str.replace('"\u4e60\u8fd1\u5e73"','["\u4e60\u8fd1\u5e73"]')
            # print(str)
            # # # if str.__contains__('"keywords": "\\u4e60\\u8fd1\\u5e73"'):
    except Exception as e:
        print(e)
    try:
        with open(out,'w+') as f:
            y = json.dumps(y)
            f.write(y)
    except Exception as e:
        print(e)





add()