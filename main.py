import requests

api_key ="21fec9ba90cb46e9a18d28867becd322"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-20&sortBy=publishedAt&apiKey=21fec9ba90cb46e9a18d28867becd322" 

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["author"])