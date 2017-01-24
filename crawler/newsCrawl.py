from selenium import webdriver
import os
import datetime
import random

driver = webdriver.Chrome('./chromedriver')


def crawl_news_list(file_dir):
    date = '2017-01-23'
    entertain_url = 'http://entertain.naver.com/home/mainNews?date='+date+'&page='
    page_num = 28

    f = open(file_dir+'/news_list', 'w')


    for cnt in range(1, page_num+1):
        page_url = entertain_url+str(cnt)
        driver.get(page_url)

        news_list = driver.page_source
        xpath = "//ul[@class='news_lst news_lst2']"

        title_area = driver.find_element_by_xpath(xpath)

        title_li = title_area.find_elements_by_css_selector('li')

        for tit in title_li:
            title = tit.find_element_by_css_selector('a')
            href = title.get_attribute('href')

            f.write(href+'\n')


        driver.implicitly_wait(5)

    f.close()

    driver.close()

def crawl_news_page(file_dir):

    open_f=open(file_dir+'/news_list', 'r')
    line = open_f.readline()
    while True:
        if not line:
            break

        driver.get(line)

        driver.implicitly_wait(5)

        file_name = line.split('=')[2]
        file_name = file_name.replace('\n', '')

        write_f=open(file_dir+'/'+file_name+'.html', 'w')
        write_f.write(driver.page_source)
        write_f.close()

        line = open_f.readline()

def main():
    folder_name = datetime.date.today().isoformat()
    file_dir = '/Users/namhyungyu/Documents/naverNews/' + folder_name


    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


    #crawl_news_list(file_dir)
    crawl_news_page(file_dir)


if __name__ == '__main__':
    main()