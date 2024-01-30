# vault-door-7
Reverse Engineering (400 points)

## Description
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! 
The source code for this vault is here: [VaultDoor7.java](./VaultDoor7.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```passwordToIntArray``` does the following with the remaining string:

1. Computes the UTF-8 encoding of the first four characters,
2. Concatenates them in order to get a 32 bit number,
3. Converts it to an integer and stores it in the first element of the array ```x```.

Then the process is repeated for the second four characters, etc. Finally, ```checkPassword```  compares the elements of ```x``` against numbers that were produced by the same process from the flag.

The following Python script reverses this procedure (converts the given integer to a 32 bit binary number, slices it to four 8 bit binary numbers and converts them to characters via UTF-8 decoding):

```python
x = [""]*8 

x[0] = '{:032b}'.format(1096770097)
x[1] = '{:032b}'.format(1952395366)
x[2] = '{:032b}'.format(1600270708)
x[3] = '{:032b}'.format(1601398833)
x[4] = '{:032b}'.format(1716808014)
x[5] = '{:032b}'.format(1734293296)
x[6] = '{:032b}'.format(842413104)
x[7] = '{:032b}'.format(1684157793)


def split_to_8bit(x):
    return [x[:8], x[8:16], x[16:24], x[24:]]

bit_list = []
for i in range(8):
    bit_list += split_to_8bit(x[i])

flag = ""
for letter in bit_list:
    flag += chr(int(letter, 2))

print('picoCTF{' + flag + '}')
```
The flag:
```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}
```
