# keygenme-py
- Download the files required
- Notice that lines 157 - 192 check a value that we have to provide
- The solution is to just print thme out ahead of time, so that we can put it into the program and get the flag
- I added the following line of code: 
    ```print(hashlib.sha256(username_trial).hexdigest()[4]+hashlib.sha256(username_trial).hexdigest()[5]+hashlib.sha256(username_trial).hexdigest()[3]+hashlib.sha256(username_trial).hexdigest()[6]+hashlib.sha256(username_trial).hexdigest()[2]+hashlib.sha256(username_trial).hexdigest()[7]+hashlib.sha256(username_trial).hexdigest()[1]+hashlib.sha256(username_trial).hexdigest()[8])```
- Then run the program, enter the key provided and get the flag