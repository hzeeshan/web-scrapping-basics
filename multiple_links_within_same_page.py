from bs4 import BeautifulSoup
import requests

root_url = 'https://subslikescript.com'
website_link = f"{root_url}/movies"
result = requests.get(website_link)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

box = soup.find('article', class_='main-article')
link_elements = box.find_all('ul', class_='scripts-list')
links = [a['href'] for ul in link_elements for a in ul.find_all('a')]
for link in links:

    movie_link = f"{root_url}/{link}"
    result = requests.get(movie_link)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    movie_details_page_box = soup.find('article', class_="main-article")
    title = movie_details_page_box.find('h1').get_text()
    details = movie_details_page_box.find('div', class_="full-script").get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w') as file:
        file.write(details)

print('success')



