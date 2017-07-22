#!/usr/bin/python 

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('iii','good')

print "r.get('iii')==>", r.get('iii')
print "r['iii']==>", r['iii']

print "keys==>", r.keys()
print "size==>", r.dbsize()

print "delete iii done", r.delete('iii')

r.save()
print "save to disk, please check /var/bin/redis"

r.flushdb()
print "clean all data from redis"
