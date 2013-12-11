#!/usr/bin/env python

"""
This little program calculates the prime number up to a
given range using the "sieve of eratosthenes" algorithm.

it is called with "$: python sieve.py max_range"
where "max_range" is an integer between 2 and 7900
"""

import sys


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
