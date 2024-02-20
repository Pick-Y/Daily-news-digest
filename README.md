# Daily-news-digest

This app sends information about a selected topic via email

## Generate API KEY for this project

Users can generate the relevant API KEY for this project by following the link below:

[a link](https://newsapi.org)

## Imports

Import the Python modules:

```bash
import requests
from sendmail import send_email
import smtplib,ssl
from email.message import EmailMessage
```

## Note on password setup

As Google does not allow less secure app access anymore, users can follow the lnk below to set up a specific password to be used to send emails:

[a link](https://youtu.be/g_j6ILT-X0k?t=25)
