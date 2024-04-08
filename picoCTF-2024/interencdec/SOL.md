# interencdec
- Download the file
- It looks to be base64 encrypted (by the two = at the end), so we do that to get a value starting with `b`, so I trimmed that character onwards and removed the quotations
- Then rotating the characters by 19 reveals the `picoCTF` flag