# useless
- connect to the server using the given ssh command
- Looking around in the directory via `ls`, we find an executable called useless.
- If we run the script the first time, we notice that it wants us to read the code.
- Then we notice from the `$#` that it wants 3 arguments passed, the first of which should either be "add", "sub", "div" or "mul"
- However, the last else statement wants us to use the man command, so we run `man useless` and find that the flag is the very last thing in the command 
(this was a very interesting chall)