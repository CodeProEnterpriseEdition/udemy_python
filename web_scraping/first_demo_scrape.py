# https://www.rithmschool.com/blog
import csv
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        a_tag = article.find("a")
        # title = article.find("a").get_text()
        title = a_tag.get_text()
        date = article.find("time")["datetime"]
        # href = article.find("a")["href"]
        href = a_tag["href"]
        print(title)
        print(date)
        print(href)
        print("--------")
        csv_writer.writerow([title, date, href])
