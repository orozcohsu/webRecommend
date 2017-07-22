#!/usr/bin/python

import redis


with open('/tmp/recommend.txt') as f:
    content = f.readlines()

r = redis.Redis(host='localhost',port=6379,db=0)

#delete all data
r.flushdb()

for i in content:
    j = i.split('\t')
    r.sadd('product:'+j[1].rstrip(),'uuid:'+j[0].rstrip())


print 'keys ==> ', r.keys()

for i in r.keys():
    print i, r.smembers(i)

print 'product1 and product2 inter==>', r.sinter('product:1', 'product:2')
print 'product1 and product2 union ==>', r.sunion('product:1', 'product:2')

