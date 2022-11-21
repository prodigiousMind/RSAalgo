#!/usr/bin/python3

# Author: https://github.com/prodigiousMind
# Youtube: https://youtube.com/@prodigiousMind

import sys
import string

plSt = []

def encrypt(e, n, P):
    if str(P).isdigit():
        return (int(P) ** e) % n
    else:
        P=str(P)
        for i in P:
            try:
                iAscii = ord(i)
                plSt.append(chr((iAscii**e)%n))
            except: plSt.append(i)
        return ''.join(plSt)


def decrypt(d, n, C):
    if str(C).isdigit():
        return (int(C) ** d) % n
    else:
        C=str(C)
        for i in C:
            try:
                iAscii = ord(i)
                plSt.append(chr((iAscii**d)%n))
            except: plSt.append(i)
        return ''.join(plSt)

def help():
    print("RSAalgo.py encrypt/decrypt/generate/help\n")
    print("RSAalgo.py encrypt - To encrypt the data")
    print("RSAalgo.py decrypt - To decrypt the data")
    print("RSAalgo.py  generate - To calculate n, phi(n), e, d")
    print("RSAalgo.py  help - To Show Help")

try:

    if sys.argv[-1] == "encrypt":
        l = input("Enter e, public key exponent & n, eg: e, n (37, 2881): ")
        e, n = int(l.split(",")[0]), int(l.split(",")[1])
        plaintext = input("Enter plaintext: ".format(n))
        ciphertext = encrypt(e, n, plaintext)
        print(60*"-")
        print("(e, n): ({}, {})\nPlaintext: {}\nCiphertext: {}".format(e, n, plaintext, ciphertext))
        print(60*"-")

    elif sys.argv[-1] == "decrypt":
        l = input("Enter d, private key exponent & n, eg: d, n (1873, 2881): ")
        d, n = int(l.split(",")[0]), int(l.split(",")[1])
        C = input("Enter ciphertext: ")
        decrypted = decrypt(d, n, C)
        print(60*"-")    
        print("(d, n): ({}, {})\nCiphertext: {}\nPlaintext: {}".format(d, n, C, decrypted))
        print(60*"-")

    elif sys.argv[-1] == "generate":
        print("Enter two large prime numbers (p & q)")
        p = int(input("enter p: "))
        q = int(input("Enter q: "))
        n = p * q
        phiN = (p - 1) * (q - 1)

        e = int(input("Enter e (such that 1 < e < {phiN}, and e & phi(n) are co-prime [gcd(e, {phiN}) = 1]): ".format(phiN=phiN)))

        for mi in range(1, phiN):
            if (mi * e) % phiN == 1:
                d = mi
                break
        print(60*"-")
        print("p: {}\nq: {}\nn: {}\nEuler's totient function, phi(n): {}\ne: {}\nd: {}".format(p, q, n, phiN, e, d))
        print("public key (e, n): ({}, {})\nprivate key (d, n): ({}, {})".format(e,n,d,n))
        print(60*"-")

    else:
        help()

except:
    help()
