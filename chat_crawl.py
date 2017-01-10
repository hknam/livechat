from selenium import webdriver
import time

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver

driver.implicitly_wait(5)



while True:
    driver.get('https://www.youtube.com/live_chat?is_popout=1&v=1oJxQoi-5C8')
    driver.implicitly_wait(5)

    file_path = '/Users/namhyungyu/Documents/youtube/'
    file_name = time.strftime('%Y-%m-%d %T:%M:%S', time.localtime())+'.html'

    f=open(file_path + file_name, 'w')
    f.write(driver.page_source)
    f.close()
    print(file_name)

    driver.refresh()
    driver.implicitly_wait(5)
