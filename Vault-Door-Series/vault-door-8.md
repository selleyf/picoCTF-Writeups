# vault-door-8
Reverse Engineering (450 points)

## Description
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents 
to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](./VaultDoor8.java)

## Solution
First, the code needs to be formatted. A decent source code editor does this job automatically (I used VS Code). Formatted code: [VaultDoor8Formatted.java](./VaultDoor8Formatted.java)

The code prompts the user to enter the password. The input is stripped from presumably ```picoCTF{``` and ```}``` (more precisely, the first 8 and last character).

Then ```checkPassword``` first calls ```scramble```, which takes the UTF-8 encoding of each character and switches around some bits. The result is then compared in ```checkPassword``` to hexadecimal 
numbers, which were produced by the flag via the same process.

To reverse this, notice that we get back the original 8 bit number by applying the same switch twice: 

00000101 -> 00000110 -> 00000101 

(here we applied switch(6,7) twice). But note that two 
switches don't commute: applying switch(6,7) and then switch(5,6) is 

00000101 -> 00000110 -> 00000110

while applying switch(5,6) and then switch(6,7) is 

00000101 -> 00000011 -> 00000011. 

This means that the 
inverse of ```scramble``` is ```scramble```, with the order of switch commands reversed. We need to convert the given hexadecimal numbers to 8 bit binaries, do the described unscrambling, then convert to
characters by UTF-8 decoding to get the flag. 

This Python code does the job:

```python
hex_string = "f4c097f07797c0e4f077a4d0c577f486d0a5459627b577d2d0b4e1c1e0d0d0e0"
bit_list = ['{:08b}'.format(int(hex_string[i:i+2], 16)) for i in range(0, 63, 2)]

def bit_switch(bit_ascii, p1, p2):
    new_bit_ascii = [*bit_ascii]
    new_bit_ascii[p1], new_bit_ascii[p2] = new_bit_ascii[p2], new_bit_ascii[p1]
    return ''.join(new_bit_ascii)

def unscramble(bit_list):
    for i in range(len(bit_list)):
        c = bit_list[i]
        c = bit_switch(c,7,6)
        c = bit_switch(c,5,2)
        c = bit_switch(c,4,3)
        c = bit_switch(c,1,0)
        c = bit_switch(c,7,4)
        c = bit_switch(c,6,5)
        c = bit_switch(c,3,0)
        c = bit_switch(c,2,1)
        bit_list[i] = c
    return bit_list

new_bit_list = unscramble(bit_list)
flag = ''
for item in new_bit_list:
    decimal_no = sum([int(item[7-i])*2**i for i in range(8)])
    flag += chr(decimal_no)

print('picoCTF{' + flag + '}')
```
The flag:
```
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}
```
