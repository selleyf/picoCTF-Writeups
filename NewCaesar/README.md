# New Caesar
Cryptography (60 points)
## Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj 
* [new_caesar.py](./new_caesar.py)
## Solution
1. First, let's understand what the code does!
   
   1.1 Note that ```ALPHABET``` is the string ```"abcdefghijklmnop"```.
   
   1.2 ```b16_encode(plain)```: for each character ```c``` of the plaintext ```plain```, it computes the UTF-8 encoding, takes the first four digits, converts it to decimal and takes the character of corresponding index from ```ALPHABET``` ; similarly for the last four digits. E.g.

   'p' -> 01110000 -> 0111, 0000 -> 7, 0 -> 'h', 'a'

   Then these two characters are concatenated to the encoded text ```enc```.

   1.3 ```shift(c,k)```: takes the index of character ```k``` in ```ALPHABET```, and shifts the character ```c``` with this index (modulo the length of ```ALPHABET```). E.g.

   'h', 'b' -> index: 7, index: 1 -> index: 7+1 = 8 -> 'i'

   1.4 Now for the main part: we can read off that the unknown key consists of a single character from ```ALPHABET```. Then the encoding works in the following way: first, the flag is encoded with ```b16_encode```, then each character of the result is shifted with the unknown key via ```shift```.

2. We need to invert this algorithm.

   2.1 First construct and algorithm that inverts ```shift``` e.g by knowing the key shifts the character ```c``` backwards, e.g if the key is 'b', then

   'i', 'b' -> 'h'

   2.2 Invert ```b16_encode```, e.g. construct an algorithm that transforms

   "ha" -> 'p'

   2.3 Do a brute force search for the key by trying all characters from ```ALPHABET```. Pick the output that resembles a flag.

This is implemented in [new_caesar_solution.py](./new_caesar_solution.py). For the flag, see [new_caesar_flag.txt](./new_caesar_flag.txt).
