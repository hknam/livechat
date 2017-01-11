from bs4 import BeautifulSoup
import urllib.request
import os
import json

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        file_name = full_filename.split('/')[-1]
        if file_name.split('.')[1] == 'html':
            json_result = extract_script(full_filename)
            break




def extract_script(page_url):
    page_open = urllib.request.urlopen('file://'+page_url)
    soup = BeautifulSoup(page_open, 'html.parser', from_encoding='utf-8')
    scripts = soup.findAll('script')
    chat_script = scripts[7]
    #print(type(chat_script))
    chat_json = chat_script.text.split('window["ytInitialData"] = ')[1]
    chat_json = chat_json.split('</script>')[0].replace(';', '')
    chat_json = chat_json.strip()

    json_filename = '/Users/namhyungyu/Documents/result/'+page_url.split('/')[-1]+'.json'

    f=open(json_filename, 'w')
    f.write(chat_json)
    f.close()
    print(json_filename)

search("/Users/namhyungyu/Documents/youtube")


