from sqr_6k_primality import is_prime

def next_prime(n):
    """
        Bertrand's postulate (actually a theorem) states that
        if n > 3 is an integer, then there always exists at least
        one prime number p with n <= p < 2n − 2
    """
    # make it odd
    if n % 2 == 0:
        n += 1
    # we only want to pass in odd numbers, so increase by 2
    for i in range(n, 2*n, 2):
        if is_prime(i):
            return i

    
def generate_first_primes(n):
    """
        Generates the first `n` prime numbers using next_prime.
        TODO: Sieve can be a better option to generate such
    """
    retval = [2]
    while len(retval) < n:
        retval.append(next_prime(retval[-1]+1))
    return retval
