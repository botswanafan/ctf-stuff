# MatchTheRegex
- Open the given web instance
- Look at the `send_request()` function, the regex provided is: ^p.....F!?. This boils down to ^ (matching the beginning of the string), p (matching the letter p), then any given characters (as indicated by the `.`), the F (matching `F` only), then `!?`, meaning the string matches 0 or 1 `!`
- I just entered `picoCTF!`, and got the flag