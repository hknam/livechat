from bs4 import BeautifulSoup
import urllib.request
import sys
import random
import time
import os


try:
    page_number = int(sys.argv[1])
    target_folder_name = sys.argv[2]

except IndexError as e:
    print('NEED [PAGE NUMBER] [TAGET FOLDER NAME]')
    sys.exit(1)


def read_table(page_number):
    page_url = 'http://gall.dcinside.com/board/lists/?id=drama_new1&page=' + str(page_number)
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    tr_list = soup.findAll('tr', attrs={'class':'tb'})
    for tr_count in range(2, len(tr_list)):
        body_list = tr_list[tr_count].find('td', attrs={'class': 't_subject'})
        body_url = 'http://gall.dcinside.com' + body_list.find('a')['href']
        crawl(body_url)



def crawl(url):
    url_open = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
    page_source = str(soup.prettify())
    file_name = url.split('&')[-2].split('=')[1]
    file_path = os.path.expanduser('~')+'/Documents/'+target_folder_name+'/'

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    f = open(file_path + file_name + '.html', 'w')
    f.write(page_source)
    f.close()
    print(url)
    time.sleep(random.randrange(2,5))

def main():
    count = page_number
    while True:
        read_table(count)
        count+=1


if __name__ == '__main__':
    main()
