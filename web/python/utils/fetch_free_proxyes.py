#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import logging
from lxml import etree

logger = logging.getLogger(__name__)

def get_html(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36")
    html = urllib.request.urlopen(request)
    return html.read()

def get_soup(url):
    soup = BeautifulSoup(get_html(url), "html.parser")
    return soup

def fetch_kxdaili(page):
    """
    从www.kxdaili.com抓取免费代理
    """
    proxyes = []
    try:
        url = "http://www.kxdaili.com/dailiip/1/%d.html" % page
        soup = get_soup(url)
        table_tag = soup.find("table", attrs={"class": "ui table segment"})
        trs = table_tag.tbody.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            latency = tds[4].text.split(" ")[0]
            # print ip,':',port,' ',latency
            if float(latency) < 10: # 输出延迟小于0.5秒的代理
                # print ip,':',port,' ',latency
                proxy = "%s:%s" % (ip, port)
                proxyes.append(proxy)
    except:
        pass
        # logger.warning("fail to fetch from kxdaili")
    return proxyes

def img2port(img_url):
    """
    mimvp.com的端口号用图片来显示, 本函数将图片url转为端口, 目前的临时性方法并不准确
    """
    code = img_url.split("=")[-1]
    if code.find("4vMpAO0OO0O")>0:
        return 80
    elif code.find("4vMpDg4")>0:
    	return 8088
    elif code.find("4vMpDgw")>0:
    	return 8080
    elif code.find("5vOpTk5")>0:
    	return 9999
    elif code.find("yvMpDAwMAO0OO0O")>0:
    	return 20000
    elif code.find("4vOpDg4")>0:
    	return 8888
    elif code.find("zvMpTI4")>0:
    	return 3128
    elif code.find("5vMpDAw")>0:
    	return 9000
    elif code.find("4vMpQO0OO0O")>0:
    	return 81
    elif code.find("5vNpzk3")>0:
    	return 9797
    elif code.find("4vMpDAw")>0:
    	return 8000
    elif code.find("4vMpTE4")>0:
    	return 8118
    else:
        return None

def fetch_mimvp():
    """
    从http://proxy.mimvp.com/free.php抓免费代理
    """
    proxyes = []
    try:
        url = "http://proxy.mimvp.com/free.php?proxy=in_hp"
        soup = get_soup(url)
        # print soup
        table = soup.find("table", attrs={"class": "table"})
        tds = soup.find_all("td")
        for i in range(0, len(tds), 10):
            # print tds[i]
            id = tds[i].text
            ip = tds[i+1].text
            port = img2port(tds[i+2].img["src"])
            response_time = tds[i+7]["title"][:-1]
            transport_time = tds[i+8]["title"][:-1]
            if port is not None and float(response_time) < 10 :
                proxy = "%s:%s" % (ip, port)
                proxyes.append(proxy)
    except Exception as e:
        pass
        # logger.warning("fail to fetch from mimvp")
    return proxyes

def fetch_xici():
    """
    http://www.xicidaili.com/nn/
    """
    proxyes = []
    try:
        url = "http://www.xicidaili.com/nn/"
        soup = get_soup(url)
        table = soup.find("table", attrs={"id": "ip_list"})
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            tr = trs[i]
            tds = tr.find_all("td")
            ip = tds[1].text
            port = tds[2].text
            speed = tds[6].div["title"][:-1]
            latency = tds[7].div["title"][:-1]
            if float(speed) < 10 and float(latency) < 10:
                proxyes.append("%s:%s" % (ip, port))
    except Exception as e:
        pass
        # logger.warning("fail to fetch from xici")
    return proxyes

def fetch_ip181():
    """
    http://www.ip181.com/
    """
    proxyes = []
    try:
        url = "http://www.ip181.com/"
        soup = get_soup(url)
        table = soup.find("table")
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            tds = trs[i].find_all("td")
            ip = tds[0].text
            port = tds[1].text
            latency = tds[4].text[:-2]
            if float(latency) < 10:
                proxyes.append("%s:%s" % (ip, port))
    except Exception as e:
        pass
        # logger.warning("fail to fetch from ip181: %s" % e)
    return proxyes

def fetch_httpdaili():
    """
    http://www.httpdaili.com/mfdl/
    更新比较频繁
    """
    proxyes = []
    try:
        url = "http://www.httpdaili.com/mfdl/"
        soup = get_soup(url)
        table = soup.find("div", attrs={"kb-item-wrap11"}).table
        trs = table.find_all("tr")
        for i in range(1, len(trs)):
            try:
                tds = trs[i].find_all("td")
                ip = tds[0].text
                port = tds[1].text
                type = tds[2].text
                if type == u"匿名":
                    proxyes.append("%s:%s" % (ip, port))
            except:
                pass
    except Exception as e:
        pass
        # logger.warning("fail to fetch from httpdaili: %s" % e)
    return proxyes

def fetch_66ip():
    """    
    http://www.66ip.cn/
    每次打开此链接都能得到一批代理, 速度不保证
    """
    proxyes = []
    try:
        # 修改getnum大小可以一次获取不同数量的代理
        url = "http://www.66ip.cn/nmtq.php?getnum=10&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip"
        content = get_html(url)
        urls = content.split("</script>")[-2].split("<br/>")[0:-2]
        for u in urls:
            if u.strip():
                proxyes.append(u.strip())
    except Exception as e:
        pass
        # logger.warning("fail to fetch from httpdaili: %s" % e)
    return proxyes

    

def check(proxy):
    import urllib.request
    url = "http://www.baidu.com/js/bdsug.js?v=1.0.3.0"
    proxy_handler = urllib.request.ProxyHandler({'http': "http://" + proxy})
    opener = urllib.request.build_opener(proxy_handler,urllib.request.HTTPHandler)
    try:
        response = opener.open(url,timeout=0.1)
        return response.code == 200
    except Exception:
        return False

def fetch_all(endpage=10):
    proxyes = []
    for i in range(1, endpage):
        proxyes += fetch_kxdaili(i)
    proxyes += fetch_mimvp()
    proxyes += fetch_xici()
    proxyes += fetch_ip181()
    proxyes += fetch_httpdaili()
    proxyes += fetch_66ip()
    valid_proxyes = []
    # return proxyes
    # logger.info("checking proxyes validation")
    for p in proxyes:
        if check(p):
            valid_proxyes.append(p)
    return valid_proxyes

def ipwrite():
    proxyes = fetch_all()
    # logger.info(proxyes)
    with open("proxyes.dat", "w") as fd:
            for i in proxyes:
                fd.write(i+"\n") # 只保存有效的代理


if __name__ == '__main__':
    import sys
    root_logger = logging.getLogger("")
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(name)-8s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(stream_handler)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    proxyes = fetch_all()
    #print check("202.29.238.242:3128")
    for p in proxyes:
        print (p)
