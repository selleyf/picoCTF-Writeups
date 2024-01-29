# Transformation
Reverse Engineering (20 points)
## Description 
I wonder what this really is... [enc.txt](./enc.txt) 
```python 
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
## Solution
1. Understand the encryption: take the fist two characters of the secret to be encrypted. Compute the UTF-8 encoding for both, then concatenate it to get a 16-bit number. Decode the (UTF-16 encoded) character.
2. Reverse the encryption: take the UTF-16 encoding of a character, slice it to 8-8 digits. Decode the two UTF-8 encoded characters and concatenate to the solution. In Python:
```python 
binary = ["{0:15b}".format(ord(char)) for char in code]
dec = ''.join([chr(int(binary[i][0:7], 2))+ chr(int(binary[i][7:], 2)) for i in range(len(code))])
```
See [flag.txt](./flag.txt) for the flag. 
