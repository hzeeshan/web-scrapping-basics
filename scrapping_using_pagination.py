from bs4 import BeautifulSoup
import requests

result = requests.get('https://subslikescript.com/movies')
content = result.text
soup = BeautifulSoup(content, 'html.parser')
#pagination
pagination_container = soup.find('ul', class_="pagination")
pages = pagination_container.find_all('li', class_="page-item")
last_page = pages[-2].text
#print(last_page)
for page in range(1, 2):
    website = f"https://subslikescript.com/movies?page={page}"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    box = soup.find('article', class_='main-article')
    link_elements = box.find_all('ul', class_='scripts-list')
    links = [a['href'] for ul in link_elements for a in ul.find_all('a')]
    for link in links:
        try:
            result = requests.get(f'https://subslikescript.com/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'html.parser')
            movie_details_page_box = soup.find('article', class_="main-article")
            title = movie_details_page_box.find('h1').get_text()
            details = movie_details_page_box.find('div', class_="full-script").get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w') as file:
                file.write(details)
        except:
            print('som error ...')
            pass

print('success')