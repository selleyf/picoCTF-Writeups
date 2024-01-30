# vault-door-5
Reverse Engineering (300 points)

## Description
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! 
The source code for this vault is here: [VaultDoor5.java](./VaultDoor5.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks that after a round of URL encoding and base-64 encoding, the transformed input matches the string 
```"JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"```. We need to reverse first the base-64 encoding, then the
URL encoding. This Python script does the job: 
```python
import base64
from urllib.parse import unquote

string_expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"

# base 64 decoding
convert_bytes = string_expected.encode("ascii")
converted_bytes = base64.b64decode(convert_bytes)
decoded_string = converted_bytes.decode("ascii")

# URL decoding
flag = unquote(decoded_string)

print('picoCTF{' + flag + '}')
```
The flag:
```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}
```
