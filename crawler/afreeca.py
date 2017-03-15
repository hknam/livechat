from selenium import webdriver
import os
import time
import sys
from datetime import datetime

drive_path = './chromedriver'

try:
    target_page_url = sys.argv[1]
    target_folder_name = sys.argv[2]
except IndexError as e:
    print('NEED [PAGE URL][TARGET_FOLDER_NAME]')
    sys.exit(1)


driver = webdriver.Chrome(drive_path)

clear_script = "$('#li_chat_memodel').find('a').trigger('click')"

driver.get(target_page_url)
driver.implicitly_wait(10)


try:
    while True:
        time.sleep(10)
        chat_area = driver.find_element_by_id('chat_memoyo')
        timestamp = datetime.now()
        text = chat_area.get_attribute('innerHTML')

        # local time to utc converter - deprecated
        """
        datetime_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        utc_timestamp = calendar.timegm(timestamp.timetuple())
        """

        local_time = int(time.mktime(timestamp.timetuple()))

        folder_name = time.strftime('%Y-%m-%d', time.localtime())
        file_path = os.path.expanduser('~') + '/Documents/afreeca/' + target_folder_name + '/' + str(folder_name) + '/'

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_name = str(local_time)

        f=open(folder_name+file_name, 'w')
        f.write(text)
        f.close()

        print(text)

        driver.execute_script(clear_script)

except Exception as e:
    print(e)
    driver.quit()