from bs4 import BeautifulSoup
import os
import urllib.request
import datetime
import calendar
import sys


def search(dirname):
    f=open(fname, 'w')
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        #file_name = full_filename.split('/')[-1]
        if full_filename.split('.')[1] == 'html':
            #print(full_filename)
            parse_html(full_filename, f)
            #break
    f.close()


def parse_html(url, f):
    page_url = 'file://'+url
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    comment_list = soup.find('div', attrs={'class':'cbox_list_area'})
    time_list = comment_list.findAll('div', attrs={'class':'cbx_info'})
    cmt_list = comment_list.findAll('div', attrs={'class':'cbx_cmt'})

    for index in range(0, len(cmt_list)):
        cmt = cmt_list[index].text
        cmt = cmt.strip()
        timestamp = time_list[index].find('span', attrs={'class':'c_date'}).text
        timestamp = timestamp.strip()
        print(timestamp, cmt)
        f.write(timestamp + '\t' + cmt + '\n')

target_folder_path = sys.argv[1]
fname = target_folder_path.split('/')[-1] + '.tsv'

search(target_folder_path)
