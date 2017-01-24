import sys
import os
from bs4 import BeautifulSoup
import urllib.request
import datetime
import calendar

'''
try:
    if not str(sys.argv[1]).startswith('/') :
        print('URL must start /"')
        sys.exit(1)
except IndexError as e:
    print('NEED .py [HTML_FOLDER_PATH]')
    sys.exit(1)

'''


def search(dirname):
    f=open('result.csv', 'w')
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        #file_name = full_filename.split('/')[-1]
        if full_filename.split('.')[1] == 'html':
            parse_html(full_filename, f)
            #break
    f.close()


def parse_html(url, f):
    page_url = 'file://'+url
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
    div_top_left = soup.find('div', attrs={'class':'w_top_left'})
    dl_list = div_top_left.findAll('dl')
    subject = dl_list[0].find('dd').text.strip()
    author = dl_list[1].find('dd').text.strip()

    div_top_right = soup.find('div', attrs={'class':'w_top_right'})
    ul = div_top_right.find('ul')
    li_list = ul.findAll('li')
    timestamp = li_list[0].text.strip()
    datetime_timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    utc_timestamp = calendar.timegm(datetime_timestamp.timetuple())

    print(subject, author, utc_timestamp)
    f.write(subject+','+author+','+str(utc_timestamp)+'\n')


search('/Users/namhyungyu/Documents/dcinside/')