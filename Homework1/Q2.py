import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

key_words=urllib.parse.quote("금리")

total_num = 1221
pages = []

for val in range(int(total_num//10)):
    start_val=str(val)+"1"
    pages.append(start_val)
    # print(start_val)

# 전체 페이지의 기사 크롤링
news_link = []
for page in pages:
    url = "https://search.naver.com/search.naver?where=news&query=" + \
          key_words + \
          "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2019.10.13&de=2019.10.14&docid=&nso=so:r,p:from20191013to20191014,a:all&mynews=0&cluster_rank=26&start=" + \
          page + "&refresh_start=0"

    req = urllib.request.urlopen(url)
    data = req.read()

    soup = BeautifulSoup(data, 'html.parser')

    anchor_set = soup.find_all("a")

    main_articles = soup.select(".info")
    sub_articles = soup.select(".sub_txt")
    articles = main_articles + sub_articles

    for article in articles:
        try:
            if article['href'].startswith("https://news.naver.com/main/read.nhn"):
                news_link.append(article['href'])
                print(article['href'])
        except Exception as e:
            # print(e)
            continue

# 중복 제거
news_set = set(news_link)
news_link = list(news_set)

# print(len(news_link))   # 402