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
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        file_name = full_filename.split('/')[-1]
        if file_name.split('.')[1] == 'html':
            json_result = extract_script(full_filename)
            break



def parse_html(url):
    page_url = url
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




parse_html('http://gall.dcinside.com/board/view/?id=drama_new1&no=592822&page=1330')


