from bs4 import BeautifulSoup
from urllib import request
import re


class name(object):
    pass


def get_link(LinkUrl):
    LinkList = []
    # LinkUrl = 'http://www.biqukan.com/0_178/'
    req = request.Request(LinkUrl)
    req.add_header(
        'User-Agent',
        'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    )
    try:
        response = request.urlopen(req)
    except Exception as e:
        print('该网址：' + LinkUrl + '可能不正确。请重新确认。')
    html = response.read().decode('gbk', 'ignore')
    soup = BeautifulSoup(html, 'lxml')
    LinkTag = soup.find('div', class_='listmain')
    NovelNameFatherTag = soup.find('div', class_='info')
    NovelName = NovelNameFatherTag.h2.string
    # print(NovelName)
    init(NovelName)
    begin_flag = False
    for child in LinkTag.dl.children:
        if child != '\n':
            if '正文卷' in child.string:
                begin_flag = True
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                # download_name = child.string
                LinkList.append(download_url)
                # print(download_name + " : " + download_url)
    return LinkList


def init(NovelName):
    name.per = NovelName + '.txt'
    print(name.per)
    with open(name.per, 'w', encoding='utf-8') as f:
        f.write('')


# for i in get_link():
#     # print(i)
#     pass
