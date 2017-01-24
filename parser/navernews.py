from bs4 import BeautifulSoup
import urllib.request
import os

def search(dirname):
    f=open(dirname+'result', 'w')
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        try:
            file_name = full_filename.split('/')[-1]
        except Exception as e:
            print(e, full_filename)
            continue
        if full_filename.split('.')[1] == 'html':
            parse_html(full_filename, f)

    f.close()


def parse_html(page_url, f):
    url = 'file://'+page_url
    url_open = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    content = soup.find('div', attrs={'id':'content'})
    end_ct = content.find('div')
    end_ct_area = end_ct.find('div', attrs={'class':'end_ct_area'})

    article_title = end_ct_area.find('p').text
    end_body_wrp = end_ct_area.find('div', attrs={'class':'end_body_wrp'})

    article_body = end_body_wrp.find('div').text
    article_body = article_body.replace('이미지 원본보기', '')
    article_body = article_body.replace('\n', '')

    f.write(article_title+'\n')

    print(page_url)



def main():
    file_path = '/Users/namhyungyu/Documents/naverNews/2017-01-24/'
    search(file_path)



if __name__ == '__main__':
    main()
