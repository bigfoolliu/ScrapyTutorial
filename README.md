# scrapy基础知识

**制作 Scrapy 爬虫 一共需要4步:**

1. 新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
2. 明确目标 （编写items.py）：明确你想要抓取的目标
3. 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
4. 存储内容 （pipelines.py）：设计管道存储爬取内容

**核心组件:**

1. 引擎(Engine), 和各组件交互
2. 管道(Item Pipeline), 接收并保存item数据
3. 爬虫(Spider), 第一批的url地址以及解析响应的方法
4. 下载器(Downloader), 并发发送请求返回响应
5. 调度器(Scheduler), 对每一个请求去重处理并将去重请求放入队列

*所有的组件都直接和引擎交互,从而降低耦合度,只需要编写爬虫和管道的代码!*

**三大对象:**

1. Request对象
2. Response对象
3. Item对象

**两大可选中间件:**

1. 下载中间件(Downloader Middleware)
2. 爬虫中间件(Spider Middleware)

*对失败的请求会重试, 当重试三次失败则会丢弃请求.*

相关命令:

```text
终端常用命令:
scrapy startproject projectName: 创建一个新的项目

scrapy genspider baidu "baidu.com": 创建一个使用默认模板的爬虫, 且爬取的域名有限制

scrapy list: 查看当前爬虫的列表

scrapy runspider baidu.py: 执行爬虫
scrapy crawl baidu: 执行爬虫(推荐,不必需要指定具体的文件)

scrapy crawl baidu -o data/baidu_result.json: 执行爬虫,并将结果保存指定目录下的json格式文件(还默认支持csv、xml、jl等)
```

**Request对象和Response对象的属性:**

```text
Request对象的属性:

Response对象的属性:
    response.url: 响应 url地址
    response.haeders: 响应报头
    response.body: 网页原始编码字符串
    response.text: 网页Unicode编码字符串

从response中提取字符串:
    response.xpath("//title/text()").extract()  # 返回所有结果的字符串列表,没有匹配到则返回空列表
    response.xpath("//title/text()").extract_first()  # 返回第一个匹配到的结果,没有匹配到则返回None
```

