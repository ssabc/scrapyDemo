## MongoDB 数据库

```shell
$ mongosh # 进入mongodb 数据库
$ show dbs # 查看所有数据库
$ use test # 切换数据库（默认的数据库就是test）
$ show tables # 擦看该数据库下的所有表
$ db.[表名称].find() 查看表下面的所有记录
```


## 启动mongodb

```shell
# 前提是用[cmd管理员]模式运行
$ net start MongoDB # 启动mongodb
$ net stop MongoDB # 停止mongodb

http://localhost:27017/
```