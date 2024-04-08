# heap 0
- Connect to the server, and spam a bunch of 9s
- Notice how safe_var gets overwritten eventually, and changes it.
    - This can be seen in the code, as the memory for both variables are right next to each other, so when you overflow, it then switches to the next variable, and overwrites it. This is the case here
- We can control this, just spam `99999999999999999999999999999999pico`, then print the flag using the option, and the flag will be printed