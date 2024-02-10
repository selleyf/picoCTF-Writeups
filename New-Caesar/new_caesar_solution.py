import string

LOWERCASE_OFFSET = ord("a") 
ALPHABET = string.ascii_lowercase[:16] # abcdefghijklmnop
SECRET = 'mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj'

def b16_decode(code):
    dec = ""
    for i in range(0, len(code), 2):
        char_to_binary = "{0:04b}".format(ALPHABET.index(code[i]))
        next_char_to_binary = "{0:04b}".format(ALPHABET.index(code[i+1]))
        joined_binary = int(char_to_binary + next_char_to_binary, 2)
        dec = dec + joined_binary.to_bytes((joined_binary.bit_length() + 7) // 8, 'big').decode()
    return dec

def unshift(c, k):
    t1 =  ord(c) - LOWERCASE_OFFSET
    t2 =  - ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

for key in ALPHABET:
	dec = ""
	for i, c in enumerate(SECRET):
		dec += unshift(c, key[i % len(key)])

	try:
		dec = b16_decode(dec)
  except UnicodeDecodeError:
		pass
	print(dec)
