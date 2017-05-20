import sys
import os

def search(dirname, start_time):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        #file_name = full_filename.split('/')[-1]
        if full_filename.split('.')[1] == 'tsv':
            count_text(full_filename, start_time)
            #break


def count_text(fname, start_time):
    f=open(fname, 'r')
    data = f.read()
    count = data.count(start_time)
    if count != 0:
        print(count)
    f.close()


fname = sys.argv[1]


tfile = open(fname, 'r')
while True:
    start_time = tfile.readline()
    start_time = start_time.replace('\n', '')
    if not start_time:
        break
    search('/home/hknam/Downloads/ogn_lol', start_time)

tfile.close()

'''
while True:
    start_time = input('Enter time : ')
    search('/home/hknam/Downloads/ogn_lol', start_time)
'''


