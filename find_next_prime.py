from sqr_6k_primality import is_prime

def next_prime(n):
    """
        Bertrand's postulate (actually a theorem) states that
        if n > 3 is an integer, then there always exists at least
        one prime number p with n < p < 2n − 2
    """
    if n % 2 == 0:
        n += 1
    for i in range(n+1, 2*n):
        if is_prime(i):
            return i

    
