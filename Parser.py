from bs4 import BeautifulSoup
import requests

def parse():
    filteredModel = []
    filteredInfo = []
    filteredCost = []

    url = 'https://auto.drom.ru/'
    page = requests.get(url) 
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser") 
    model = soup.findAll('div', class_="css-l1wt7n e3f4v4l2") 
    info = soup.findAll('div', class_="css-1fe6w6s e162wx9x0") 
    cost = soup.findAll('div', class_="css-1dv8s3l eyvqki91") 

    for data in model:
        if data.find('span', {'data-ftid': 'bull_title'}):
            filteredModel.append(data.text)

    for data in info:
        if data.find('span', {'data-ftid': 'bull_description-item'}):
            filteredInfo.append(data.text)

    for data in cost:
        if data.find('span', {'data-ftid': 'bull_price'}):
            filteredCost.append(data.text)

    i = 0
    result_str = ''
    for data in filteredModel:
        result_str += filteredModel[i]
        result_str += filteredInfo[i]
        result_str += filteredCost[i]
        result_str += '\n'
        i += 1

    file = open("result.txt", "w", encoding="utf-8")
    file.write(result_str)
    file.close()

