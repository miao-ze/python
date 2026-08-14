# 1，导入redis包
import redis

if __name__ == '__main__':
    # 在连接外界的资源时一定要注意使用try
    try:
        # 2. 创建redis的连接实例
        # host：连接的对象可以是对方的ip地址
        # port；端口号为6379
        # db： 进行操作的数据库
        re = redis.Redis(host='localhost',port=6379,db=1)
    except Exception as e:
        print(e)
    else:
        #3. 操作string
        # 3.1 添加
        result = re.set("string1","1")             #单添加
        re.mset({'string2':'2','string3':'3'})                  #多添加
        # 3.3 删除
        re.delete('string3')
        # 3.2 获取
        print(re.get('string2'))
        # 3.4 追加
        re.append('string2','1212')
        print(re.get('string2'))
        # *获取当前库的所有key
        all_keys = re.keys('*')
        print(all_keys)
        # *设置过期时间
        re.setex('string3',20,'3')
        print(re.ttl('string3'))

        # 4. 操作hash
        re.hset('hash1','num1','1')             #单添加
        print(re.hget('hash1','num1'))                #查看单个
        re.hset('hash2',mapping={'num2':'2','num3':'3'})   #多添加
        print(re.hmget('hash2',['num2','num3']))     #查看多个
        print(re.hgetall('hash2'))                               #查看所有元素
        print(re.hkeys('hash2'))                                #查看所有键
        print(re.hvals('hash2'))                                #查看所有值

        # 5.操作列表
        re.lpush('list1',"1","2","3","4")       #创建并添加元素
        print(re.lrange('list1',0,-1))       #查看所有元素
        re.lrem('list1',0,"4")             #删除元素
        print(re.lrange('list1', 0, -1))
        re.lset('list1',2,'333333')        #列表更新
        print(re.lrange('list1', 0, -1))
        re.linsert('list1','before','333333','3')  #插入元素
        print(re.lrange('list1', 0, -1))
        #
        #6.无序集合操作
        re.sadd('set1','1','2','3')   #创建并添加
        print(re.smembers('set1'))                  #查询操作
        re.srem('set1','3')                                #删除操作
        print(re.smembers('set1'))

        #7.有序集合操作


