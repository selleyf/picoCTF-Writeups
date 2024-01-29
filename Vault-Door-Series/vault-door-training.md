# vault-door-traning
Reverse Engineering (50 points)

## Description
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each 
door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, 
but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for 
that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](./VaultDoorTraining.java)

## Solution
First,
```java
String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```
asks for keyboard input and strips it from ```picoCTF{``` and ```}```. Then ```checkPassword``` checks the remaining string against
```java
"w4rm1ng_Up_w1tH_jAv4_3808d338b46"
```
so the flag is

> picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}
