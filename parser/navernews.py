from bs4 import BeautifulSoup
import urllib.request
import os

result_file_path = '/Users/namhyungyu/Documents/result/'
def search(dirname, f):

    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)

        try:

            if full_filename.find('html') > 0:
                parse_html(full_filename, f)


        except Exception as e:
            print(e, full_filename)
            continue


def parse_html(page_url, f):
    url = 'file://'+page_url
    url_open = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_open, 'html.parser', from_encoding='utf-8')

    try:
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
    except Exception as e:
        print(e)


def main():
    file_path = '/Users/namhyungyu/Downloads/news/'
    folder_list = os.listdir(file_path)
    f=open(result_file_path+'result', 'w')
    for list in folder_list:
        full_file_list = os.path.join(file_path, list) + '/'
        search(full_file_list, f)

    f.close()

if __name__ == '__main__':
    main()
