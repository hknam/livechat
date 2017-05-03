import os
import urllib.request
from bs4 import BeautifulSoup


file_path = os.path.expanduser('~') + '/Documents/afreeca/2017-04-25/'



def search(dirname):
    f=open('result.tsv', 'w')
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)

        if full_filename.split('.')[1] == 'html':
            parse_html(full_filename)

chat_length = []


def parse_html(url):
    page_url = 'file://'+url
    url_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')
    dl_list = soup.findAll('dl')
    #print(page_url, len(dl_list))
    chat_length.append(len(dl_list))

    for dl in dl_list[1:]:
        chat = dl.text.split(':')[1].strip()
        print(chat)



#search(file_path)

#chat_length.sort(reverse=True)

'''
for chat in chat_length:
    print(chat)
'''
parse_html('/Users/hknam/Documents/afreeca/2017-04-25/1493119341.html')