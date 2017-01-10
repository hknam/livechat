from selenium import webdriver
import time

drive_path = './chromedriver'

driver = webdriver.Chrome(drive_path)
#os.environ["webdriver.chrome.driver"] = driver
driver.get('https://www.youtube.com/live_chat?v=h7v_Erh6eCI&is_popout=1')
driver.implicitly_wait(5)

while True:
    file_name = time.time()
    f=open('./html/'+str(file_name)+'.html', 'w')
    page_source = driver.page_source
    f.write(page_source)
    f.close()
    driver.refresh()
    driver.implicitly_wait()
    print(file_name)

