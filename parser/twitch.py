import sys
import os
from bs4 import BeautifulSoup
import urllib.request
import datetime
import calendar



def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)

        if full_filename.split('.')[1] == 'tsv':
            parse_chat(full_filename)



def parse_chat(fname, date):

    file_path = os.path.expanduser('~') + '/Documents/twitch/'

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    result_file_name = file_path + fname.split(' ')[1]

    f1 = open(result_file_name, 'w')
    f2 = open(fname, 'r')
    while True:
        line = f2.readline()
        if not line:
            break
        list = line.split(':')
        timestamp = list[0].strip()

        if list[0].find(date) >= 0:

            chat = list[-1].strip().replace('\n', '')
            f1.write(chat + '\n')
            print(timestamp, chat)

    f1.close()
    f2.close()

try:
    target_folder_name = sys.argv[1]
    search_timestamp = sys.argv[2]
except Exception as e:
    print(e)
    sys.exit(1)


search(target_folder_name)