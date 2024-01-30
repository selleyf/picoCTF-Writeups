# vault-door-4
Reverse Engineering (250 points)

## Description
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](./VaultDoor4.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks that the characters of the input match various ASCII encodings as a sequence of bytes:
```java
{
  106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
  0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
  0142, 0131, 0164, 063 , 0163, 0137, 0146, 064 ,
  'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e' ,
}
```
The first 8 characters represent decimal encoding format, the second 8 hexadecimal, the third 8 octal and the last 8 are the characters themselves. This Python script decodes the flag:
```python
my_bytes = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            '55', '6e', '43', '68', '5f', '30', '66', '5f',
            '0142', '0131', '0164', '063' , '0163', '0137', '0146', '064',
            'a' , '8' , 'c' , 'd' , '8' , 'f' , '7' , 'e']

flag = ''
for i in range(8):
    flag += chr(my_bytes[i])
for i in range(8,16):
    flag += bytes.fromhex(my_bytes[i]).decode("ASCII") 
for i in range(16,24):
    flag += chr(int(my_bytes[i], 8))
for i in range(24,32):
    flag += my_bytes[i]

print('picoCTF{' + ''.join(flag) + '}')
```
The flag:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
```
