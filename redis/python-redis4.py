#!/usr/bin/python 

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.sadd('DL:CPU:cnn','user:andy')
r.sadd('DL:CPU:cnn','user:bill')
r.sadd('DL:CPU:cnn','user:candy')
r.sadd('DL:GPU:lstm','user:candy')
r.sadd('DL:GPU:lstm','user:edward')
r.sadd('DL:GPU:lstm','user:bill')

print 'cnn user ==>', r.smembers('DL:CPU:cnn')

print 'inter ==>', r.sinter('DL:CPU:cnn', 'DL:GPU:lstm')
print 'both ==>', r.sunion('DL:CPU:cnn', 'DL:GPU:lstm')

