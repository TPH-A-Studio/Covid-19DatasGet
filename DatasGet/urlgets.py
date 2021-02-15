# -*- coding:utf-8 -*-
# @Time:     2021/2/12 22:54
# @Author:   Top Programmer - Hacker(Administrator)
# @Software: PyCharm
import requests
from lxml import etree
import my_fake_useragent as mfu

headers = {
    "Referer": "http://bitpush.news/covid19/",
    "User-Agent": mfu.UserAgent().random()
}

gets = requests.get("http://bitpush.news/covid19/", headers=headers).text


def x_paths(ps):
    html = etree.HTML(gets)
    return html.xpath(ps)
