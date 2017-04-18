from selenium import webdriver
import os
import datetime
import sys
from naver_get_news_title import *
import time
import random

def crawl_news_page(driver, file_dir):

    open_f=open(file_dir+'/news_list', 'r')
    line = open_f.readline()
    while True:
        if not line:
            break

        driver.get(line)

        driver.implicitly_wait(5)

        file_name = line.split('=')[2]
        file_name = file_name.replace('\n', '')
        file_name = file_name.replace('?', '')

        write_f=open(file_dir+'/'+file_name+'.html', 'w')
        write_f.write(driver.page_source)
        write_f.close()
        time.sleep(random.randrange(2,5))

        line = open_f.readline()

def main():
    folder_name = datetime.date.today().isoformat()
    file_dir = os.path.expanduser('~') + '/Documents/news/'+ folder_name + '/'


    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if len(sys.argv[1]) == 0:
        print('Need date')
        sys.exit(1)

    date = sys.argv[1]
    driver = webdriver.Chrome('./chromedriver')

    crawl_news_list(driver, file_dir, date)
    crawl_news_page(driver, file_dir)


if __name__ == '__main__':
    main()