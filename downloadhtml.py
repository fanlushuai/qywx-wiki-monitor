# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup


def getFileNmae(htmlAddr):
    filename = os.getcwd() + '\\wiki\\' + htmlAddr + ".html"
    return filename


def downhtml(htmlAddr):
    r = requests.get('http://qydev.weixin.qq.com/wiki/index.php', params={'title': htmlAddr})
    print type(r)
    print r.status_code
    print r.encoding
    filename = getFileNmae(htmlAddr.replace('/', '').replace('\\', ''))
    print  filename
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(2000):
            fd.write(chunk)


def getMenus():
    htmlAddr = '首页'
    downhtml(htmlAddr)
    filename = getFileNmae(htmlAddr)
    soup = BeautifulSoup(open(filename))
    menus = []
    for menu in soup.find_all(id="p-.24name-label"):
        print(menu.text.strip())
        menus.append(menu.text.strip())

    for menu in soup.select('li > a[href*="/wiki/index.php"]'):
        print(menu.text.strip())
        menus.append(menu.text.strip())

    return menus


def downloadWiki():
    menus = getMenus()
    for menu in menus:
        # if menu.find("2016") == -1:
        downhtml(menu)
        print menu + 'ok'


if __name__ == "__main__":
    getMenus()
    # downloadWiki()
