import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210808}"

page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")

links = soup.find_all("a")


