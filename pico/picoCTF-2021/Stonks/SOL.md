# Stonks
- Download the vuln.c (you could do it without it, but it makes reading this a lot easier)
- Notice that the flag file `api` is loaded into memory -> suggesting that we should just attempt to print the memory
- As clang notes, we can read the memory, so just spam %x (the binary is most likely 32-bit, but you could use %lx if you wanted)
- Then just spam cyberchef to convert the hex memory into a string, and swap endianness (x86 is little-endian by default), and get the flag (delete some characters at the beginning if neccessary)