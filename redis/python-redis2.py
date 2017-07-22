#!/usr/bin/python 

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

print 'using r.pipeline() (pipeline more efficiency)'
p = r.pipeline()
p.set('iii','redis')

print "sadd('jjj','hadoop') => a collection object LIKE set)"
p.sadd('jjj','hadoop')

print "sadd('jjj','hadoop') => no action because hadoop exists"
p.sadd('jjj','hadoop')

p.sadd('jjj','spark')
p.sadd('jjj','deep learning','machine learning')

p.execute()

print r.get('hello')
print 'print jjj collection ==>', r.smembers('jjj')



