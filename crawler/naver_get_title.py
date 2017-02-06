from selenium import webdriver


def crawl_news_list(driver, file_dir, date):

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
