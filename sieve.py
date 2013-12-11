#!/usr/bin/env python

import sys

# Pseudo Code
#primes = sieve [2..]
#sieve (p : xs) = p : sieve [x | x <- xs. x 'mod' p > 0]


def sieve(xs, primes=[]):
    """
    This function calculates the prime numbers up to a given range.
    The tested maximal range is 7900.
    """
    if len(xs) == 0:
        return primes
    primes.append(xs[0])
    return sieve([x for x in xs if x % xs[0] > 0], primes)


def find_primes(max_value):
    """
    just a function to beautify...not really needed, but nice to have
    """
    return sieve(range(2, max_value + 1))

if __name__ == "__main__":
    if not sys.argv[1]:
        print find_primes(50)
    else:
        print find_primes(int(sys.argv[1]))
