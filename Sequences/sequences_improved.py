#import math
import hashlib
import sys
import numpy as np
from gmpy2 import mpz, mpq
import timeit
#from tqdm import tqdm
#import functools

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfe2d6046e248ff7962b")

# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
# @functools.cache
# def m_func(i):
#     if i == 0: return 1
#     if i == 1: return 2
#     if i == 2: return 3
#     if i == 3: return 4

#     return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)

def m_func(i):
    v_0 = np.array([1, 2, 3, 4])

    if i < 4:
        return v_0[i]

    eigenvalues = [mpz(-21), mpz(12), mpz(13), mpz(17)] 
    eigenvalues_imin3 = np.array([pow(eigenvalue, i - 3) for eigenvalue in eigenvalues])

    D_imin3 = np.diag(eigenvalues_imin3)

    S = np.array([[-1, 1, 1, 1],
              [21, 12, 13, 17],
              [-441, 144, 169, 289],
              [9261, 1728, 2197, 4913]])

    S_inv = np.array([[mpq(-13, 209), mpq(581, 42636), mpq(-7, 7106), mpq(1, 42636)],
              [mpq(1547, 55), mpq(-409, 165), mpq(-3, 55), mpq(1, 165)],
              [mpq(-63, 2), mpq(405, 136), mpq(1, 17), mpq(-1, 136)],
              [mpq(819, 190), mpq(-369, 760), mpq(-1, 190), mpq(1, 760)]])

    A_imin3 = np.dot(np.dot(S, D_imin3), S_inv)

    v_imin3 = np.dot(A_imin3, v_0)

    return v_imin3[3]

# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    start = timeit.default_timer()
    sol = m_func(ITERS)
    stop = timeit.default_timer()
    print('Time: ', stop - start) 
    decrypt_flag(sol)
