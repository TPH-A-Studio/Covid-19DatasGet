# -*- coding:utf-8 -*-
import requests
from lxml import etree

gets = requests.get("http://bitpush.news/covid19/")
gets.encoding = "utf-8"
