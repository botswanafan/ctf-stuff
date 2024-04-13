# dont-use-client-side
- Open up the webpage and view source
- Unsuprisingly (as per the name of the chall), the password validation is done client side
- There is a large amount of javascript to parse the password, but it is based around substrings. In all honesty, if I were doing this live, I would just ask chatgpt for this mlao, but for the sake of practice, do it manually. The split is 4, so you can do this by piecing together parts of the string at a time, by following the pattern 0->4, 4->8, then putting them all together for the final flag.

