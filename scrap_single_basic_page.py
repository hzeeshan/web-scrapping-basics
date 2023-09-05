from bs4 import BeautifulSoup
import requests

website_link = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website_link)
content = result.text
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
box = soup.find("article", class_="main-article")
title = box.find('h1').get_text()
description = box.find('p', class_="plot").get_text()
transcript = box.find('div', class_="full-script").get_text(strip=True, separator=' ')
#print(transcript)
with open(f'{title}.txt','w') as file:
    file.write(transcript)


