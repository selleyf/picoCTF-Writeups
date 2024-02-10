# Play Nice
Cryptography (110 points)
## Description 
Not all ancient ciphers were so bad... The flag is not in standard format. <span style="color:red"> nc mercury.picoctf.net 33686 </span> [playfair.py](./playfair.py)
## Solution
Connecting to mercury.picoctf.net 33686, we see
```console
┌──(fanni㉿kali-virtualbox)-[~]
└─$ nc mercury.picoctf.net 33686
Here is the alphabet: v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp
Here is the encrypted message: 4celvfdkoq5a0dx7pr40ifzctd8488
What is the plaintext message?
```
We need to reverse the encryption algorithm in [playfair.py](./playfair.py) to get the plaintext message from the encrypted message.

Studying the algorithm on https://en.wikipedia.org/wiki/Playfair_cipher, we see that we only need to reverse the encryption of pairs. 
When a pair is not in the same row or column, the encryption is symmetric: encryption is the same as decryption. When the two letters are in the same row, we have to replace them with the letters to their immediate *left*, respectively. 
When the two letters are in the same column, we replace them with the letters immediately *above*, respectively. 

So we change the respective function of [playfair.py](./playfair.py) accordingly:

```python
def decrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:
        return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
    elif p1[1] == p2[1]:
        return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]
```

And this is what we have to feed into the function decrypting a string:

```python
def decrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s
	else:
		plain = s + "v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp"[0]
	for i in range(0, len(plain), 2):
		result += decrypt_pair(plain[i:i + 2], matrix)
	return result
```
We get the decrypted message with the following script:

```python
alphabet = 'v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp'
msg = '4celvfdkoq5a0dx7pr40ifzctd8488'

playfair_mtx = generate_square(alphabet)
print(decrypt_string(msg, playfair_mtx))
```
Then we get the flag from the server:

```console
┌──(fanni㉿kali-virtualbox)-[~]
└─$ nc mercury.picoctf.net 33686
Here is the alphabet: v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp
Here is the encrypted message: 4celvfdkoq5a0dx7pr40ifzctd8488
What is the plaintext message? dpksmue41bnyue84jlem2jhl9ux755
Congratulations! Here's the flag: 3a64de31e7b5acb6c87ae45050e187ee
```
(Fyi: *do not* encase it with picoCTF{} for picoGym to accept it.)


