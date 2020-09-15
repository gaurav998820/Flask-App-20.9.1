from redis import StrictRedis,Redis
from Flask.app import factorial

#create redis connection object
r = Redis(host='redis-18252.c212.ap-south-1-1.ec2.cloud.redislabs.com',port='18252',password='4AOSmHLSWtRMH6aBKjbqVeq46dybSDww$$',
          db=0,decode_responses='true')
#testing redis working set the value of key foo
r.hsetnx('sample','foo','Gupta')
r.hsetnx('sample','foo1','Gaurav2')
r.set('koo','Gaurav1')
#retrieve and print values
print(r.hexists('sample','foo'))
if (r.hexists('sample','foo'))!='True':
    r.hsetnx('sample','foo','Gupta2')
    print(r.hget('sample','foo'))
    print(r.hgetall('sample'))
else:
    print('No values')

#print('flushing all data+++')
#r.flushdb()
#r.flushall()
#r.close()

def factorial_cache(num):
    number=num
    print('number is :::::', number)
    print('client ID and client name is :::::', r.client_id(),r.client_getname())
    print('print all values in factorial', r.hgetall('factorial'))
    print('print if cache exists', r.hexists('factorial','number'))
    fac_result = factorial.factorial(number)
    r.hset('factorial','number','fac_result')
    print('print all values in factorial after setting-->', r.hgetall('factorial'))
    print('print factorial is-->',fac_result )
    if(r.hexists('factorial','number') == 'True') & (r.hget('factorial','number') != 'fac_result'):
        print(r.hget('factorial','number'))
        fac_result = r.hget('factorial','number')
        print('getting cached results for:: ', number)
        return fac_result
    else:
        print('setting cache result for', number)
        r.hsetnx('factorial','number','fac_result')
        print('in setting cache block-->',r.hgetall('factorial'))
        return fac_result

def factorial_flush():
    #r.flushdb('factorial')
    r.flushall('factorial')

