#!/usr/bin/env python3
"""a(n) = number of cycles of the permutation x -> (2^n-1) - rot(x) on n-bit words
(rotate left one place, then complement every bit).  Burnside formula, checked
against direct enumeration for n <= 16.   python3 rotcomp.py [--bfile N]"""
import sys
from math import gcd
def a(n):
    L = 2 * n if n % 2 else n                    # order of g = C o R
    s = 0
    for j in range(L):
        g = gcd(j % n, n) if j % n else n        # cycles of R^j have length n/g, count g
        if j % 2 == 0: s += 2 ** g               # g^j = R^j
        elif (n // g) % 2 == 0: s += 2 ** g      # g^j = C R^j: fixed words alternate on each cycle
    assert s % L == 0
    return s // L
def brute(n):
    p = (1 << n) - 1; rot = lambda x: ((x << 1) | (x >> (n - 1))) & p
    seen, c = set(), 0
    for s in range(p + 1):
        if s in seen: continue
        c += 1; x = s
        while x not in seen: seen.add(x); x = p - rot(x)
    return c
if __name__ == "__main__":
    assert all(a(n) == brute(n) for n in range(1, 17))
    if len(sys.argv) > 2 and sys.argv[1] == "--bfile":
        for n in range(1, int(sys.argv[2]) + 1): print(n, a(n))
    else:
        print(",".join(str(a(n)) for n in range(1, 31)))
