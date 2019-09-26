# https://www.seleniumhq.org/docs/

from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome('/ai/pythonP/selenium/chromedriver')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(4)
# element1 = driver.find_element_by_id('quickSearchText')
# element1.send_keys('제주시')
loca = driver.find_element_by_css_selector('.loca_search a')     # loca = driver.find_element_by_class_name('loca_search') 
loca.send_keys('\n')    # loca.click()
time.sleep(4)
sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].send_keys('\n')


# driver = webdriver.Chrome('/ai/pythonP/selenium/chromedriver')
driver.get('https://www.google.com/maps/?hl=ko')
time.sleep(3)
element2 = driver.find_element_by_id('searchboxinput')
element2.send_keys('카카오')
element3 = driver.find_element_by_id('searchbox-searchbutton')
element3.click()
time.sleep(3)
page = driver.page_source
bs = BeautifulSoup(page, 'html.parser')
itemTitle = bs.select('h3.section-result-title span')
itemLoca = bs.select('span.section-result-location')
print(itemTitle[0].string)
print(itemLoca[0].string)