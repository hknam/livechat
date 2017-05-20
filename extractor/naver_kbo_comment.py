def extract_top_comment():
    f=open('../parser/result.tsv', 'r')
    result = []
    count = 1

    while True:
        line = f.readline()
        if not line:
            break

        try:
            timestamp = line.split('\t')[0]
            comment = line.split('\t')[1]

            if int(timestamp) >= 1478111400:
                if int(timestamp) <= 1478123520:
                    result.append(timestamp+'/'+comment)
                    #print(timestamp)

        except Exception as e:
            print(e)
    f.close()


def extract_comments():
    f = open('../parser/result.tsv', 'r')
    result = ''
    count = 1

    while True:
        line = f.readline()
        if not line:
            break

        try:
            timestamp = line.split('\t')[0]
            comment = line.split('\t')[1]
            comment = comment.replace('\n', '')

            if str(timestamp) == '1478119740':
                result+=comment+','
        except Exception as e:
            print(e)
    f.close()
    print(result)
extract_comments()