import requests
from bs4 import BeautifulSoup

#html_doc = '<h1>Hello word</h1><h2 id="subtitle">Comment ca va?</h2><p class="font-arial">Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit, eius ab corrupti vitae maxime natus quasi sunt voluptates totam et optio suscipit impedit nisi nobis praesentium ut iure cupiditate itaque!</p>'

url = 'https://www.mihivai.com/'
html_doc = requests.get(url).content

soup = BeautifulSoup(html_doc, 'html.parser')

people = soup.find_all(class_="card-team-text")

team = []
for person in people:
    name = person.find("p", class_="card-team-title").text
    position = person.find(class_="card-subtitle").text
    member = {
        "name": name,
        "position": position
    }
    team.append(member)
    
print(team)
