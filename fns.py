import random
import uuid


def c_str_to_c_dict(s1: str, s2: str = '; ') -> dict:
    """
    args :
        s1 : a="123; b=456; c=789; d=asdf"
        s2 : ; 
    return
        dict : {'a':"123",'b':"456",'c':"789"}
    """
    # return {str(k): str(v) for k, v in (x.split('=') for x in s1.split('; '))}
    x = [x.split('=') for x in s1.split(s2)]
    r_dict = {}
    for i in x:
        r_dict[i[0]] = i[1]
    return r_dict


def get_ran_str(s_len: int, luan=False):
    """
    返回任意长度的随机字符串
    args:
        s_len: 随机字符串的长度
        luan: 乱数, 默认为False
    """
    s = 'abcdefghijklmnopqrstuvwxyz1234567890'
    if luan:
        s = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=1234567890'
    return ''.join(random.sample(s, s_len))


if __name__ == '__main__':
    # cookies_str = r"miid=654009097734832763; enc=lLsByDdi3HM70tGWrBHWe1R0nYvT4BajAo%2BGIE4xiHHSXIZwg0TdQtc3j23r3hiPN3QJggzeMrkNG0rnqWW6bw%3D%3D; t=36e976256c24fd7441213f8ae0814890; thw=cn; tfstk=cKFGBu2idRk_hHXEw1G1GZb_SVWRaj6ZfSPUTNjaZrDa9OVj8sAMLLJ8WwmOVGJf.; cna=MqT2GurRvGcCAbaUyIXcigtO; isg=BNjYdSGRDsByjSJE-giRFD4SqgZqwTxLcjTb2hLJq5ORrXqXutV227zP4WWdpvQj; l=eBPD6TJqLc7xjo7wBO5Crurza77OmIR4zkPzaNbMiInca6IVtpa-SNC3S7DWSdtfgtCeeetPhsKK4dhWPaUdg2HvCbKrCyClpY9O.; _m_h5_tk=d94fda89ff794bc500fea02340be733b_1652252613028; _m_h5_tk_enc=e1aec36d5c5fccfd39dc2ae9ea2cdc69; xlly_s=1; _samesite_flag_=true; cookie2=177b5913e7cd15ac68372f93743b85c9; _tb_token_=fbb6bede7b573; sgcookie=E100yhLWrdbZ5nkRKeBKUQvLrZkvsFsHmJKwMHRrSaEVKS6qoClEWtvfdUSli7daQHpu%2BFVof3J9TlHNNUqmlQxOubX9ffKC5tCIU0QkDsxdsu8%3D; unb=3455797095; uc1=existShop=true&pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=UoexMNbVysaDBA%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=V32FPkk%2Fgi8IDE%2FSq3xx; uc3=nk2=F6k3HSxlUOYM6gqnHoQSWuWbx%2BM%3D&id2=UNQyR5B2AuSyOg%3D%3D&vt3=F8dCvC6LC5RetW3cMSo%3D&lg2=UIHiLt3xD8xYTw%3D%3D; csg=acdbd34b; lgc=t_1508891678528_0604; cancelledSubSites=empty; cookie17=UNQyR5B2AuSyOg%3D%3D; dnk=t_1508891678528_0604; skt=75ec713b0e4a5924; existShop=MTY1MjI0MjY1Ng%3D%3D; uc4=id4=0%40UgP5HJslqKOI5tgjMOWzT0gd8WN1&nk4=0%40FbMocxnCtgNP73FV3v%2Bs3UGt8SEkB5K%2FU7CE8M2krw%3D%3D; tracknick=t_1508891678528_0604; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=454; _nk_=t_1508891678528_0604; cookie1=B0Fpc0Z28tOsKHTNUGJV0KQLUK%2BmZzOHCjFH%2F%2Bjd7gM%3D; JSESSIONID=FA43FA7BCF2765E8DE0B7F3168DE91EB"
    # cookies_str = r"BIDUPSID=568659A8CE5421C63024419FFF150B40; PSTM=1647093497; BD_UPN=12314753; BAIDUID=568659A8CE5421C63024419FFF150B40:SL=0:NR=10:FG=1; sug=3; sugstore=1; ORIGIN=0; bdime=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598"
    cookies_str = r"last-domain=www.ti.com.cn; _abck=9FED9FD8103C41E19F9130B936729DE7~-1~YAAQ1w7TF3biGz+BAQAA7Qw5UwhGBlfB4vQxrMZqIgqqGNEWAJYB2bpIuppvoP0BSKnGG8uND8CbfA3XYE7kqNVbvPp0MrcXgHw6hob7FO2je4j4QS5tLIyk3JFnC4V3uChbzYQ7BKgH4wEVYbGdHkUKPcg9JOddy5hrVcqByXDA7KgHiDyWSDdEoesqFIk2ZJkUWK5B6NT6/+G9ouQSBN23QUDbZ/Efkb0piDFpDIvdTiufp3zvosh37llKKFnPx5ekhAlhRRviicKdKX9RCQvuNbBtc3IhAMshuChf1zeYipzhSNY8sD1RikyHnqhrgffK6cMoSHwKF70nQOrANVG78dXpVrm4wAWEx9813Ld7tkB6i5a4AyIWCRNRemCuj+d3T6lIPgUNLpC4AUjvaUHV/YzqtJKefZ6oHcnnTWKw8kYxVt6rsOGa2AH…Ce4n7wXMQt5Nu5bGP38+5nZwt9PW7PlkBKetuClxNlVKcCmJ9KGmpV128kKO08iWCt8vpxfbCzOQHMhGPd7zUs5gh6WqexiDbpyJNK6m5hjMgIaiNsjki+dFHvE3/aApY3BJtQuMLv7/GjB456kz/82hxtvuG2Sm14aX42jHPTVt2+COzXCtzXuZImhtSDlnh9aAUhoQBrTbhn3y5u0WOlH0ODWfrd8fv/ri0vSJsuH1fCSOSanlsf2DtNe+wZEuoDlg==~1; ti_geo=country=JP|city=TOKYO|continent=AS|tc_ip=50.7.14.76; ti_rid=34309cdc; ti_ua=Mozilla%2f5.0%20(Windows%20NT%2010.0%3b%20Win64%3b%20x64%3b%20rv%3a101.0)%20Gecko%2f20100101%20Firefox%2f101.0; ti_bm=; pf-accept-language=zh-CN; chipset=10493939"
    print(c_str_to_c_dict(cookies_str, '; '))
