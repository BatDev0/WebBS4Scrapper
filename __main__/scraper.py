from bs4 import BeautifulSoup
import requests
#
page_link = 'https://testlink.com/test.html'

page_response = requests.get(page_link, timeout=5)
#
page_content = BeautifulSoup(page_response.content, "html.parser")

for i in range(50):
    var = page_content.find_all(class_="class")[i].text
    print(var)
    var2 = page_content.find_all(class_="class2")[i].text
    print(var2)


for i in range(50):
     f = open("scrapes.txt", "a+")
     money = page_content.find_all(class_="money")[i].text
     title = page_content.find_all(class_="product-title")[i].text
     f.write(money)
     f.write(title)
     f.close()