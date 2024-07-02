#字典
a={'xixi ':10,'hhh':55}
# print(type(a))
# a['xixi']=666 
# print(a)
a['hhh']=78  #在字典中存在的键，会进行更改相应的值，
print(a)
a['new']=99   #在字典中不存在的键，直接追加到字典尾部
print(a)

#删除
del a['hhh']  # 删除按钮
print (a)