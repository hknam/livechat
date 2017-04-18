from selenium import webdriver
import random
import time
import os


base_url = 'http://sports.news.naver.com/wfootball/vod/index.nhn?category=primera&listType=game'

move_game_script = "document.getElementsByClassName('arr prev')[0].click();"

def change_game(index):
    return "document.getElementsByClassName('bx')["+index+"].click();"


driver_path = './chromedriver'

driver = webdriver.Chrome(driver_path)

driver.get(base_url)

file_path = os.path.expanduser('~') + 'Documents/sports/'

if not os.path.exists(file_path):
    os.makedirs(file_path)


count = 1000

try:
    for index in range(0, count):
        driver.implicitly_wait(5)
        file_name = driver.find_element_by_class_name('day').text+'.html'

        print(file_name)
        with open(file_path + file_name, 'w') as f:
            f.write(driver.page_source)

        driver.execute_script(move_game_script)
        time.sleep(random.randrange(2,4))


    driver.quit()

except Exception as e:
    print(e)