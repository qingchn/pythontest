#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by carlin.wang
#for upload js html to CDN
import httplib
import urllib
import urllib2



index_url = 'http://192.168.8.161:9090/cdn?ak=57375315e710d4538f785454e3eb52b5e0f64ae9&sk=cb66403bf94e7d71e229230eab78319b4ed1ac9f&bucketName=resmaxmob&fileEntities=[{"fileName":"index.html","filePath":"/data/www/maxmobres/tracker/index.html","fileKey":"tracker/index.html"}]'
js_url = 'http://192.168.8.161:9090/cdn?ak=57375315e710d4538f785454e3eb52b5e0f64ae9&sk=cb66403bf94e7d71e229230eab78319b4ed1ac9f&bucketName=resmaxmob&fileEntities=[{"fileName":"mmTrack.min.js","filePath":"/data/www/maxmobres/tracker/mmTrack.min.js","fileKey":"tracker/mmTrack.min.js"}]'

def upload_get(url):
    req = urllib2.Request(url)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    if res:
        print "upload url is OK"
    else:
        print "upload url is not OK,Please check it"


upload_get(index_url)
upload_get(js_url)


