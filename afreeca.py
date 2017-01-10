from selenium import webdriver
import os
import time

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)



driver.get('http://play.afreecatv.com/dbseo012/187218994')
driver.implicitly_wait(10)


time.sleep(35)

f=open('test.html', 'w')
f.write(driver.page_source)
f.close()

driver.quit()