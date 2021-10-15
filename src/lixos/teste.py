from urllib.parse import urljoin
import requests
from src.config.conf import base_url

data = requests.get(urljoin(base_url, '1'))
res = data.json()
print(data.json())
print(res['Modulos'][0]['name'], res['Modulos'][0]['version'],res['Modulos'][0]['url'], res['Modulos'][0]['isActive'])