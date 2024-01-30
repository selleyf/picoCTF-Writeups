# vault-door-6
Reverse Engineering (350 points)

## Description
This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](./VaultDoor6.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks that the characters of the remaining string one-by-one bitwise XORed with the character ```0x55``` give the following
hexadecimal numbers:
```java
{
  0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
  0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
  0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
  0xa , 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c,
}
```
Applying the bitwise XOR with ```0x55``` to these characters will give back the key, since ```(c ^ 0x55) ^ 0x55 = c``` for any character ```c```. This Python script does the job:
```python
hex_str = """0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d, 0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa , 
0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27, 0xa , 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c""".replace("0x0","0x00").replace("0xa","0x0a").replace("0x","").replace(" ","").replace(",","")

byte_str = bytes.fromhex(hex_str)  
key = '55'*32
key_byte_str = bytes.fromhex(key) 
flag = ''.join([chr(byte_str[i] ^ key_byte_str[i]) for i in range(len(byte_str))])

print('picoCTF{' + flag + '}')
```
The flag:
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}
```
