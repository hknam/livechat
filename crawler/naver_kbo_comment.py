from selenium import webdriver
import os
import time
import sys
import random

try:
    base_url = sys.argv[1]

except IndexError as e:
    print('NEED [URL]')
    sys.exit(1)


target_folder_name = 'kbo'

driver_path = './chromedriver'

driver = webdriver.Chrome(driver_path)



def home_next_page(page_num):
    return "showComment({page_no: "+str(page_num)+"}, 0);"

def away_next_page(page_num):
    return "showComment({page_no: "+str(page_num)+"}, 1);"


try:
    driver.get(base_url)
    date = base_url.split('gameId=')[1].split('&')[0]


    file_path = os.path.expanduser('~') + '/Documents/' + target_folder_name + '/' + date + '/'

    if not os.path.exists(file_path):
        os.makedirs(file_path)



    total_list = driver.find_elements_by_xpath('.//span[@class ="c_total"]')
    home_total = int(total_list[1].text.split(' ')[1][:-2])
    away_total = int(total_list[3].text.split(' ')[1][:-2])

    home_page_number = (home_total // 8) + 1
    away_page_number = (away_total // 8) + 1

    if home_page_number >= away_page_number:
        page_number = home_page_number
    else:
        page_number = away_page_number

    for index in range(1, page_number + 1):

        script = home_next_page(index)
        driver.execute_script(script)
        print(script)



        file_name = file_path + str(index) + '.html'
        f = open(file_name, 'w')
        f.write(driver.page_source)
        f.close()

        time.sleep(random.randrange(1,3))

except Exception as e:
    print(e)
    driver.quit()


