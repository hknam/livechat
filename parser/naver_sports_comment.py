from bs4 import BeautifulSoup
import os
import urllib.request
import datetime
import calendar

def search(dirname):
    f=open('result.tsv', 'w')
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

    comment_list = soup.find('div', attrs={'class':'cbox_list_comment'})
    ul = comment_list.find('ul')
    li_list = ul.findAll('li', attrs={'class':'cbox_thumb_on'})
    for li in li_list:
        comment_area = li.find('div', attrs={'class':'cbox_comment_area'})
        info_area = comment_area.find('div', attrs={'class':'cbox_info_area'})

        box_section = info_area.find('div', attrs={'class':'cbox_section'})
        user_id = box_section.find('span', attrs={'class':'cbox_user_id'}).text
        date = box_section.find('span', attrs={'class':'cbox_date'}).text

        comment = comment_area.find('div', attrs={'class':'cbox_desc_comment'}).text.strip()
        comment = comment.replace('\n', '')

        print(user_id, date, comment)



search('/Users/namhyungyu/Documents/sports/2017021930011002880/')