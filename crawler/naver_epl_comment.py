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


target_folder_name = 'epl'

driver_path = './chromedriver'

driver = webdriver.Chrome(driver_path)

page_number = 1


def move_next_page(page_num):
    return "document.getElementsByClassName('N=a:CML.page,r:"+str(page_num)+"')[0].click();"

def move_neet_ten_page():
    return "document.getElementsByClassName('cbox_next N=a:CML.next')[0].click();"

try:
    driver.get(base_url)
    date = base_url.split('gameId=')[1]

    file_path = os.path.expanduser('~') + '/Documents/' + target_folder_name + '/' + date + '/'

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    for index in range(1, 5000):

        file_name = file_path + str(index) + '.html'

        f=open(file_name, 'w')

        if index % 10 == 1:
            f.write(driver.page_source)
            continue

        elif index % 10 == 0:
            script = move_next_page(index)
            driver.execute_script(script)
            f.write(driver.page_source)


            script = move_neet_ten_page()
            driver.execute_script(script)


        else:
            script = move_next_page(index)
            driver.execute_script(script)
            f.write(driver.page_source)


        print(script)

        f.close()
        time.sleep(random.randrange(1,3))


except Exception as e:
    print(e)
    driver.quit()


