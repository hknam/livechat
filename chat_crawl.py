from selenium import webdriver
import os

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver

driver.get('https://www.youtube.com/watch?v=bWqpvO8eukY')
driver.implicitly_wait(5)



while True:
    comment_ul = driver.find_element_by_id('all-comments')
    comment_li = comment_ul.find_elements_by_css_selector('li')

    for li in comment_li:
        timestamp = li.get_attribute('data-timestamp')
        comment = li.find_element_by_class_name('comment-text').text

        print(timestamp, comment)

    driver.refresh()
    driver.implicitly_wait(5)



    '''
    for comment_li in comment_ul:
        timestamp = comment_li.find_element_by_css_selector('li').get_attribute('data-timestamp')
        comment = comment_li.find_element_by_class_name('comment-text')

        print(comment.text, timestamp)
    '''


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

'''