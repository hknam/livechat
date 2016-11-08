from selenium import webdriver
import os

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver

driver.get('https://www.youtube.com/watch?v=bWqpvO8eukY')
driver.implicitly_wait(5)


'''
while True:
    comment_list = driver.find_elements_by_class_name('comment-text')
    for comment in comment_list:
        print(comment, comment.text, comment.find_elements_by_tag_name('data-timestamp'))

    driver.refresh()
    driver.implicitly_wait(5)
'''

while True:

    comment_list = driver.find_elements_by_id('all-comments')

    for comment in comment_list:
        time_stamp = comment.find_element_by_css_selector('li').get_attribute('data-timestamp')
        comment_div = comment.find_element_by_class_name('comment-text')
        text = comment_div.text

        print(time_stamp, text)

    driver.refresh()
    driver.implicitly_wait(5)

