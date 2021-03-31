# Primality

A small repository that demonstrate pseudocodes/algorithms relating to prime numbers. This small repository has proven to be useful in my college CS classes, as I saved lots of time not to reinvent and re-research on this matter whenever prime number algorithms is involved.

## find_next_prime.py: requires is_prime() [sqr_6k_primality.py]

This provides next_prime(n: int) which finds the next prime number (higher than n). Also provides generate_first_primes(n: int) which generates a list of first `n` primes using next_prime(n)

## sqr_6k_primality.py: 

This provides the is_prime(n:int) function that uses 6k optimization. The code is a direct fork from the [wikipedia page](https://en.wikipedia.org/wiki/Primality_test#Python_code)

## prime_factor.py: 

This provides prime factorization function that uses something like the 6k optimization prime check, but reduces the input number by the prime numbers. This should optimize from the traditional brute-force way with is_prime then divide.

## prime_japanese_date.py: requires find_next_prime.py

A small program to generate a prime japanese date format (YYYY/MM/DD) that it itself a prime number (in base10). This is a small hobby project to kind of verify Zero Escape 3 release date. This script is thought to be buggy at the point of writing.