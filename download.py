import urllib.request
import json
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
]

h = {
    'Host': 'www.hzcourse.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://ebooks.cmanuf.com/detail?id=10755',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=293A59750C3B7B24B80FB92980C9C1D4'
}
h2 = {
    'Host': 'www.hzcourse.com',
    'Connection': 'keep-alive',
    'Content-Length': 52,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.hzcourse.com',
    'Referer': 'http://www.hzcourse.com/web/refbook/probationAll/6587/5fd81ea856db4d8abb503c9429b49f07',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=293A59750C3B7B24B80FB92980C9C1D4'
}

proxy = {'http': str(json.loads(urllib.request.urlopen('http://localhost:5010/get/').read().decode('utf-8'))['proxy'])}


def _main_():
    opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))
    # 华章书籍目录存放文件
    hz = open("HuazhangList.txt", "w", encoding='utf-8')
    # 华章书籍机工图书馆数据
    with open("AChuazhang", "r", encoding='utf-8') as f:
        for i in f:
            print("-----------------------------------")
            print(json.loads(i)['name'])
            _id = json.loads(i)['id']
            # 拼机工的地址
            _url = 'http://ebooks.cmanuf.com/detail?id={0}'.format(_id)
            x = BeautifulSoup(urllib.request.urlopen(_url).read().decode('utf-8'), 'html.parser').find(
                attrs={'target': '_blank'})
            _url = 'http://ebooks.cmanuf.com' + x['href']
            req = urllib.request.Request(url=_url, headers=h)
            # 自动换代理，
            is_loop = True
            while is_loop:
                try:
                    response = opener.open(req)  # 通过代理访问地址
                    html = response.read().decode('utf-8')
                    soup = BeautifulSoup(html, 'html.parser')
                    ebookId = soup.find(id='ebookId')['value']
                    is_loop = False
                    print("解析成功.")
                except Exception as e:  # 偷懒，直接用异常来测是不是到访问上限
                    is_loop = True
                    print(e, end=". ")
                    print("更换代理.")
                    proxy['http'] = str(
                        json.loads(
                            urllib.request.urlopen('http://localhost:5010/get/').read().decode('utf-8')
                        )['proxy']  # 更换代理
                    )
                    opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))
            # response = urllib.request.urlopen(req)
            # html = response.read().decode('utf-8')
            # soup = BeautifulSoup(html, 'html.parser')
            # ebookId = soup.find(id='ebookId')['value']
            # 不用代理的话把64到82行、48行删掉就行。
            print("解析成功.")

            token = soup.find(id='token')['value']


            params = bytes('ebookId={0}&token={1}'.format(str(ebookId), str(token)), encoding='utf-8')
            h2['Content-Length'] = len(params)
            req = urllib.request.Request(url='http://www.hzcourse.com/web/refbook/queryAllChapterList', headers=h2,
                                         data=params, method="POST")
            response = urllib.request.urlopen(req)
            html = response.read().decode('utf-8')  # 目录的json数据
            print(html)
            hz.write(html + '\n')


_main_()
