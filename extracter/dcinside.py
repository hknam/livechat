import collections

def save_comment():
    comment_list = []
    flist=open('../parser/result.tsv', 'r')

    while True:
        line = flist.readline()
        if not line:
            break
        comment_list.append(line)
    e15 = open('e16.tsv', 'w')
    for comment in comment_list:
        try:
            title = comment.split('\t')[0]
            author = comment.split('\t')[1]
            timestamp = comment.split('\t')[2]

            if int(timestamp) >= 1485033600:
                if int(timestamp)<=1485037980:
                    e15.write(title+'\t'+author+'\t'+timestamp)

        except IndexError as e:
            print(e)

    e15.close()
    flist.close()

def extract_top_clip():
    comment_list = []
    clip_list = []
    flist = open('e15.tsv', 'r')
    while True:
        line = flist.readline()
        if not line:
            break
        comment_list.append(line)

    comment_list.reverse()

    start = int(comment_list[0].split('\t')[2]) + 10
    count = 0
    for comment in comment_list:
        title = comment.split('\t')[0]
        timestamp = int(comment.split('\t')[2])
        if timestamp <= start:
            count+=1
            #print(title)
        else:
            clip_list.append(str(timestamp)+','+str(count))
            start = timestamp+10
            count =1

    for clip in clip_list:
        count = int(clip.split(',')[1])
        if count >= 17:
            print(clip)

extract_top_clip()