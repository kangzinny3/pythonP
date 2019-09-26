from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('/ai/pythonP/selenium/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login') 
driver.implicitly_wait(3)    # time.sleep(3)이랑 같은 기능

userid = 'kangzinny3'
pw = 'wldmsdl1219!'

# driver.find_element_by_name('id').send_keys(userid) 
# driver.find_element_by_name('pw').send_keys(pw)
# time.sleep(3)
# driver.find_element_by_class_name('btn_global').click()
# time.sleep(5)
driver.execute_script("document.getElementsByName('id')[0].value=\'" + userid + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'") 
        # document.getElementsByName : JS 메서드


# element창 로그인버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 Copy Xpath
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[2]/a').click()
time.sleep(2)

driver.find_element_by_class_name('tab_npay').click()
time.sleep(2)

