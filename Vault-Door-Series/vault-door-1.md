# vault-door-1
Reverse Engineering (100 points)

## Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](./VaultDoor1.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks the characters of the remaining string one-by-one to see if they match certain characters:
```java
password.length() == 32 &&
password.charAt(0)  == 'd' &&
password.charAt(29) == 'a' &&
password.charAt(4)  == 'r' &&
password.charAt(2)  == '5' &&
password.charAt(23) == 'r' &&
password.charAt(3)  == 'c' &&
password.charAt(17) == '4' &&
password.charAt(1)  == '3' &&
password.charAt(7)  == 'b' &&
password.charAt(10) == '_' &&
password.charAt(5)  == '4' &&
password.charAt(9)  == '3' &&
password.charAt(11) == 't' &&
password.charAt(15) == 'c' &&
password.charAt(8)  == 'l' &&
password.charAt(12) == 'H' &&
password.charAt(20) == 'c' &&
password.charAt(14) == '_' &&
password.charAt(6)  == 'm' &&
password.charAt(24) == '5' &&
password.charAt(18) == 'r' &&
password.charAt(13) == '3' &&
password.charAt(19) == '4' &&
password.charAt(21) == 'T' &&
password.charAt(16) == 'H' &&
password.charAt(27) == '6' &&
password.charAt(30) == 'f' &&
password.charAt(25) == '_' &&
password.charAt(22) == '3' &&
password.charAt(28) == 'd' &&
password.charAt(26) == 'f' &&
password.charAt(31) == '4';
```

Transforming this to Python code,

```python
java_code = """
password.charAt(0)  == 'd' &&
password.charAt(29) == 'a' &&
password.charAt(4)  == 'r' &&
password.charAt(2)  == '5' &&
password.charAt(23) == 'r' &&
password.charAt(3)  == 'c' &&
password.charAt(17) == '4' &&
password.charAt(1)  == '3' &&
password.charAt(7)  == 'b' &&
password.charAt(10) == '_' &&
password.charAt(5)  == '4' &&
password.charAt(9)  == '3' &&
password.charAt(11) == 't' &&
password.charAt(15) == 'c' &&
password.charAt(8)  == 'l' &&
password.charAt(12) == 'H' &&
password.charAt(20) == 'c' &&
password.charAt(14) == '_' &&
password.charAt(6)  == 'm' &&
password.charAt(24) == '5' &&
password.charAt(18) == 'r' &&
password.charAt(13) == '3' &&
password.charAt(19) == '4' &&
password.charAt(21) == 'T' &&
password.charAt(16) == 'H' &&
password.charAt(27) == '6' &&
password.charAt(30) == 'f' &&
password.charAt(25) == '_' &&
password.charAt(22) == '3' &&
password.charAt(28) == 'd' &&
password.charAt(26) == 'f' &&
password.charAt(31) == '4'"""

python_code = java_code.replace('password.charAt(', 'flag[').replace(')', ']').replace(' == ', ' = ').replace(' &&','')
print(python_code)
```

we can use it to create a script which assign characters to a string and thus building flag:

```python
flag = ['']*32

# paste python_code
flag[0]  = 'd'
flag[29] = 'a'
flag[4]  = 'r'
flag[2]  = '5'
flag[23] = 'r'
flag[3]  = 'c'
flag[17] = '4'
flag[1]  = '3'
flag[7]  = 'b'
flag[10] = '_'
flag[5]  = '4'
flag[9]  = '3'
flag[11] = 't'
flag[15] = 'c'
flag[8]  = 'l'
flag[12] = 'H'
flag[20] = 'c'
flag[14] = '_'
flag[6]  = 'm'
flag[24] = '5'
flag[18] = 'r'
flag[13] = '3'
flag[19] = '4'
flag[21] = 'T'
flag[16] = 'H'
flag[27] = '6'
flag[30] = 'f'
flag[25] = '_'
flag[22] = '3'
flag[28] = 'd'
flag[26] = 'f'
flag[31] = '4'

print('picoCTF{' + ''.join(flag) + '}')
```
The flag:
> picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}


