# function to pull the top BBC news headlines


import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://www.bbc.com/news",
)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find_all(class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
title.insert(0, soup.find(class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text"))
country = soup.find_all(class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state")
country = country[:17]
c = country.pop(0)


for t in title:
    if t.string == "BBC World News TV" or t.string == "BBC World Service Radio":
        # do nothing
        continue
    elif len(country) != 0:
        c = country.pop(0)
        print(t.string + " (" + c.string + ")") 
    else:
        print(t.string)

