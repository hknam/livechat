from bs4 import BeautifulSoup
import urllib.request
import os

clip_count = 1
total_time = 0

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if full_filename.find('.html') > 0:
            read_element (full_filename)

def page_open(page_url):
     return urllib.request.urlopen(page_url)

def read_element(page_url):
    global total_time, clip_count
    file_path = 'file://'+page_url
    url_open = page_open(file_path)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
    try:
        video_list = soup.find('div', attrs={'class':'video_list'})
        ul = video_list.find('ul')
        li_list = ul.findAll('li')
        for li in li_list:
            if li.text.find('하이라이트') > 0:
                timestamp = li.find('span', attrs={'class':'time'}).text
                timestamp = timestamp.replace('재생시간', '').split(':')
                seconds = int(timestamp[0])*60+int(timestamp[1])
                print(seconds)
                total_time +=seconds
                clip_count+=1
    except Exception as e:
        print(e)

search('/Users/namhyungyu/Documents/sports/')
print(total_time, clip_count, total_time/clip_count)
