import os
import requests
import re
import yaml
import json
import time
import random
from parsel import Selector
from addict import Dict

# Host 应该被覆盖
ua = Dict({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'})
headers = Dict({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
           'Host': 'pscly.cn', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1'})
headers.update(ua)


def is_file(path):
    return os.path.isfile(path)


def load_config_yaml(path='config/config.yaml', mode='WAI', err=True):
    if not is_file(path):
        if err:
            raise Exception(f'{path}文件不存在')
        return {}
    return yaml.safe_load(open(path, 'r'))[mode]


def load_json(path='config/config.json'):
    if is_file(path):
        raise Exception(f'{path}文件不存在')
    return json.load(open(path, 'r'))


class MyRes():
    '''
    封装一个获取结果的类
    仔细想想， 可以把cookies保存到一个对象中，到时候获取和调用都很方便了
    '''

    def __init__(self, config: dict={}, headers={}, cookies={}, coding='utf-8', dailis:list=[]) -> None:
        """ 
        args:
            dailis: 代理列表，格式为['http://ip:port', 'http://ip:port']
        """ 
        self.config = config
        self.headers = headers
        self.cookies = cookies
        self.coding = coding
        self.url = ''
        self.proxies = {}
        self.dailis = dailis
        if dailis:
            self.daili1 = self.get_one_daili()
            self.proxies = {'http': self.daili1, 'https': self.daili1}

    def get_one_daili(self):
        if self.proxies:
            return self.proxies
        return random.choice(self.dailis)
    
    def get(self, url, re_text=None, params={}, **kwargs):
        '''
        封装requests.get方法
        args:
            url: 访问地址
            re_text: 可选，提供正则，自动匹配
            headers: 可选，自己提供一个headers

        return: res1, re后的东西
        返回res1，想要什么就拿什么
        '''
        if self.config.get('Gen_url') and self.config.get('Gen_url') not in url:
            url = self.config.get('Gen_url') + url
        if self.proxies:
            res1 = requests.get(url, cookies=self.cookies,
                                params=params, headers=self.headers, proxies=self.proxies,  **kwargs)
        else:
            res1 = requests.get(url, cookies=self.cookies,
                                params=params, headers=self.headers,  **kwargs)

        res1.encoding = self.coding
        self.cookies.update(res1.cookies.get_dict())
        self.url = url
        self.headers = res1.headers
        self.headers['Referer'] = url
        self.text = res1.text
        self.res1 = res1
        if re_text:
            re_hou = re.findall(re_text, res1.text)
            return res1, re_hou
        return res1, None

    def post(self, url, data, re_text=None, **kwargs):
        '''
        封装requests.post方法
        '''
        if self.config.get('Gen_url') and self.config.get('Gen_url') not in url:
            url = self.config.get('Gen_url') + url
        if self.proxies:
            res1 = requests.post(
                url, data=data, cookies=self.cookies, headers=self.headers, proxies=self.proxies,  **kwargs)  # 这里加上header就有问题
        else:
            res1 = requests.post(
                url, data=data, cookies=self.cookies, headers=self.headers,  **kwargs)
        res1.url = self.url
        res1.encoding = self.coding
        self.cookies.update(res1.cookies.get_dict())
        self.headers = res1.headers
        self.headers['Referer'] = url
        self.res1 = res1
        self.text = res1.text
        if re_text:
            re_hou = re.findall(re_text, res1.text)
            return res1, re_hou
        return res1, None


def get_files(path):
    """
    将目录下的所有非y_的文件名，返回一个列表，通过文件的创建时间排序
    """
    if not os.path.isdir(path):
        os.system(f"mkdir -p {path}")
    files_path = os.listdir(path)
    files = [file for file in files_path if not file.startswith('y_')]
    files_dates = [os.path.getmtime(os.path.join(path, file))
                   for file in files]
    t_files = list(
        zip(
            [time.strftime("%Y-%m-%d %X", time.localtime(files_date))
             for files_date in files_dates],
            files,
            files_dates,
        )
    )
    t_files.sort(key=lambda x: x[2], reverse=True)
    return t_files


if __name__ == '__main__':

    r = MyRes(dailis=['http://112.25.236.167:9091'])
    # r = MyRes(dailis=['http://127.0.0.1:21080'])
    # 查询 ip
    # r.proxies = {'http': 'http://127.0.0.1:21080'}
    z = r.get('http://httpbin.org/ip')
    # z = r.get('http://httpbin.org/ip',
    #           proxies={'http': 'http://127.0.0.1:21080'})
    print(z[0].text)
