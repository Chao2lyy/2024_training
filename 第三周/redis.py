import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

# 字符串操作
redis_client.set('111', '卧室')
str_value = redis_client.get('卧室')
print("字符串查询结果:", str_value.decode('utf-8'))

# 列表操作
redis_client.lpush('keylist', 'item1', 'item2', 'item3')
list_items = redis_client.lrange('keylist', 0, -1)
print("列表查询结果:", list_items)

# 修改列表中的元素
redis_client.lset('keylist', 1, 'new_item2')
new_list_items = redis_client.lrange('keylist', 0, -1)
print("修改后列表查询结果:", new_list_items)

# 删除列表中的元素
redis_client.lrem('keylist', 0, 'item3')
after_delete_list_items = redis_client.lrange('keylist', 0, -1)
print("删除后列表查询结果:", after_delete_list_items)

# 集合操作
redis_client.sadd('set_key', 'item1', 'item2', 'item3')
set_members = redis_client.smembers('set_key')
print("集合查询结果:", set_members)

# 删除集合中的元素
redis_client.srem('set_key','item2')
after_delete_set_members = redis_client.smembers('set_key')
print("删除后集合查询结果:", after_delete_set_members)

# 哈希操作
redis_client.hset('hash_key', 'field1', 'value1')
redis_client.hset('hash_key', 'field2', 'value2')
hash_values = redis_client.hgetall('hash_key')
print("哈希查询结果:", hash_values)

# 修改哈希中的值
redis_client.hset('hash_key', 'field1', 'new_value1')
new_hash_values = redis_client.hgetall('hash_key')
print("修改后哈希查询结果:", new_hash_values)

# 删除哈希中的字段
redis_client.hdel('hash_key', 'field2')
after_delete_hash_values = redis_client.hgetall('hash_key')
print("删除后哈希查询结果:", after_delete_hash_values)