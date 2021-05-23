import scrapy
from pyquery import PyQuery as PyQuery
from bs4 import BeautifulSoup
from myScrapy.items import SmzdmItem

class SmzdmCrawler(scrapy.Spider):
    name='smzdm'
    # start_urls=['https://faxian.smzdm.com/']
    start_urls=["http://www.ahpu.edu.cn/"]
    def parse(self,response):
        # res=pq(response.body)
        # response.body.decode('gbk')
        filename=response.url.split("/")[-2]
        print(filename)
        # with open (filename,'a','utf-8') as f:
        #     f.write(response.text)
        f =open(filename,'w',encoding='utf-8')
        f.write(response.text)
        f.close()
        start_urls="http://www.ahpu.edu.cn/"
        res=BeautifulSoup(response.text,'lxml')
        link=res.select('a')
        # print(link)
        # print(link[1])
        # print(type(link))
        n=1
        for item in link:
            print(item.get("href"),item.string,'链接计数',n,end='\n\n')
            if item.get('href').find("http")<0:
                url=start_urls+item.get('href')
            else :
                url=item.get('href')
            if n<5:
                yield scrapy.Request(url,self.parse_detail,encoding='utf-8')
            n=n+1
            if n>=1:
                break
    def parse_detail(self,response):
        response.body.decode("utf-8")
        res=BeautifulSoup(response.text,'lxml')
        zdmitem=SmzdmItem()
        for p in res.select('p'):
            if p.string!=None:
                zdmitem['message']='ahpu'+p.string
            else:
                zdmitem['message']=''
        zdmitem['title']=res.title.string+response.url
        print('这是爬虫爬取输出',zdmitem,end='\n\n')
        yield zdmitem