from socket import *
import time
import sys
import os

try:
    if not str(sys.argv[1]).startswith('https://'):
        print('URL must start "https://www.twitch.tv"')
        sys.exit(0)
except IndexError as e:
    print('NEED .py [LIVE_STREAMING_URL]')
    sys.exit(1)


server_name = 'irc.twitch.tv'
port = 6667

password = 'oauth:u0t937zaesb5y4lczpopxfr7faurgy'
nickname = 'w88272'
#channel = '#gabrielcro'
channel = '#' + sys.argv[1].split('/')[-1]

socket = socket(AF_INET, SOCK_STREAM)
socket.connect((server_name, port))

socket.send(('PASS ' + password + '\r\n').encode())
socket.send(('NICK ' + nickname + '\r\n').encode())
socket.send(('JOIN '+channel + '\r\n').encode())


file_path = os.path.expanduser('~') + '/Documents/twitch/' + channel + '/'

if not os.path.exists(file_path):
    os.makedirs(file_path)


curr_time = time.strftime('%Y-%m-%d %T-%M-%S', time.localtime())



f=open(file_path+str(curr_time)+'.tsv', 'w')


while True:
    recv_message = socket.recv(4096)
    recv_time = time.strftime('%Y-%m-%d %T:%M:%S', time.localtime())
    #recv_time = time.time()
    if recv_message == 'PING :tmi.twitch.tv\r\n' :
        socket.send('PONG :tmi.twitch.tv\r\n')

    elif len(recv_message) == 0:
        f.close()
        os.system('python3 twitch.py '+sys.argv[1])
        sys.exit(0)

    else:
        print(recv_time, recv_message.decode())
        f.write(recv_time + '\t' + recv_message.decode()+'\n')

