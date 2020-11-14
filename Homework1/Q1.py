import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

key_words=urllib.parse.quote("금리")
url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2019.10.13&de=2019.10.14"
req = urllib.request.urlopen(url)
data = req.read()

soup = BeautifulSoup(data, 'html.parser')

anchor_set = soup.find_all("a")
news_link = []

main_articles = soup.select(".info")
sub_articles = soup.select(".sub_txt")
articles = main_articles + sub_articles

for article in articles:
    try:
        if article['href'].startswith("https://news.naver.com/main/read.nhn"):
            news_link.append(article['href'])
            print(article['href'])
    except Exception as e:
        #print(e)
        continue

print(len(news_link))   # 19