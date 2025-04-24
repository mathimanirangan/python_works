from http import HTTPStatus

import requests

response=requests.get("https://google.com")

if response.status_code == HTTPStatus.OK:
    print("Everything is fine.")
