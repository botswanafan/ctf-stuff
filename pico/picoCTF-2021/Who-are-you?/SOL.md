# Who are you?
This chall is just abusing [a wikipedia article repeatedly and getting lucky with your guesses as to which header you need](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- Open the given webpage, and notice that you need to have the "PicoBrowser" in order to solve this chall.
- Send a request that has a User-Agent of PicoBrowser, and you will come across another obstacle: I don't trust users visiting from another site.
- Now you need to set the refferer as the host, so I set the Host and Referer (yes it is mispelled on purpose apparently) header as: `http://mercury.picoctf.net:36622`.
- Then we get another error: Sorry, this site only worked in 2018. To fix this, I set the Date header as `2018` which seems to pass their checks.
- Then another Header obstacle: I don't trust users who can be tracked. To fix this, we use the Do-Not-Track header as: [DNT: 1](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT)
- then another obstacle (this challenge is very tedious for sure), now we need to be in Sweden. To solve this, use the X-Forwarded-For header and get a swedish ip (I used `192.44.242.19`), which seemed to work
- Then we need to have our language set as Swedish: You're in Sweden but you don't speak Swedish? To fix this, we use the Accept-Language header with value `sv-SE`
- Now the flag is given!

My entire http request for the lazy:
```GET / HTTP/1.1
Host: http://mercury.picoctf.net:36622
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8
Accept-Language: sv-SE
Accept-Encoding: gzip, deflate
Referer: http://mercury.picoctf.net:36622/
DNT: 1
Date:  2018
X-Forwarded-For: 192.44.242.19
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache```