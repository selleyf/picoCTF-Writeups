# XtraORdinary
Cryptography (150 points)
## Description
Check out my new, never-before-seen method of encryption! I totally invented it myself. I added so many for loops that I don't even know what it does. It's extraordinarily secure!

[output.txt](./output.txt)

[encrypt.py](./encrypt.py)

## Solution

1. Understand ```encrypt.py```: the function ```encrypt(ptxt, key)``` outputs the bitwise XOR of ```ptxt``` and ```key```, characterwise. E.g if ```ptxt = "abc"``` and ```key = "de"```, we get

      b'a' ^ b'd' <-> 01100001 ^ 01100100 = 00000101 -> b'\x05'
   
      b'b' ^ b'e' <-> 01100010 ^ 01100101 = 00000111 -> b'\x07'
   
      b'c' ^ b'd' <-> 01100011 ^ 01100100 = 00000111 -> b'\x07'

   The flag is encrypted this way with an unknown key. Then same process is repeated for the following strings, for a number of times (this number for each string is chosen randomly).

      ```python
      random_strs = [
       b'my encryption method',
       b'is absolutely impenetrable',
       b'and you will never',
       b'ever',
       b'ever',
       b'ever',
       b'ever',
       b'ever',
       b'ever',
       b'break it'
       ]
      ```
   Finally, the result is decoded to ASCII characters.

2. The important thing to realize is that XOR with the same key applied twice is the identity operation: ``` (a ^ b) ^ b = a```.

   First, ```encrypt(encrypt(ctxt, random_str), random_str) = ctxt```. This means that from the point of decoding, the only thing that matters if ```ctxt``` was encrypted with ```random_str``` odd or even times: in the even case, we get ```ctxt```, in the odd case we get ```encrypt(ctxt, random_str)``` from which we can get back ```ctxt = encrypt(encrypt(ctxt, random_str), random_str)```.

   So we need try every combination ```encrypt(...(encrypt(encrypt(ctxt, random_str_0), random_str_1),... random_str_j)``` for ```random_str_i in random_strs, i <= j = 0,...,4``` (notice that we have 5 different random strings.)

   How do we know if we got ```ctxt```? Take the first 7 characters and encrypt "picoCTF" with it. This will give a guess for the key, since ```encrypt("picoCTF", "secret[:7]") = key```, as we hope that ```encrypt(key, "secret[:7]") = "picoCTF"``` (notice that ```encrypt``` is symmetric in its two arguments -provided that their length is the same-, as the bitwise XOR operation is such.) Notice that we are also hoping for the key to have 7 characters. We decode ```ctxt``` with our guess for the key: ```ptxt = encrypt(ctxt, key)```, since ```ctxt = encrypt(ptxt, key)```.

   Finally we comb through the results to find something that looks like a flag.

See [flag.txt](./flag.txt) for the flag, [key.txt](./key.txt) for key and [xtra_solution.py](./xtra_solution.py) for the implementation of the idea above.
