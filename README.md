# RSAalgo

> RSAalgo.py is a basic implementation CLI tool of RSA Algorithm written in Python. It provides three functionalities:
> 1. Generation of public key (e, n) & private key (d, n)
> 2. Encryption of Integers and Characters (based on the ASCII values)
> 3. Decryption of Integers and Characters (based on the ASCII values)

For calculation of euler's totient function, phi(N) of a number, N seperately, use `eulertotient.py`

For calculation of euler's totient function, phi(N) of a number, N seperately, use `mi.sh`

 ### Examples:
 > `python3 RSAalgo.py generate`
 
 > ![Generate public & private keys](/pics/generate.png)
 
 > `python3 RSAalgo.py encrypt`
 
 > ![Encryption](/pics/encrypt.png)
 
 > `python3 RSAalgo.py decrypt`
 
 > ![Decryption](/pics/decrypt.png)
 
 > Use `python3 RSAalgo.py help` for usage
 
 > ![Decryption](/pics/rsaHelp.png)

 ## eulertotient.py
 > It takes a positive integer as a command line argument and generates the euler's totient function of it 
 
 > `python3 eulertotient.py help`
 
 ### Example:
 > `python3 eulertotient.py [num]`
 
 > ![Euler's Totient Function](/pics/et.png)

 ## mi.sh
 > It takes two positive integers (x, n) passed as command line arguments and output the modular multiplicative inverse of it.
 
 > `bash mi.sh help`
 
 ### Examples:
 > `bash mi.sh [num1] [num2]`
 
 > ![Modular Multiplicative Inverse](/pics/mi.png)

## Working of RSAalgo.py
> 1. Choosing two prime numbers (p, q)
> 2. Computing product of p & q `n = p * q`
> 3. Find Euler's totient function of n, phi(n)
>       `phi(n) = (p - 1) * (q - 1)` (As, p and q are prime, p.q=n)
> 4. Choose e, such that (1 < e < phi(n)) and gcd(e,phi(n))=1 [co-prime]
> 5. Public Key `(e, n)`, where e is encryption exponent
> 6. Compute d, using modular multiplicative inverse equation,
>       In simple terms, `(e.d)mod(phi(n)) == 1`
> 7. Private Key `(d, n)`, where n is decryption exponent
> 8. For Encryption,
>       C = P<sup>e</sup> mod n
> 9. For Decryption,
>        P = C<sup>d</sup> mod n

## Working of eulertotient.py
> Case I: If an integer n, is a prime number
>   `phi(n) = n - 1`

> Case II: If product of two prime numbers is equal to integer n, (p * q = n)
>   `phi(n) = (p - 1) * (q - 1)`

> Case III: If neither of the above case matches, then find all numbers from 1 upto n, whose gcd with n is 1 (gcd(num, n))
>   phi(n) = count of all numbers from above

## Working of mi.sh
> If two numbers (x & n are co-prime) or (n is a prime number, where x mod n != 0, x is not divisible by n) then modular multiplicative inverse can be calculated using the below condition,

>    `(x.mi)mod(phi(n)) == 1`, mi is modular multiplicative inverse

# For Complete Tutorial


