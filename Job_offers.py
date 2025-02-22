import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


url = "https://www.aplikuj.pl/praca/wroclaw?distance=0"

#driver = webdriver.Edge()
#driver.get(url)

html_txt = requests.get(url).text
soup = BeautifulSoup(html_txt, 'lxml')

obszar = soup.find_all("li", class_= "result-facets__item")

def kategorie():
    linki = []
    for kategoria in obszar:

        tytuły2 = kategoria.find("span", class_="flex-initial text-ellipsis lg:overflow-hidden lg:max-h-4").text
        link = kategoria.find("a").get('href')
        link = "https://www.aplikuj.pl" + link
        print(tytuły2)
        linki.append(link)
    return linki
    
def oferty_lista():
     oferty = kategorie()
     for oferta in oferty:
        txt = requests.get(oferta).text
        soup2 = BeautifulSoup(txt,'lxml')
        x = soup2.find_all("div", class_='offer-card-main')
        for i in x: 
            y = i.find('a', class_='offer-title').get('title')
            print(y)
        print('\n', 8*'*', '\n')

oferty_lista()




