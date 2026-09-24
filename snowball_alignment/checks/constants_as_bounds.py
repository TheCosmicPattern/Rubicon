#!/usr/bin/env python3
"""
Constants as the opposing object: what a measured constant's published bounds
FORCE under each reader, in exact rational arithmetic.

Premise (author's framing, made precise with RELATION.md):
  * The constant's measurement comes first. Its published interval
    I_k = [v - k*u, v + k*u] (declared coverage k) is the source relation:
    the set of compatible reals (RR-INTERACTION-RETURN IR1).
  * A reader (continued fraction, radix-b digits, simplest rational, binary
    contact word) returns its fiber over I_k. A term is FORCED (RR-FORCED-LAW)
    exactly when it is constant on I_k. The first unforced place is the
    transition ("betwixt"): the complete compatible set is retained there
    (RR-JOINT-CALIBRATION: "At a crossed boundary, keep every compatible output
    rather than expanding a rounded estimate into an allegedly exact infinite
    sequence").
  * Two measurements of "the same" constant jointly force it only on the
    intersection of their intervals. An empty intersection is the exact
    certificate that the identity transport between the two readings is NOT
    compatible at that coverage (RR-FORCED-LAW; RR-CONSTITUTION-RETURN
    distinct endpoint lenses G_d^-1(b) - G_c^-1(a)).
  * A window of one standard uncertainty is not a probability-one enclosure
    (RR-JOINT-CALIBRATION). The coverage k is therefore always declared.

PROVENANCE: values marked [OEIS] are copied from the cited OEIS records.
Values marked [recall] were entered from the author-assistant's memory of
CODATA/PDG/literature and MUST be confirmed against the primary source before
any external use. Nothing here fits a parameter.

Run: python3 constants_as_bounds.py > ../CONSTANTS_RESULTS.json
"""
import json, math, sys
from fractions import Fraction as Q

D = lambda s: Q(s)                     # exact decimal string -> rational

DATA = {
 "alpha_inv": [
   ("CODATA2014", "137.035999139", "0.000000031", "[OEIS] A082726 example"),
   ("CODATA2018", "137.035999084", "0.000000021", "[recall] NIST CODATA 2018"),
   ("CODATA2022", "137.035999177", "0.000000021", "[recall] NIST CODATA 2022"),
   ("Parker2018_Cs", "137.035999046", "0.000000027", "[recall] Parker et al., Science 360 (2018)"),
   ("Morel2020_Rb", "137.035999206", "0.000000011", "[OEIS] A005600 example, Morel et al. Nature 588 (2020)"),
   ("Fan2023_ge", "137.035999166", "0.000000015", "[recall] Fan et al., PRL 130 (2023)"),
 ],
 "mu_p_e": [
   ("CODATA2018", "1836.15267343", "0.00000011", "[recall] NIST CODATA 2018"),
   ("CODATA2022", "1836.152673426", "0.000000032", "[recall] NIST CODATA 2022"),
 ],
 "G_1e-11": [
   ("CODATA2018", "6.67430", "0.00015", "[OEIS] A070058 example"),
 ],
 "H0": [
   ("Planck2018", "67.4", "0.5", "[recall] Planck 2018 VI"),
   ("SH0ES2022", "73.04", "1.04", "[recall] Riess et al. ApJL 934 (2022)"),
 ],
 "sin2thetaW_MSbar": [("PDG2022", "0.23121", "0.00004", "[recall] PDG 2022")],
 "alpha_s_MZ": [("PDG2022", "0.1179", "0.0009", "[recall] PDG 2022")],
 "m_H_GeV": [("PDG2022", "125.25", "0.17", "[recall] PDG 2022")],
 "Omega_Lambda": [("Planck2018", "0.6847", "0.0073", "[recall] Planck 2018 VI")],
}

# ---------------------------------------------------------------- readers
def cf(x, n=40):
    """Continued fraction of a positive rational (canonical, last term > 1 unless single)."""
    out = []
    while len(out) < n:
        a = x.numerator // x.denominator
        out.append(a)
        f = x - a
        if f == 0: break
        x = 1 / f
    return out

def cf_certified(lo, hi):
    """Forced CF prefix on [lo,hi] and the complete compatible set at the first unforced place."""
    a, b = cf(lo), cf(hi)
    k = 0
    while k < min(len(a), len(b)) and a[k] == b[k]:
        k += 1
    # the partial quotient at place k is monotone on the common cylinder; all integers between are attained
    if k < len(a) and k < len(b):
        lo_k, hi_k = sorted((a[k], b[k]))
        compat = list(range(lo_k, hi_k + 1))
    else:
        compat = "endpoint is a convergent: both representations retained"
    return {"forced": a[:k], "transition_index": k, "compatible_at_transition": compat}

def digits(x, base, n):
    """Integer part (in base) and first n fractional digits of positive rational x."""
    ip = x.numerator // x.denominator
    f = x - ip
    ds = []
    for _ in range(n):
        f *= base
        d = f.numerator // f.denominator
        ds.append(d); f -= d
    return ip, ds

def radix_certified(lo, hi, base, n=64):
    il, dl = digits(lo, base, n); ih, dh = digits(hi, base, n)
    if il != ih:
        return {"integer_part_forced": False, "compatible_integer_parts": [il, ih]}
    k = 0
    while k < n and dl[k] == dh[k]: k += 1
    return {"integer_part": il, "forced_fraction_digits": dl[:k], "transition_index": k,
            "compatible_at_transition": list(range(dl[k], dh[k] + 1)) if k < n else None}

def simplest_rational(lo, hi):
    """Unique rational of least denominator (then least numerator) in closed [lo,hi] (Stern-Brocot)."""
    fl = lo.numerator // lo.denominator
    if Q(fl) == lo: return Q(fl)
    if fl + 1 <= hi: return Q(fl + 1)
    # lo, hi in (fl, fl+1): recurse on reciprocals of fractional parts
    return fl + 1 / simplest_rational(1 / (hi - fl), 1 / (lo - fl))

def contact_word(lo, hi, nbits=48):
    """CA14 midpoint contact of the two endpoint inscriptions (binary fractional bits):
    shared bits kept, changed bits become 1/2 (the 'betwixt' seats)."""
    _, bl = digits(lo, 2, nbits); _, bh = digits(hi, 2, nbits)
    word = "".join(str(x) if x == y else "½" for x, y in zip(bl, bh))
    k = next((i for i, (x, y) in enumerate(zip(bl, bh)) if x != y), nbits)
    return {"forced_bits": k, "contact_prefix": word[:min(nbits, k + 12)]}

def interval(v, u, k): return (D(v) - k * D(u), D(v) + k * D(u))

OUT = {"provenance_note": "values tagged [recall] require confirmation against the primary source",
       "readers": {}, "joint": {}, "draft_renderings": {}}

for name, rows in DATA.items():
    for label, v, u, src in rows:
        for k in (1, 2, 3):
            lo, hi = interval(v, u, k)
            key = f"{name}|{label}|k={k}"
            OUT["readers"][key] = {
                "source": src, "interval": [str(lo), str(hi)],
                "continued_fraction": cf_certified(lo, hi),
                "decimal": radix_certified(lo, hi, 10, 24),
                "hex": radix_certified(lo, hi, 16, 20),
                "binary_contact": contact_word(lo, hi),
                "simplest_rational": str(simplest_rational(lo, hi)),
            }

# ---------------------------------------------------------------- joint relations
def joint(name, a, b, ks=(1, 2, 3, 4, 5)):
    ra = next(r for r in DATA[name] if r[0] == a); rb = next(r for r in DATA[name] if r[0] == b)
    res = {}
    for k in ks:
        la, ha = interval(ra[1], ra[2], k); lb, hb = interval(rb[1], rb[2], k)
        lo, hi = max(la, lb), min(ha, hb)
        res[f"k={k}"] = ({"status": "compatible", "intersection": [str(lo), str(hi)]} if lo <= hi else
                         {"status": "NOT (empty joint relation)", "minimal_forced_residual": str(lo - hi)})
    kstar = (abs(D(ra[1]) - D(rb[1])) / (D(ra[2]) + D(rb[2])))
    res["coverage_where_identity_transport_first_compatible"] = float(kstar)
    return res

OUT["joint"]["alpha_inv Parker2018_Cs vs Morel2020_Rb"] = joint("alpha_inv", "Parker2018_Cs", "Morel2020_Rb")
OUT["joint"]["alpha_inv CODATA2018 vs CODATA2022"] = joint("alpha_inv", "CODATA2018", "CODATA2022")
OUT["joint"]["H0 Planck2018 vs SH0ES2022"] = joint("H0", "Planck2018", "SH0ES2022")
# the H0 ratio interval and its forced simplest rendering (what the bounds mandate, vs 1+(11/15)^8)
for k in (1, 2, 3):
    p = interval("67.4", "0.5", k); s = interval("73.04", "1.04", k)
    rlo, rhi = s[0] / p[1], s[1] / p[0]
    rub = 1 + Q(11, 15) ** 8
    OUT["joint"][f"H0 ratio SH0ES/Planck k={k}"] = {
        "ratio_interval": [float(rlo), float(rhi)], "simplest_rational": str(simplest_rational(rlo, rhi)),
        "rubicon_1+(11/15)^8": float(rub), "rubicon_compatible": rlo <= rub <= rhi}

# ---------------------------------------------------------------- draft renderings vs bounds
L = 13 / (13 + 3 * math.cos(6 * math.pi / 13))
render = {
 "alpha_inv": {"Cosmic tree 137": 137.0, "Cosmic 137*L^(-1/137)": 137 * L ** (-1 / 137),
               "Rubicon (225/44)^3": (225 / 44) ** 3},
 "sin2thetaW_MSbar": {"Cosmic tree 3/13": 3 / 13, "Cosmic 3/13*L^(-4/59)": 3 / 13 * L ** (-4 / 59),
                      "Rubicon 12/49": 12 / 49},
 "alpha_s_MZ": {"Cosmic tree 7/59": 7 / 59, "Cosmic 7/59*L^(39/196)": 7 / 59 * L ** (39 / 196),
                "Rubicon (11/15)^7": (11 / 15) ** 7},
 "Omega_Lambda": {"Cosmic 20/29": 20 / 29},
 "m_H_GeV": {"Cosmic 124.9*L^(-3/31)": 124.9 * L ** (-3 / 31)},
}
for name, cands in render.items():
    label, v, u, _ = DATA[name][-1] if name != "alpha_inv" else DATA[name][2]
    for cn, val in cands.items():
        OUT["draft_renderings"][f"{name}|{cn}"] = {
            "value": val, "against": label,
            "pulls_sigma": round((val - float(D(v))) / float(D(u)), 3),
            "status": "compatible at 1 sigma (N'T: admitted, not forced)" if abs(val - float(D(v))) <= float(D(u))
                      else "outside 1 sigma"}
    lo, hi = interval(v, u, 1)
    OUT["draft_renderings"][f"{name}|FORCED simplest rational at 1 sigma"] = str(simplest_rational(lo, hi))

# ---------------------------------------------------------------- critical coverages
# The constant's bound is a filtration I_k (k = declared coverage). A reader's forced
# prefix is a nonincreasing step function of k; its jump points are exact rationals:
#   k_j = dist(v, boundary of the depth-j cylinder of v) / u.
# Inverting the transitions into objects: the sequence (k_1 >= k_2 >= ...) is the
# constant's radix-free precision profile; the central value v is the anchor that
# re-inverts it (cf. TI3 / OG1: one anchor per component).
def cf_eval(prefix, tail):
    x = tail
    for a in reversed(prefix):
        x = a + (1 / x if x is not None else 0) if x is not None else Q(a)
    return x

def cylinder(prefix):
    """Interval of reals whose CF begins with `prefix` (endpoints: tail -> infinity and tail = 1)."""
    e1 = Q(prefix[0]) if len(prefix) == 1 else cf_eval(prefix[:-1], Q(prefix[-1]))
    p2 = prefix[:-1] + [prefix[-1] + 1]
    e2 = Q(p2[0]) if len(p2) == 1 else cf_eval(p2[:-1], Q(p2[-1]))
    return min(e1, e2), max(e1, e2)

def critical_coverages(v, u, depth=12):
    a = cf(v, depth + 1)
    ks = []
    for j in range(1, min(depth, len(a)) + 1):
        lo, hi = cylinder(a[:j])
        ks.append(min(v - lo, hi - v) / u)
    return a[:len(ks)], ks

def radix_critical(v, u, base, depth=16):
    ks = []
    for j in range(depth):
        w = Q(base) ** (-j)
        lo = (v // w) * w
        ks.append(min(v - lo, lo + w - v) / u)
    return [float(x) for x in ks]

OUT["critical_coverages"] = {}
for name, rows in DATA.items():
    for label, v, u, src in rows:
        terms, ks = critical_coverages(D(v), D(u))
        OUT["critical_coverages"][f"{name}|{label}"] = {
            "cf_terms": terms, "k_j": [float(x) for x in ks],
            "cf_depth_forced_at_k=1": sum(1 for x in ks if x >= 1),
            "decimal_k_j": radix_critical(D(v), D(u), 10, 14),
            "hex_k_j": radix_critical(D(v), D(u), 16, 12)}

# endpoint hits: a forced object lying exactly on an interval endpoint depends on the
# closed/open convention (RR-INTEGER-ATTAINMENT: open endpoints use strict bounds)
OUT["endpoint_hits"] = {}
for key, rec in OUT["readers"].items():
    s = Q(rec["simplest_rational"]); lo, hi = map(Q, rec["interval"])
    if s in (lo, hi):
        OUT["endpoint_hits"][key] = f"simplest rational {s} equals an endpoint: convention-dependent"

if __name__ == "__main__":
    json.dump(OUT, sys.stdout, indent=1, default=str); print()
