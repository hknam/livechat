from bs4 import BeautifulSoup
import urllib.request
import os
import sys


html_path = sys.argv[1]
json_path = sys.argv[2]

if len(html_path) == 0:
    print('.py [HTML FOLDER] [JSON_FOLDER]')
    sys.exit(1)

if len(json_path) == 0:
    print('.py [HTML FOLDER] [JSON_FOLDER]')
    sys.exit(1)


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        file_name = full_filename.split('/')[-1]
        if file_name.split('.')[1] == 'html':
            json_result = extract_script(full_filename)
            break




def extract_script(page_url):
    #page_open = urllib.request.urlopen('file://'+page_url)
    page_open = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page_open, 'html.parser', from_encoding='utf-8')
    scripts = soup.findAll('script')
    chat_script = scripts[7]
    #print(type(chat_script))
    chat_json = chat_script.text.split('window["ytInitialData"] = ')[1]
    chat_json = chat_json.split('</script>')[0].replace(';', '')
    chat_json = chat_json.strip()

    json_filename = json_path+page_url.split('/')[-1]+'.json'

    f=open(json_filename, 'w')
    f.write(chat_json)
    f.close()
    print(json_filename)


def main():

    #search(html_path)
    extract_script('file:///Users/namhyungyu/test.html')

if __name__ == '__main__':
    main()



