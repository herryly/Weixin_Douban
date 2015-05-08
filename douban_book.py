#!/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, json
from config import DOUBAN_APIKEY

# 访问豆瓣API获取书籍数据
BOOK_URL_BASE = 'http://api.douban.com/v2/book/search'


# 通过豆瓣API获取书籍数据，然后把数据格式化成特定的格式：
# [{"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"}]
def search_book(q):
    params = {'q': q.encode('utf-8'), 'apikey': DOUBAN_APIKEY, 'count': 3}
    url = BOOK_URL_BASE + '?' + urllib.urlencode(params)
    resp = urllib2.urlopen(url)
    r = json.loads(resp.read())
    books = r['books']

    bookList = []
    for i, book in enumerate(books):
        item = {}
        title = u'%s\t%s分\n%s\n%s\t%s' % (
        book['title'], book['rating']['average'], ','.join(book['author']), book['publisher'], book['price'])
        description = ''
        picUrl = book['images']['large'] if i == 1 else book['images']['small']
        url = book['alt']
        item['title'] = title
        item['description'] = description
        item['image'] = picUrl
        item['url'] = url
        bookList.append(item)

    return bookList