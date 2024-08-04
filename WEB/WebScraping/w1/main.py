from bs4 import BeautifulSoup
#import lxml

PATH = "WEB/WebScraping/w1/website.html"
with open(PATH, "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.li.text)

all = soup.find_all(name="p")

for tag in all:
    # print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

comp_url = soup.select_one(selector="p a")
print(comp_url)


headings = soup.select(".heading")
print(headings)
