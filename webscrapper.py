import requests
from bs4 import BeautifulSoup

url = "https://www.eatthismuch.com/food/browse/?type=recipe"
body = requests.get(url)
body_text = body.content

soup = BeautifulSoup(body_text, 'html.parser')

divs = soup.find_all("div", class_="col-11")



print(divs)




# import requests
# from bs4 import BeautifulSoup
# from inflection import titleize

# def title_generator(links):
#     titles = []

#     def post_formatter(url):
#         if 'posts' in url:
#             url = url.split('/')[-1]
#             url = url.replace('-', ' ')
#             url = titleize(url)
#             titles.append(url)

#     for link in links:
#         if link.get('href') == None:
#             continue
#         else:
#             post_formatter(link.get("href"))

#     return titles


# r = requests.get('https://www.eatthismuch.com/food/browse/?type=recipe')
# soup = BeautifulSoup(r.text, 'html.parser')
# links = soup.find_all('a')
# titles = title_generator(links)

# for title in titles:
#     print(title)