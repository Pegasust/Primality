# prime_factor(7815361098838094241990551) gives 198449351 ^ 3 (correct but slow)
def prime_factor(n):
    start = str(n)
    nums = []
    p = 2
    # test each number until sqrt(n)
    while n >= p * p:
        if n % p == 0:
            # It is the first prime
            nums.append(str(p))
            n //= p
        else:
            # do 6k optimization if larger or equal to 5
            if p < 5:
                p += 1
            else:
                p += 6
    # This is the last prime factor (or the only prime factor)
    nums.append(str(n))
    print("{} = {}".format(start, " * ".join(nums)))
