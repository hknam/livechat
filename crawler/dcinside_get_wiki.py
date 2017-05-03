import os
from bs4 import BeautifulSoup
import urllib.request

url = 'http://wiki.dcinside.com/index.php?title=%ED%8A%B9%EC%88%98:%EC%99%B8%ED%86%A8%EC%9D%B4%EB%AC%B8%EC%84%9C&limit=5000&offset=0'


def crawl_word_url(url):
    url_open = urllib.request.urlopen(url)

    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    page_list = soup.find('ol', attrs={'class':'special'})

    word_list = page_list.findAll('li')

    file_path = os.path.expanduser('~')+'/Documents/dcinside/wiki/'

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_name = url.split('offset=')[1]

    f = open(file_path + file_name, 'w')


    for word in word_list:
        word_url = 'http://wiki.dcinside.com' + word.find('a')['href']
        print(word_url)
        f.write(word_url + '\n')

    f.close()

def main():

    for index in range(0, 4):
        base_url = 'http://wiki.dcinside.com/index.php?title=%ED%8A%B9%EC%88%98:%EC%99%B8%ED%86%A8%EC%9D%B4%EB%AC%B8%EC%84%9C&limit=5000&offset=' + str(index * 5000)
        crawl_word_url(base_url)


if __name__ == '__main__':
    main()
