from random import choice
import sys


def legendre(a, p):
    j = (a ** ((p - 1) // 2)) % p
    if j == p - 1:
        return -1
    else:
        return j


def prime(i, primes):
    for prime in primes:
        if not i % prime:
            return False
    return True


def primes(n):
    primes = set()
    for p in range(3, n + 1, 2):
        if prime(p, primes):
            primes.add(p)
    return list(primes)


def make_prog(ins, out):
    seen = set()
    prime_list = primes(200)
    i300 = set(range(1, 300))
    code = ""
    for i in ins:
        tried = set()
        next_prime = choice(prime_list)
        next_num = next(iter(i300 - seen))
        while legendre(next_num, next_prime) != i:
            if i == 0:
                prime_multiples = {next_prime * i for i in range(2, 10)}
                next_num = next(iter(prime_multiples - seen - tried))
            else:
                next_num = next(iter(i300 - seen - tried))
            tried.add(next_num)
        seen.add(next_num)
        out.write(f"({next_num}/{next_prime})")
    return code

# ALTERNATE VERSION THAT ALWAYS FINDS A SOLUTION:
#
# def make_prog(ins, out):
#     seen = set()
#     prime_list = primes(200)
#     ints = set(range(1, len(ins) ** 2))
#     for i in ins:
#         tried = set()
#         next_prime = choice(prime_list)
#         next_num = choice(list(ints - seen))
#         while next_num in seen | tried or legendre(next_num, next_prime) != i:
#             tried.add(next_num)
#             next_num += 1
#         seen.add(next_num)
#         out.write(f"({next_num}/{next_prime})")

# you can translate any program
hello_world = [-1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1,
               -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1,
               1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1,
               -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1,
               -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1,
               1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1,
               -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1,
               -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1,
               -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1,
               1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1,
               1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1,
               -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1,
               1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1]

print(make_prog(hello_world, sys.stdout))
