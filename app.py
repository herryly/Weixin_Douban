#!/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, abort
from config import APP_SECRET_KEY
from lib.wechatpy import parse_message, create_reply
from lib.wechatpy.utils import check_signature
from lib.wechatpy.exceptions import InvalidSignatureException
import douban_wrapper

app = Flask(__name__)
app.debug = True
app.secret_key = APP_SECRET_KEY

TOKEN = 'douban_book'  # 注意要与微信公众帐号平台上填写一致


@app.route('/')
def home():
    return render_template('index.html')


# 公众号消息服务器网址接入验证
#需要在公众帐号管理台手动提交, 验证后方可接收微信服务器的消息推送
@app.route('/weixin', methods=['GET', 'POST'])
def weixin():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echo_str = request.args.get('echostr', '')
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)
    if request.method == 'GET':
        return echo_str
    else:
        msg = parse_message(request.data)
        if msg.type == 'text':
            #reply = create_reply(douban_book.search_book(msg.content), msg)
            reply = getSeachResult(msg)
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return reply.render()

def getSeachResult(msg) :
    q = msg.content.encode('utf-8')
    if q.startswith('film:') :
        q = q.replace('film:', '')
        reply = create_reply(douban_wrapper.search_film(q), msg)
    elif q.startswith('book:') :
        q = q.replace('book:', '')
        reply = create_reply(douban_wrapper.search_book(q), msg)
    else :
        reply = create_reply(douban_wrapper.search_book(q), msg)

    return reply

if __name__ == '__main__':
    app.run()
