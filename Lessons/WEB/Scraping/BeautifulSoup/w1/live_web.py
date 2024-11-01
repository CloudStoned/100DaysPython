from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_spans = soup.find_all("span", class_="titleline")

article_texts = []
article_links = []

for article_span in article_spans:
    article_tag = article_span.find("a")
    article_text = article_tag.getText()
    article_texts.append(article_text)
    
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_upvote = max(article_upvotes)
highest_upvote_index = article_upvotes.index(highest_upvote)

print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
print(highest_upvote)
