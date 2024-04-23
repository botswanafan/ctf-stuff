# Super Serial
- Open up the given webpage, and head to `/robots.txt`
- We see an entry called `/admin.phps`, which doesn't lead to anything of itself
- However, we can try `/index.phps`, which does reveal some php (mine is listed in 1.php)
- In `1.php`, we can see that the file calls for `authentication.php`, which we can head to. 
- All we see is `Welcome Back Guest`, so we try `/authentication.phps`, which shows some more php (mine is listed in 2.php)
- We then realise that we need to get admin rights to read/write to the flag file, so we embark on that
- This file calls another file called `cookie.php`, which we then view `/cookie.php`
- Trying similar tricks, we view `cookie.phps` at `/cookie.phps`, which then shows more php (which is in cookie.phps)
    - You could have just jumped here from the first file, which also included cookie.php