import requests
import smtplib,ssl
from sendmail import send_email

api_key ="YOUR API KEY"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-20&sortBy=publishedAt&apiKey="+ api_key

request = requests.get(url)

content = request.json()

body =""

for article in content["articles"]:

    body =f"{body}{article['title']}\n{article['description']}\n\n"
    
send_email(body)