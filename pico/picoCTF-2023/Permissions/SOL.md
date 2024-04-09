# Permissions
- Start the instance to begin the chall by using the ssh command and password given
- From the tags, we can see that we can use vim for this challenge. Directly using vim is banned, but using the `vi` command we can access files. Additionally, we are part of the sudoers group, so we can do `sudo vi`
- From there, we can use vim (there are plenty of tutorials on how to run commands) as follows: `In normal mode, type :e then press Space and Ctrl-D. That will list file names in the current directory.`
- From there, we can navigate to /challenge/metadata.json, which contains the flag in plaintext.