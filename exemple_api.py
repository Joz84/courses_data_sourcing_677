# VERB            Action        ex url               Description
# GET         =>  Read all   => /restaurants      => all restos
# GET         =>  Read       => /restaurant/:id   => One resto
# POST        =>  Create     => /restaurants      => Create one resto (body)
# PATCH/PUT   =>  Update     => /restaurant/:id   => Update one resto (body)
# DELETE      =>  Delete     => /restaurant/:id   => Delete one resto

import requests

url = 'https://api.github.com/users/FuriousHarry'
response = requests.get(url).json()

print(response["avatar_url"])

# https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data
url = 'https://openlibrary.org/api/books?'

params = {
    "bibkeys": "ISBN:9780571191536",
    "format": "json",
    "jscmd": "data"
}

r = requests.get(url, params=params).json()

print(r["ISBN:9780571191536"]["title"])
