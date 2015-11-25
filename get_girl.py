#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by carlin.wang
#__author__ = 'carlin.wang'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import random




def get_Html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"}
    req = urllib2.Request(url,headers=headers)
    res = urllib2.urlopen(req)
    res_html = res.read().decode('UTF-8')
    return res_html

def urlPages(page):
    url = "http://www.iiqr.com/page/" +str(page)
    return url

def findList(html):
    pattern = re.compile('http:\/\/www.iiqr.com\/\d+\.html',re.S)
    items = re.findall(pattern,html)
    #print items
    return items

def find_img_url(html):
    pattern = re.compile('http:\/\/www.iiqr.com\/wp-content\/uploads\/\d+\/\d+\/\d+\.jpg',re.S)
    items = re.findall(pattern,html)
    return items



def download_img(url):
    fdir = "D:/data/img"
    if not os.path.exists(fdir):
        os.makedirs(fdir)
    try:
        #(p2) = os.path.split(url)
        #(p2, f2) = os.path.split(url)
        f2 = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16))) #随机字符串作为文件名字，防止名字重复
        if os.path.exists(fdir + "/" + f2):
            print "fdir is exists"
        return url
        urllib.urlretrieve(url, fdir + "/" + f2 + ".jpg")
    except:
        return "down image error!"


def upload_qiniu(img):
    localfile = __file__
    key = 'test_file'
    mime_type = "text/plain"
    params = {'x:a': 'a'}

    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


for page in range(1,31):
    print page
    html = get_Html(urlPages(page))
    urls = findList(html)
    for url in urls:
        img_url_html = get_Html(url)
        img_urls = find_img_url(img_url_html)
        for img_url in img_urls:
            download_img(img_url)






