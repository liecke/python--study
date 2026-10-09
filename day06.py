#通讯录：查、增、改、删、用 items() 打印全部
lt={'name':'张三','age':18,'gender':'男','number':'13344456789'}
print(lt.get('name'))
lt['age']=25#改
lt['家庭住址']='北京市朝阳区'#增
for keys in lt.items():
    print(keys)
del lt['age']#删
for keys in lt.items():
    print(keys)
print(lt.get('name'))
print(lt.get('age'))#此时age被删掉，输出none
