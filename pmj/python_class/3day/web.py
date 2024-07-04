import os
import requests
from bs4 import BeautifulSoup

url = "https://school.busanedu.net/buil-h/main.do"
response = requests.get(url)

page_content = response.content
soup = BeautifulSoup(page_content,"html.parser")

qoutes = soup.find_all('dd',class_='meal_list')

for q in qoutes :
    print(q.getText())

os.system("pause")


