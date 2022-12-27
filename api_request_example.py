import sys

import requests

url = 'http://127.0.0.1:8000/get_text'

filename = sys.argv[1]

post_files = {
    'img': open(f'data/{filename}', "rb"),
}
response = requests.request(method='POST', url=url, files=post_files)

print(response.text)
