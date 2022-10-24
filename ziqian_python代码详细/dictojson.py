#!/usr/bin/python3
import json
 
#python字典类型转换为json对象
data = {
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
}
data2 = [{
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
},{
    'id' : 2,
    'name' : 'test2',
    'age' : '2'
}]
 
json_str = json.dumps(data)
print ("python原始数据：", repr(data))
print ("json对象：", json_str)
 
json_str2 = json.dumps(data2)
print ("python原始数据：", repr(data2))
print ("json对象：", json_str2)
	
 
# 将json对象转换为python字典
data3 = json.loads(json_str)
print ("data3['name']: ", data3['name'])
print ("data3['age']: ", data3['age'])