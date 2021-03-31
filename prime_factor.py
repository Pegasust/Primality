def prime_factor(n):
    start = str(n)
    nums = []
    p = 2
    while n >= p * p:
        if n % p == 0:
            nums.append(str(p))
            n //= p
        else:
            if p < 5:
                p += 1
            else:
                p += 6
    nums.append(str(n))
    print("{} = {}".format(start, " * ".join(nums)))
