# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 12:00:39 2022

@author: Dipen
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
import pandas as pd



ttypes = ['tspirits','tbeer','tcider','tpremixed']


data = []

#page = requests.get('https://www.boozebud.com/browse-products?filtercontext=ttype&ttype=tspirits')
options = Options()
driver = webdriver.Chrome('C:\\Users\\Dipen\\webdriver\chromedriver.exe',options=options)
driver.get('https://www.boozebud.com/browse-products?filtercontext=ttype&ttype=tspirits')
time.sleep(2)
#driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="bb-content"]/div[2]/div[3]/div/div/div[1]/div/div[2]')))) 


boozebud_spirits = pd.DataFrame()

def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

scroll_to_bottom(driver)
#Product=driver.find_elements_by_xpath('//*[@id="bb-content"]/div[2]/div[3]/div/div')
Product = driver.find_elements_by_class_name('bb-grid--tile')
url=[]
name=[]
bottle_price=[]
case_price=[]
for i in Product:
    soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
    for a in soup.find_all("a"):
        print('https://www.boozebud.com' + a['href'])
        url.append('https://www.boozebud.com' + a['href'])
    #products = 
    for products in soup.find_all("div", class_="bb-product-tile--name"):
        print(products.text)
        name.append(products.text)
    bprice = soup.find_all("div", class_="bb-variant--to")
    bprice = bprice[:1]
    for i in bprice:
        print(i.text)
        bottle_price.append(i.text)
    cprice = soup.find_all("div", class_="bb-variant--to")
    if len(cprice) == 2:
        cprice = cprice[1:2]
        for i in cprice:
            print(i.text)
            case_price.append(i.text)
    else:
            case_price.append('0')

boozebud_spirits['url'] = url
boozebud_spirits['case_price'] = case_price
boozebud_spirits = boozebud_spirits.iloc[36:]
boozebud_spirits['name'] = name
boozebud_spirits['bottle_price'] = bottle_price

#---------------------------------------------------
driver.get('https://www.boozebud.com/browse-products?filtercontext=ttype&ttype=tbeer')
time.sleep(2)

boozebud_beers = pd.DataFrame()
scroll_to_bottom(driver)

#Product=driver.find_elements_by_xpath('//*[@id="bb-content"]/div[2]/div[3]/div/div')
Product = driver.find_elements_by_class_name('bb-grid--tile')
url=[]
name=[]
bottle_price=[]
case_price=[]
can_price=[]
for i in Product:
    soup = BeautifulSoup(i.get_attribute('innerHTML'),'html.parser')
    for a in soup.find_all("a"):
        print('https://www.boozebud.com' + a['href'])
        url.append('https://www.boozebud.com' + a['href'])
    #products = 
    for products in soup.find_all("div", class_="bb-product-tile--name"):
        print(products.text)
        name.append(products.text)
    bprice = soup.find_all("div", class_="bb-variant--to")
    bprice = bprice[1:2]
    for i in bprice:
        print(i.text)
        bottle_price.append(i.text)
    cprice = soup.find_all("div", class_="bb-variant--to")
    if len(cprice) == 3:
        cprice = cprice[2:3]
        caprice = cprice[:1]
        for i in cprice:
            print(i.text)
            case_price.append(i.text)
    else:
            case_price.append('0')
            caprice.append('0')

boozebud_beers['url'] = url
boozebud_beers['case_price'] = case_price
boozebud_beers = boozebud_beers.iloc[36:]
boozebud_beers['name'] = name
boozebud_beers['pack_price'] = bottle_price
boozebud_beers['can_price'] = caprice

#----------------------------------------------------------------


    


