# dont-you-love-banners
- Connect to the first given server, as it can be used to gather the password. For instance, I used: `nc tethys.picoctf.net 64772`, and the password was printed
- Then answer the info-sec questions, the answers are: DEFCON, then John Draper
- From there, we have access to a server, so we can exploit it
- We can read both `/etc/passwd` and `/etc/shadow`, so we can get the password (using johntheripper) as `iloveyou`
- Then in `/challenge`, we can read the `metadata.json` file to get the flag