from selenium import webdriver
import time
import sys


try:
    if not str(sys.argv[1]).startswith('https://'):
        print('URL must start "https://www.youtube.com"')
        sys.exit(0)
except IndexError as e:
    print('NEED .py [LIVE_STREAMING_URL]')
    sys.exit(1)


live_url = sys.argv[1]

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver

#driver.implicitly_wait(5)


while True:
    driver.get(live_url)
    driver.implicitly_wait(5)

    file_path = '/Users/namhyungyu/Documents/youtube/'
    file_name = time.strftime('%Y-%m-%d %T:%M:%S', time.localtime())+'.html'

    f=open(file_path + file_name, 'w')
    f.write(driver.page_source)
    f.close()
    print(file_name)

    driver.refresh()
    driver.implicitly_wait(5)

