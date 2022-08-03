## 命令行操作

>1. 安装
[python官网](https://www.python.org/downloads)
```shell
  $ pip install scrapy # 安装scrapy包
```
>2. 使用
```shell
	$ scrapy startproject mySpider # 创建一个爬虫项目
```
```shell
	$ scrapy genspider demo "demo.cn" # 生成一个爬虫
```
>3.  运行
```shell
	$ scrapy crawl demo # demo爬虫的名字
```

### 实战Demo
```shell
$ scrapy startproject huabaike # 创建一个scrapy项目
```
```shell
$ scrapy genspider home “huabaike.com” # 生成一个爬虫 scrapy genspider 爬虫文件名称 要爬取的域名
```
## 制作爬虫开始爬取网页 spiders/home.py
  ```python
   class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['huabaike.com']
    start_urls = ['https://www.huabaike.com/jingtian/']

    def parse(self, response):
        for quoteUl in response.css('div.zhiwuImg ul'):
            for quoteli in quoteUl.css('li'):
                yield {
                    'name': quoteli.css('a::text').extract_first(),
                    'img': quoteli.css('a img::attr(src)').extract()[0]
                }
  ```
## 设计管道存储爬取内容 pelines.py

```python
import json
import codecs
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class DemoPipeline:
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        self.file = codecs.open('data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item 
```  

## 修改配置 settings.py

避免在程序运行的时候打印log日志信息

```js
 LOG_LEVEL = 'WARNING' 
 ROBOTSTXT_OBEY = False
```

开启管道
```js
ITEM_PIPELINES = {
    'demo.pipelines.DemoPipeline': 300,
}
```

## 运行得到数据应用数据 

// 在命令中运行爬虫

```shell
$ scrapy crawl home # qb爬虫的名字
```
