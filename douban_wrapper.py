#!/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, json
from config import DOUBAN_APIKEY

# 访问豆瓣API获取书籍数据
BOOK_URL_BASE = 'http://api.douban.com/v2/book/search'

# 访问豆瓣API获取电影数据
FILM_URL_BASE = 'http://api.douban.com/v2/movie/search'

# 访问豆瓣API获取音乐数据
MUSIC_URL_BASE = 'http://api.douban.com/v2/music/search'

# 通过豆瓣API获取书籍数据，然后把数据格式化成特定的格式：
# [{"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"}]
def search_book(q):
    params = {'q': q, 'apikey': DOUBAN_APIKEY, 'count': 3}
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


# 通过豆瓣API获取电影数据，然后把数据格式化成特定的格式：
# [{"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"}]
def search_film(q):
    params = {'q': q, 'apikey': DOUBAN_APIKEY, 'count': 3}
    url = FILM_URL_BASE + '?' + urllib.urlencode(params)
    resp = urllib2.urlopen(url)
    r = json.loads(resp.read())
    films = r['subjects']

    filmList = []
    for i, film in enumerate(films):
        item = {}
        title = u'%s\t%s分\n%s年\n%s' % (
            film['title'], film['rating']['average'], film['year'], ','.join(film['genres']))
        description = ''
        picUrl = film['images']['large'] if i == 1 else film['images']['small']
        url = film['alt']
        item['title'] = title
        item['description'] = description
        item['image'] = picUrl
        item['url'] = url
        filmList.append(item)

    return filmList


# 通过豆瓣API获取音乐数据，然后把数据格式化成特定的格式：
# [{"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"},
# {"title":"失控", "description":"", "image":"http://xxx", "url":"http://xxx"}]
def search_music(q):
    params = {'q': q, 'apikey': DOUBAN_APIKEY, 'count': 3}
    url = MUSIC_URL_BASE + '?' + urllib.urlencode(params)
    # raise Exception(url, url)
    resp = urllib2.urlopen(url)
    r = json.loads(resp.read())
    musics = r['musics']

    musicList = []
    for i, music in enumerate(musics):
        print music
        item = {}
        title = u'%s\t%s分\n%s\n%s\t%s' % (
            music['title'], music['rating']['average'], ','.join(music['attrs']['singer']),
            ','.join(music['attrs']['publisher']),
            ','.join(music['attrs']['pubdate']))
        description = ''
        picUrl = music['image']
        url = music['alt']
        item['title'] = title
        item['description'] = description
        item['image'] = picUrl
        item['url'] = url
        musicList.append(item)

    return musicList