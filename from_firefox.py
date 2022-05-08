"""此文件能将firefox处复制过来的headers 转换为requests可以使用的headers
"""
x = {
    "headers": [
        {
            "name": "Accept",
            "value": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        },
        {
            "name": "Accept-Encoding",
            "value": "gzip, deflate"
        },
        {
            "name": "Accept-Language",
            "value": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
        },
        {
            "name": "Cache-Control",
            "value": "no-cache"
        },
        {
            "name": "Connection",
            "value": "keep-alive"
        },
        {
            "name": "Host",
            "value": "pscly.cn:31002"
        },
        {
            "name": "Pragma",
            "value": "no-cache"
        },
        {
            "name": "Upgrade-Insecure-Requests",
            "value": "1"
        },
        {
            "name": "User-Agent",
            "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        }
    ]
}

x2 = {}

for i in x['headers']:
    x2[i['name']] = i['value']
print(x2)
