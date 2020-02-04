# -*- coding:utf-8 -*-
import random
import time
import urllib.request

from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
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


def _print(x):
    print(x)


def get_response(url, proxy={}, header={}, params=None, method=None):
    if not params:
        header['Content-Length'] = len(params)
    if not proxy:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))
        response = opener.open(urllib.request.Request(url=url, headers=header, data=params, method=method))
        return response

    response = urllib.request.urlopen(urllib.request.Request(url=url, headers=header, data=params, method=method))
    return response


def post(data):
    params = bytes(data, encoding='utf-8')
    req = urllib.request.Request(url='http://198.13.46.231:18899/senddata',
                                 headers={'Content-Length': len(params)}, data=params, method="POST")
    flag = True
    while flag:
        try:
            _print("尝试提交任务.")
            response = urllib.request.urlopen(req)
            flag = False
        except Exception as e:
            _print("任务提交失败.")
            _print(str(e))
            time.sleep(random.choice(range(1, 4)))
            break
    _print("任务提交成功.")


def get():
    flag = True
    while flag:
        try:
            _print("尝试领取任务")
            response = urllib.request.urlopen('http://198.13.46.231:18900/gettask')
        except Exception as e:
            flag = False
            _print("任务领取失败.")
            _print(str(e))
            time.sleep(1)
            break
    print("任务领取成功. ")
    return str(response.read().decode("utf-8")).split(' ')


def auto_proxy():
    return {}


def download():
    flag = False
    while not flag:
        access_err = False  # 访问错误，说明到访问上限了
        for _id in get():
            http_err = False  # HTTP错误，一般是网页请求错误
            if not _id:
                continue

            if 'clear' in _id:
                _print("任务队列空.")
                flag = True
                break

            response = str(_id)
            if not access_err:
                soup = BeautifulSoup(  # 从机工获取跳转url
                    get_response(url='http://ebooks.cmanuf.com/detail?id={0}'.format(_id)).read().decode('utf-8'),
                    'html.parser').find(attrs={'target': '_blank'})
                for x in range(5):  # 5次错误后把id返回服务器
                    try:
                        soup = BeautifulSoup(  # 从跳转url跳转到华章并取参数
                            get_response(url=('http://ebooks.cmanuf.com' + soup['href']), header=h,
                                         proxy=auto_proxy()).read().decode('utf-8'),
                            'html.parser')
                        http_err = True
                        break
                    except Exception as e:
                        http_err = False
                        _print("网页访问错误。")
                        _print(e)
                        time.sleep(1)
                if not http_err:
                    try:
                        ebookId = soup.find(id='ebookId')['value']
                        _print("解析成功.")
                    except Exception as e:
                        access_err = True
                        _print(e)
                        _print("达到访问上限.")
                        post(response)
                        continue
                    token = soup.find(id='token')['value']

                    try:
                        response = get_response(url="http://www.hzcourse.com/web/refbook/queryAllChapterList",
                                                params=bytes('ebookId={0}&token={1}'.format(str(ebookId), str(token)),
                                                             encoding='utf-8'), header=h2, method="POST").read().decode(
                            'utf-8')
                    except Exception as e:
                        _print(e)
                        _print("目录获取失败.")
            post(response)
    _print("任务全部完成.")
