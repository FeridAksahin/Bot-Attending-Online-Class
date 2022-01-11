from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://lms.uskudar.edu.tr/Course/MyCourses' 
PATH = r'C:\\Users\\Ferid\\Desktop\\chromedriver.exe' 

web = webdriver.Chrome(PATH) 
action = ActionChains(web) 
web.get(URL) 

web.maximize_window()
time.sleep(2)
search = web.find_element_by_xpath('//*[@id="UserName"]')
search.send_keys('190209063')
search.send_keys(Keys.RETURN)
time.sleep(2)
search = web.find_element_by_name('Password')
search.send_keys('my_password_was_here')
search.send_keys(Keys.RETURN)
time.sleep(2)
derslerimLink = web.find_element_by_xpath('//*[@id="r_menu_my_courses"]/a')
action.double_click(derslerimLink).perform()
time.sleep(2)
web.get('https://lms.uskudar.edu.tr/Activity/Index/F50A4CFDAE9499C1753AABF0E8265605')
time.sleep(2)
softQuaLink = web.find_element_by_link_text('PROCESS QUALITY')
softQuaLink.click()
time.sleep(2)
do = web.find_element_by_xpath('//*[@id="vcVideo"]')
do.click()