#!/usr/bin/env python3
"""
Transition inversion on the Hamming apertures -- exact checks, r = 3 .. 7.

Setting (no container): for r >= 2, n = 2^r - 1, GF(2^r) = F_2[x]/(g), g primitive,
alpha = x.  The cyclic Hamming code is C_r = { w : sum_{i in supp w} alpha^i = 0 }.
It is defined by a relation (a vanishing sum) and nothing else: no radius,
metric or embedding occurs.

TI1  Transition map.  D(w) = w + shift(w), i.e. multiplication by (1+x).
     D maps C_r ONTO its even-weight subcode; ker D|C_r = {0, all-ones}.
TI2  Syndrome action.  syn(D w) = (1+alpha) syn(w) = alpha^{Z(1)} syn(w)
     (Z = Zech logarithm).  D rotates the nonzero syndromes (the Fano/PG(r-1,2)
     points) by a fixed step Z(1); the step depends on the chart g (transliteration),
     the cycle it generates does not.
TI3  Re-inversion.  (D w, parity(w)) is lossless on C_r: prefix-XOR returns w up to
     the kernel, and the parity bit (the [2^r,2^r-r-1,4] extension coordinate,
     'WAY') names the kernel class.  This is RR-OEIS-TRANSFORM-GRAPH OG1 (a
     difference loses one common level per component; one anchor returns it)
     realized on the code.
TI4  Object = description only at r = 3.  D(C_r) = C_r^perp  <=>  r = 3.
     Equivalently the extension RM(r-2,r) is self-dual iff r = 3.
TI5  Quadratic phase.  f(z) = z^2 + 1 = (z+1)^2 on GF(2^r):
       f^2 = z^4;  r odd: f^r = z + 1 (complement half-turn), order 2r,
       no fixed points, cycles = {0,1} + (2^r-2)/(2r) cycles of length 2r;
       r even: order r, fixed points = roots of z^2+z+1 (GF(4) cube roots of 1).
     f acts on non-wall states as ONE cycle  <=>  r = 3.
TI6  LM-ATLAS.  The snowball's labeled phase (0,9,1,8,4,5,2,7; 1->4->2->8->5->7,
     0<->9) equals z -> z^2+1 under F_2-linear identifications of the eight
     positions with GF(8); its complement alias 9-d is f^3 = z+1 (RR-NONRADIAL
     NR3: A = C^3), and the reflection J = (4 7)(2 5) is a linear transvection.
TI7  Transliteration.  A radix-b digit readout of 1/p, p = 2^r - 1, has the cycle
     type of f on non-wall states iff p is prime and ord_p(b) = 2r.  (r=3: b=10.)
"""
import json, sys
from itertools import permutations
from functools import reduce

PRIM = {3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011, 7: 0b10000011}
RECIP3 = 0b1101
OUT = {}; FAIL = []

def ck(name, cond, detail=None):
    OUT[name] = {"pass": bool(cond), "detail": detail}
    if not cond: FAIL.append(name)

def gmul(a, b, g, r):
    p = 0
    while b:
        if b & 1: p ^= a
        b >>= 1; a <<= 1
        if a >> r & 1: a ^= g
    return p

def powers(r, g):
    el = [1]
    for _ in range((1 << r) - 2):
        x = el[-1] << 1
        if x >> r & 1: x ^= g
        el.append(x)
    return el

def syn(w, el):
    return reduce(lambda a, b: a ^ b, (el[i] for i in range(len(el)) if w >> i & 1), 0)

def D(w, n):
    return w ^ (((w << 1) | (w >> (n - 1))) & ((1 << n) - 1))

def rank2(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v: basis.append(v)
    return len(basis), basis

def code_basis(r, g):
    """Basis of C_r: x^j * gen(x), gen = minimal polynomial of alpha = g itself."""
    n = (1 << r) - 1; k = n - r
    return [g << j for j in range(k)], n, k

def dual_basis(r, g):
    """C^perp = simplex: rows w_t(i) = Tr-free form: bit t of alpha^i."""
    el = powers(r, g); n = len(el)
    return [sum(((el[i] >> t) & 1) << i for i in range(n)) for t in range(r)]

for r, g in list(PRIM.items()) + [("3r", RECIP3)]:
    rr = 3 if r == "3r" else r
    el = powers(rr, g); n = len(el); log = {v: i for i, v in enumerate(el)}
    B, n, k = code_basis(rr, g)
    ck(f"r{r}_basis_in_code", all(syn(b, el) == 0 for b in B) and rank2(B)[0] == k)
    DB = [D(b, n) for b in B]
    rk, _ = rank2(DB)
    ck(f"r{r}_TI1_image_dim_k-1_all_even", rk == k - 1 and all(bin(v).count("1") % 2 == 0 for v in DB), (rk, k))
    ones = (1 << n) - 1
    ck(f"r{r}_TI1_all_ones_in_code_and_killed", syn(ones, el) == 0 and D(ones, n) == 0)
    z1 = log[1 ^ el[1]]
    ok = all(syn(D(1 << j, n), el) == el[(log[syn(1 << j, el)] + z1) % n] for j in range(n))
    ck(f"r{r}_TI2_syndrome_rotation_step_Z1", ok, z1)
    ck(f"r{r}_TI3_parity_names_kernel_class", bin(ones).count("1") % 2 == 1)
    dual = dual_basis(rr, g)
    same = rank2(dual + DB)[0] == rank2(dual)[0] == rk
    ck(f"r{r}_TI4_D(C)==dual", same == (rr == 3), {"D(C)=C_perp": same, "dimD": rk, "dim_dual": len(dual)})
    # TI5 quadratic phase
    N = 1 << rr
    f = [gmul(z, z, g, rr) ^ 1 for z in range(N)]
    f2 = [f[f[z]] for z in range(N)]
    frob2 = [gmul(gmul(z, z, g, rr), gmul(z, z, g, rr), g, rr) for z in range(N)]
    ck(f"r{r}_TI5_f2_is_z4", f2 == frob2)
    fr = list(range(N))
    for _ in range(rr): fr = [f[x] for x in fr]
    cyc, seen = [], set()
    for s in range(N):
        if s in seen: continue
        x, L = s, 0
        while True:
            seen.add(x); x = f[x]; L += 1
            if x == s: break
        cyc.append(L)
    fixed = [z for z in range(N) if f[z] == z]
    if rr % 2:
        ck(f"r{r}_TI5_odd_fr_is_z+1", fr == [z ^ 1 for z in range(N)])
        ck(f"r{r}_TI5_odd_cycles", sorted(cyc) == sorted([2] + [2 * rr] * ((N - 2) // (2 * rr))), sorted(cyc))
    else:
        ck(f"r{r}_TI5_even_order_r_fixed_cube_roots", fr == list(range(N)) and
           all(gmul(z, z, g, rr) ^ z ^ 1 == 0 for z in fixed) and len(fixed) == 2, {"fixed": fixed, "cycles": sorted(cyc)})
    ck(f"r{r}_TI5_single_nonwall_cycle_iff_r3", (sorted(cyc) == [2, N - 2]) == (rr == 3))

# TI6: LM-ATLAS
LAB = (0, 9, 1, 8, 4, 5, 2, 7); PH = {0: 9, 9: 0, 1: 4, 4: 2, 2: 8, 8: 5, 5: 7, 7: 1}
fpos = [LAB.index(PH[LAB[v]]) for v in range(8)]
sols = []
for g in (0b1011, 0b1101):
    for b1, b2, b4 in permutations(range(1, 8), 3):
        img = [(b1 if v & 1 else 0) ^ (b2 if v & 2 else 0) ^ (b4 if v & 4 else 0) for v in range(8)]
        if len(set(img)) == 8 and all(img[fpos[v]] == gmul(img[v], img[v], g, 3) ^ 1 for v in range(8)):
            sols.append({"g": bin(g), "phi": img})
ck("TI6_atlas_phase_is_z2+1", len(sols) > 0, {"count": len(sols), "first": sols[:2]})
comp = [LAB.index(9 - LAB[v]) for v in range(8)]
ck("TI6_complement_is_translation_by_1", comp == [v ^ 1 for v in range(8)])
Jlab = {4: 7, 7: 4, 2: 5, 5: 2}
Jpos = [LAB.index(Jlab.get(LAB[v], LAB[v])) for v in range(8)]
ck("TI6_J_is_linear_transvection", all(Jpos[a ^ b] == Jpos[a] ^ Jpos[b] for a in range(8) for b in range(8)), Jpos)
inv = [fpos.index(v) for v in range(8)]
ck("TI6_JCJ_is_C_inverse", [Jpos[fpos[Jpos[v]]] for v in range(8)] == inv)

# TI7: transliteration radices
def order(b, p):
    k, x = 1, b % p
    while x != 1:
        x = x * b % p; k += 1
        if k > p: return None
    return k
isprime = lambda m: m > 1 and all(m % d for d in range(2, int(m ** .5) + 1))
tl = {}
for r in range(2, 9):
    p = (1 << r) - 1
    if not isprime(p):
        tl[r] = f"p={p} composite: no radix readout matches (units {sum(1 for u in range(1,p) if __import__('math').gcd(u,p)==1)} != {p-1})"
        continue
    bs = [b for b in range(2, 200) if b % p and order(b, p) == 2 * r]
    tl[r] = {"p": p, "radices_ord_2r": bs[:8], "decimal_ord": order(10, p)}
ck("TI7_r3_decimal_is_a_transliteration", order(10, 7) == 6, tl)

# TI8: transliteration identity.  On the 2^r words 0..2^r-1 (0 and p=2^r-1 kept as
# the two lifts of zero mod p), x -> p - rot_j(x) equals multiplication by -2^j mod p
# (with 0 <-> p).  In a normal basis of GF(2^r) (Frobenius = rotation, all-ones = 1)
# this map is z -> z^(2^j) + 1.
def rot(x, j, r): j %= r; return ((x << j) | (x >> (r - j))) & ((1 << r) - 1)
ti8 = {}
for r in range(3, 9):
    p = (1 << r) - 1
    ok = True
    for j in range(1, r):
        for x in range(p + 1):
            lhs = p - rot(x, j, r)
            if x in (0, p): rhs = p - x
            else:
                m = (-(1 << j) * x) % p
                rhs = m if m else p
            ok &= (lhs == rhs)
    g = PRIM.get(r)
    nb = None
    if g:
        N = 1 << r
        def tr(z):
            t, y = 0, z
            for _ in range(r): t ^= y; y = gmul(y, y, g, r)
            return t
        for beta in range(1, N):
            conj = [beta]
            for _ in range(r - 1): conj.append(gmul(conj[-1], conj[-1], g, r))
            if rank2(conj)[0] == r and tr(beta) == 1:
                phi = [reduce(lambda a, b: a ^ b, (conj[i] for i in range(r) if x >> i & 1), 0) for x in range(N)]
                good = all(phi[p - rot(x, 1, r)] == gmul(phi[x], phi[x], g, r) ^ 1 for x in range(N))
                nb = {"beta": beta, "z^2+1_in_normal_basis": good}; break
    fixed = [x for x in range(p + 1) if p - rot(x, 1, r) == x]
    ti8[r] = {"identity": ok, "normal_basis": nb, "fixed_words": fixed}
ck("TI8_rotate_complement_is_times_minus_2j", all(v["identity"] for v in ti8.values()), ti8)
ck("TI8_normal_basis_realizes_z2+1", all(v["normal_basis"]["z^2+1_in_normal_basis"] for v in ti8.values() if v["normal_basis"]))
ck("TI8_decimal_10_is_minus_4_mod_7", (10 + 4) % 7 == 0)
ck("TI8_hex_fixed_nibbles_are_thirds", ti8[4]["fixed_words"] == [5, 10] and (0x5, 0xA) == (15 // 3, 2 * 15 // 3),
   "hex 1/3=0.555..., 2/3=0.AAA...; decimal thirds give the wall digits 3,6,9")

# TI9: the decimal C6 phase cannot live in the 168-element group.  GL(3,2) element
# orders are {1,2,3,4,7}; the 142857 phase (order 6) needs the affine translation,
# i.e. the eighth coordinate (AGL(3,2), order 1344).  Corroborates CLOSURE_WEB L241-245.
from itertools import product as _prod
from collections import Counter
def _mul(a, b): return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) % 2 for j in range(3)) for i in range(3))
_I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
def _det(m): return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0]) + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])) % 2
_GL = [m for m in (tuple(tuple(v[3*i:3*i+3]) for i in range(3)) for v in _prod([0, 1], repeat=9)) if _det(m)]
def _ord(m):
    k, x = 1, m
    while x != _I: x = _mul(x, m); k += 1
    return k
_orders = Counter(_ord(m) for m in _GL)
ck("TI9_GL32_has_no_order_6", len(_GL) == 168 and 6 not in _orders, sorted(_orders.items()))
ck("TI9_atlas_phase_is_affine_not_linear", fpos[0] != 0, "the phase moves the origin: translation part nonzero")

# TI10: independent characterizations of r = 3 (radix-free), each checked on r = 2..12.
tau = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0)
chars = {
    "D(C)=C_perp (TI4)": [r for r in range(2, 13) if (1 << r) - 1 - r - 1 == r],   # dim D(C) = k-1 equals dual dim r
    "2(r+1)=2^r": [r for r in range(2, 13) if 2 * (r + 1) == 2 ** r],
    "tau(2^r-2)=2^r-1-r": [r for r in range(2, 13) if tau(2 ** r - 2) == 2 ** r - 1 - r],
    "z^2+1 single non-wall cycle (TI5)": [r for r in range(2, 13) if r % 2 and (2 ** r - 2) // (2 * r) == 1],
}
ck("TI10_characterizations_of_r3", all(v == [3] for v in chars.values()), chars)
# Honest dependency record: TI4 (dim D(C) = 2^r-r-2 = r), the single-cycle condition
# ((2^r-2)/(2r) = 1) and 2(r+1) = 2^r are ONE equation read three ways.  Only the
# divisor-count condition tau(2^r-2) = 2^r-1-r is an independent route.
ck("TI10_three_readings_are_one_equation",
   all(((2**r - r - 2 == r) == (2*(r+1) == 2**r) == ((2**r - 2) == 2*r)) for r in range(2, 64)))

# TI11: the Cosmic Pattern's radii (13,3) are one squeeze parameter tanh s = r/R = 3/13:
# cosh^2 = 1/(1-a^2) = 169/160, sinh^2 = a^2/(1-a^2) = 9/160 (RR-RELATIVE-DISK calibrated radius a).
from fractions import Fraction as _F
_a = _F(3, 13)
ck("TI11_cosmic_radii_are_one_disk_parameter", (1 / (1 - _a * _a), _a * _a / (1 - _a * _a)) == (_F(169, 160), _F(9, 160)))

if __name__ == "__main__":
    json.dump({"failures": FAIL, "results": OUT}, sys.stdout, indent=1, default=str)
    print()
    sys.exit(1 if FAIL else 0)
