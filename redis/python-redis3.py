#!/usr/bin/python 

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.hset('name:Orozco','age','18')
r.hset('name:Orozco','email','orozcohsu@hotmail.com')
r.hset('name:Orozco','phone','0123456789')

r.hincrby('users:Orozco', 'view', 1)

print 'View Orozco ==>', r.hgetall('name:Orozco')
print 'Orozco hash-key', r.hkeys('name:Orozco')
