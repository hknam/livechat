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
    f=open('result.tsv', 'w')
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        #file_name = full_filename.split('/')[-1]
        if full_filename.split('.')[1] == 'html':
            parse_html(full_filename, f)

    f.close()


def parse_html(url, f):
    page_url = 'file://'+url
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    # 팀별로 class name이 다름
    cbox_area = soup.find('div', attrs={'class':'cbox_list_area bg_kbo_OB'})

    cbox_list = cbox_area.find('ul', attrs={'class':'cbox_list'})

    li_list = cbox_list.findAll('li')

    for li in li_list:
        if li.text == '신고':
            continue
        else:
            timestamp = li.find('span', attrs={'class':'c_date'}).text
            comment = li.find('div', attrs={'class':'cbx_cmt'}).text.strip()
            comment = comment.replace('\n', '')

            datetime_timestamp = datetime.datetime.strptime(timestamp, "%Y.%m.%d %H:%M")
            utc_timestamp = calendar.timegm(datetime_timestamp.timetuple())

            print(utc_timestamp, comment)
            f.write(str(utc_timestamp) + '\t' + comment + '\n')



search('/Users/namhyungyu/Documents/kbo/77771102OBNC02016/')