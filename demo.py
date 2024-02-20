import requests

url = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"

api_key = "0d82e3ab6627f982b4eac500e7f7bb83"

response = requests.get(url, params={"api_key": api_key, "query": "Matrix"})

print(response.json())

movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
# The language parameter is optional, if you were making the website for a different audience
# e.g. Hindi speakers then you might choose "hi-IN"
response = requests.get(movie_api_url, params={"api_key": api_key, "language": "en-US"})
data = response.json()