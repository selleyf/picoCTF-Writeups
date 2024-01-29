import itertools

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

hex_string = "57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"  
byte_string = bytes.fromhex(hex_string)

# by trial-end error we see that the encryption was done with 3 random strings
for combination in itertools.combinations(random_strs, 3):
    ctxt = byte_string
    for random_str in combination:
        ctxt = encrypt(ctxt, random_str)
    key = encrypt(b'picoCTF',ctxt[:7])
    print(key.decode("ASCII")) 
    ctxt = encrypt(ctxt, key)
    print(ctxt.decode("ASCII"))

