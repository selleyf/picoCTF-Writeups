# vault-door-3
Reverse Engineering (200 points)

## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](./VaultDoor3.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks that certain characters of the input string match certain characters of the string 
```"jU5t_a_sna_3lpm12g94c_u_4_m7ra41"```, according to this rule:

```java
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
String s = new String(buffer);
```
Inverting the logic, we can deduce the correct input string with this Python script:

```python
result_string = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"
flag = ['']*32
for i in range(8): 
    flag[i] = result_string[i]
for i in range(8, 16): 
    flag[23-i] = result_string[i]
for i in range(16, 32, 2): 
    flag[46-i] = result_string[i]
for i in range(31, 16, -2): 
    flag[i] = result_string[i]
print('picoCTF{' + ''.join(flag) + '}')
```
The flag:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
```
