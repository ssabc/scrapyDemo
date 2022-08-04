## MongoDB 数据库

```shell
$ mongosh # 进入mongodb 数据库
$ show dbs # 查看所有数据库
$ use test # 切换数据库（默认的数据库就是test）
$ show collections | tables # 擦看该数据库下的所有集合(表)
$ db.集合名称.find() 查看表下面的所有记录
```

# MongoDB 其他常用命令
```shell
> db.dropDatabase() # 删除当前数据库
> db.集合名称.drop() # 删除集合
> db.集合名称.stats() # 获取当前集合的状态
> db.集合名称.deleteMany({}) # 删除集合中的数据
```

## 启动mongodb

```shell
# 前提是用[cmd管理员]模式运行
$ net start MongoDB # 启动mongodb
$ net stop MongoDB # 停止mongodb

http://localhost:27017/
```