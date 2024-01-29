random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

hex_string = "57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"  
byte_string = bytes.fromhex(hex_string)

# by trial-end error we see that the encryption was done with three random strings
for key1 in random_strs:
    for key2 in random_strs:
        for key3 in random_strs:
            #for key4 in random_strs:
                #for key5 in random_strs:
                    ctxt = encrypt(byte_string, key1)
                    ctxt = encrypt(ctxt, key2)
                    ctxt = encrypt(ctxt, key3)
                    #ctxt = encrypt(ctxt, key4)
                    #ctxt = encrypt(ctxt, key5)
                    key = encrypt(b'picoCTF',ctxt[:7])
                    print(key.decode("ASCII"))
                    ctxt = encrypt(ctxt, key)
                    print(ctxt.decode("ASCII")) 

