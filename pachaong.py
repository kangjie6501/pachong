import urllib.request
from bs4 import BeautifulSoup
import re

def get_sub_url(super_url):
    response = urllib.request.urlopen(super_url)
    html = response.read()
    html = html.decode("gbk") # 解码操作
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all("a", text=re.compile("第"))

def delete_news(times, links):
    for index in range(0, times + 1): del links[0]
    return links

def get_sub_content(detail_url):
    response = urllib.request.urlopen(detail_url)
    html = response.read()
    html = html.decode("gbk") # 解码操作
    bsObj = BeautifulSoup(html, "lxml").find(id="content")
    content = re.compile(r"(.*)").search(str(bsObj)) # 把章节内容提取出来
    content = re.compile("").sub("\n", str(bsObj)) # 把网页的替换成换行
    content = re.compile('').sub("", str(content)) # 把网页的替换成换行
    content = re.compile("'" + detail_url + "'").sub("", str(content))
    content = re.compile(detail_url).sub("", str(content))
    content = re.compile('请记住本书首发域名：www.biqukan.com。笔趣阁手机版阅读网址：m.biqukan.com').sub("", str(content))
    return str(content)
def write_txt( title_name, content):
    print(title_name)
    print("开始制作txt文档" + title_name)
    f = open(book_name + ".txt", "a", encoding="utf-8")
    title = "\n\n" + " " * 20 + title_name + "\n"
    f.write(title)
    f.write(content)
    f.close()
def write_boon_name(book_name):
    f = open(book_name + ".txt", "w", encoding="utf-8")
    f.write(" " * 20 + book_name + "\n")
    f.close()

def get_content(super_url, links):
    for link in links:
        detail_url = super_url + link.get('href')
        sub_content = get_sub_content(detail_url)
        write_txt(link.get_text(),sub_content)

if __name__ == 'main':
    home_url = "http://www.biqukan.com"
    book = "/1_1094"
    super_url = home_url + book
    book_name = "一念永恒"
    write_boon_name(book_name)
    links = get_sub_url(super_url)
    new_links = delete_news(12, links)
    get_content(home_url,new_links) # http://www.biqukan.com/1_1094/17013603.html