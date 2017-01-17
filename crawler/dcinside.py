from bs4 import BeautifulSoup
import urllib.request
import sys
import random
import time


try:
    page_number = int(sys.argv[1])
    page_url = 'http://gall.dcinside.com/board/view/?id=drama_new1&page=' + str(page_number)

except IndexError as e:
    print('NEED PAGE NUMBER')
    sys.exit(1)


def read_table(page):
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    table_list = soup.find('div', attrs={'class':'list_table'})

    tbody = table_list.find('tbody', attrs={'class', 'list_tbody'})
    tr_list = tbody.findAll('tr')

    for tr in tr_list:
        href = tr.find('a')['href']
        if not str(href).startswith('/board'):
            continue
        else:
            print(href)
            crawl(href)




def crawl(href):
    url = 'http://gall.dcinside.com'+href
    url_open = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
    page_source = str(soup.prettify())
    file_name = url.split('&')[-2].split('=')[1]
    f = open('/Users/namhyungyu/Documents/dcinside/' + file_name + '.html', 'w')
    f.write(page_source)
    f.close()
    time.sleep(random.randrange(2,5))

def main():
    count = page_number
    while True:
        read_table(count)
        count+=1


if __name__ == '__main__':
    main()