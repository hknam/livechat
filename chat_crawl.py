from selenium import webdriver
import os

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver

driver.get('https://www.youtube.com/watch?v=h7v_Erh6eCI')
driver.implicitly_wait(10)

comment_list = driver.find_elements_by_class_name('comment-text')

for comment in comment_list:
    print(comment, comment.text)
