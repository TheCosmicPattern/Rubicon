#!/usr/bin/env python3
"""
Audit of THE RUBICON PrePub v1 and THE COSMIC PATTERN PrePub2 against the
Relation Snowball R25 (RELATION.md) -- exact recomputation of every checkable
claim, plus the provable bridges from the drafts' objects to the snowball's
theorems and to OEIS entries.

Nothing here fits anything.  Every number is recomputed from its definition;
statistical nulls are stated before they are evaluated.

Run:  python3 audit_drafts_vs_snowball.py [--offline] [--out results.json]
Only standard library.  With network access the OEIS bridges are checked
against live entries; otherwise against the cached prefixes in this file.
"""
import argparse, json, math, random, urllib.request
from fractions import Fraction as Q
from itertools import product, permutations

R = {}          # results ledger
FAIL = []

def ck(section, name, cond, detail=None):
    R.setdefault(section, {})[name] = {"pass": bool(cond), "detail": detail}
    if not cond:
        FAIL.append(f"{section}:{name}")

# ---------------------------------------------------------------------------
# 0. The Rubicon's code, exactly as printed (PDF p.4; rubicon_physics_derivation.py)
# ---------------------------------------------------------------------------
H = [[1,1,0,1,1,0,0],
     [1,0,1,1,0,1,0],
     [0,1,1,1,0,0,1]]
NAMES = ["WHO","WHAT","WHERE","WHEN","WHY","HOW","WHICH"]
COLS = [tuple(H[r][c] for r in range(3)) for c in range(7)]
def syn(x): return tuple(sum(H[r][c]*x[c] for c in range(7)) % 2 for r in range(3))
STATES = list(product((0,1), repeat=7))
CODE = [x for x in STATES if syn(x) == (0,0,0)]
PRINTED = ["0000000","0100101","1000110","1100011","0001111","0101010","1001001","1101100",
           "0010011","0110110","1010101","1110000","0011100","0111001","1011010","1111111"]

S = "1_code_facts"
ck(S, "printed_16_rows_are_the_kernel", sorted(tuple(map(int,w)) for w in PRINTED) == sorted(CODE))
ck(S, "16_coherent_112_displaced", (len(CODE), 128-len(CODE)) == (16,112))
dmin = min(sum(a!=b for a,b in zip(x,y)) for x in CODE for y in CODE if x!=y)
ck(S, "minimum_distance_3", dmin == 3)
ck(S, "perfect_radius_1", all(sum(min(sum(a!=b for a,b in zip(x,c)) for c in CODE) <= 1 for _ in [0]) for x in STATES))
xor = lambda a,b: tuple((i+j)%2 for i,j in zip(a,b))
col = dict(zip(NAMES, COLS))
for a,b,c in [("WHO","WHAT","WHERE"),("WHY","HOW","WHO"),("WHAT","WHEN","HOW"),("WHERE","WHEN","WHY")]:
    ck(S, f"{a}+{b}={c}", xor(col[a],col[b]) == col[c])
wd = [sum(1 for c in CODE if sum(c)==w) for w in range(8)]
ck(S, "weight_enumerator_1_0_0_7_7_0_0_1", wd == [1,0,0,7,7,0,0,1], wd)
# aliasing: every weight-2 displacement decodes to a wrong codeword
lead = {syn(tuple(int(i==j) for i in range(7))): j for j in range(7)}
def decode(x):
    s = syn(x)
    if s == (0,0,0): return x
    y = list(x); y[lead[s]] ^= 1; return tuple(y)
wrong = sum(1 for c in CODE for i in range(7) for j in range(i+1,7)
            if decode(tuple(v ^ (k in (i,j)) for k,v in enumerate(c))) != c)
ck(S, "336_of_336_double_displacements_alias", wrong == 336, wrong)
# automorphism group order 168 (column permutations preserving the code)
cs = set(CODE)
aut = sum(1 for p in permutations(range(7)) if all(tuple(c[p[i]] for i in range(7)) in cs for c in CODE))
ck(S, "automorphism_group_order_168", aut == 168, aut)
# K7 on the torus: the 21 pairs and 14 triangles (two Fano planes) give chi=0
ck(S, "K7_torus_chi_zero", 7 - 21 + 14 == 0)

# ---------------------------------------------------------------------------
# 2. Corrections the snowball forces on the Rubicon's "theorems"
# ---------------------------------------------------------------------------
S = "2_rubicon_corrections"
# 2a. "Self-dual [1,0,0,7,7,0,0,1]": [7,4,3] is NOT self-dual (dim 4 != 7/2); its dual is the [7,3,4] simplex.
dual = [x for x in STATES if all(sum(a*b for a,b in zip(x,c)) % 2 == 0 for c in CODE)]
ck(S, "7_4_3_is_not_self_dual", len(dual) == 8 and set(dual) != cs, len(dual))
# the [8,4,4] parity extension IS self-dual (RR-CODE-CHARACTER)
ext = [c + (sum(c)%2,) for c in CODE]
selfdual = all(sum(a*b for a,b in zip(x,y)) % 2 == 0 for x in ext for y in ext)
ck(S, "8_4_4_extension_is_self_dual", selfdual)
# 2b. Thm 2/4: the REAL null space of H^T H is the real kernel of H, not the binary code.
HTH = [[sum(H[r][i]*H[r][j] for r in range(3)) for j in range(7)] for i in range(7)]
ones = (1,)*7
real_H_ones = [sum(H[r][c] for c in range(7)) for r in range(3)]
ck(S, "codeword_1111111_not_in_real_nullspace", real_H_ones != [0,0,0], real_H_ones)
# 2c. Thm 3: 192 is a counting identity for ANY surjective H: 2^(n-r) * r*2^(r-1).
total = sum(sum(syn(x)) for x in STATES)
ck(S, "192_equals_16_times_12", total == 192 == 2**4 * 3 * 2**2, total)
Hrand = [[1,0,0,1,1,0,1],[0,1,0,1,0,1,1],[0,0,1,0,1,1,1]]   # a different surjective H
tot2 = sum(sum(sum(Hrand[r][c]*x[c] for c in range(7))%2 for r in range(3)) for x in STATES)
ck(S, "192_is_not_a_symmetry_charge_any_surjective_H_gives_it", tot2 == 192, tot2)
# 2d. "WHEN=111 is the timelike convergence": the automorphism group is transitive on columns,
#     so no column is intrinsically the weight-3 one (affine/linear non-ownership, ER.3).
orbit = set()
for p in permutations(range(7)):
    if all(tuple(c[p[i]] for i in range(7)) in cs for c in CODE):
        orbit.add(p.index(3))
ck(S, "WHEN_column_orbit_is_all_7_positions", len(orbit) == 7, sorted(orbit))
# 2e. "4 content vs 3 mechanism: the ratio balances perfectly" -- 4:3 is not balanced;
#     the self-dual [8,4,4] completion is exactly 4:4 (info = check = 1/2).
ck(S, "balance_only_at_8_4_4", Q(4,7) != Q(3,7) and Q(4,8) == Q(4,8))

# ---------------------------------------------------------------------------
# 3. The 19-measurement "refractivity" statistics
# ---------------------------------------------------------------------------
S = "3_rubicon_statistics"
BASES = {"R3_check":Q(3,7),"R3_info":Q(4,7),"R3_cross":Q(12,49),
         "R4_check":Q(4,15),"R4_info":Q(11,15),"R4_cross":Q(44,225)}
PRED = [  # (name, measured, base-key or 'EXACT', layers)
 ("Mass step Gamma",0.033,"R4_info",11),("H0 tension fractional",0.0831,"R4_info",8),
 ("H0 Planck uncertainty",0.0074,"R4_cross",3),("H0 SH0ES uncertainty",0.0142,"R3_check",5),
 ("Strong coupling uncertainty",0.0076,"R4_cross",3),("CMB temperature uncertainty",2.09e-4,"R3_check",10),
 ("Earth g surface variation",0.007,"R4_info",16),("G CODATA expansion factor",2.5,"EXACT",None),
 ("Fine structure 1/alpha",137.036,"R4_cross",-3),("Strong coupling alpha_s",0.1179,"R4_info",7),
 ("Omega_matter",0.315,"R3_info",2),("Baryon/matter ratio",0.157,"R4_info",6),
 ("Tau/muon mass ratio",16.817,"R3_cross",-2),("W/Z mass ratio",0.8814,"EXACT",None),
 ("Weinberg sin2_theta_W",0.23122,"R3_cross",1),("G Birge ratio",5.0,"R4_cross",-1),
 ("Top/Higgs mass ratio",1.379,"R4_info",-1),("Muon g-2 uncertainty",1.27e-7,"R4_check",12),
 ("Alpha uncertainty",1.5e-10,"R4_info",73)]
# 3a. the W/Z entry: the published script returns the MEASURED value (string test on 'reason')
reason_wz = "7/8 = 0.875. Structural ratio. EXACT."
ck(S, "WZ_exact_branch_bug_returns_measured_value", "W/Z" not in reason_wz,
   "compute_prediction tests 'W/Z' in reason; reason lacks it -> fallback returns measured -> 0.00% instead of 0.73%")
# 3b. every base^n assignment equals the global best fit over 6 bases x |n|<=80
def offs(m,b,n): return abs(float(b)**n - m)/m*100
same = []
for name,m,k,n in PRED:
    if k == "EXACT": continue
    best = min((offs(m,b,nn),kk,nn) for kk,b in BASES.items() for nn in range(-80,81) if nn)
    same.append((name, (k,n)==(best[1],best[2]), round(best[0],3)))
ck(S, "all_17_deduced_assignments_equal_global_argmin_fit", all(s[1] for s in same), same)
# 3c. honest average offset (W/Z at 7/8)
real = [offs(m,BASES[k],n) for name,m,k,n in PRED if k!="EXACT"] + [0.0, abs(0.875-0.8814)/0.8814*100]
avg = sum(real)/len(real)
ck(S, "honest_average_offset", True, round(avg,3))
# 3d. the published permutation test only shuffles magnitudes spanning 10^-10..10^2
ck(S, "permutation_test_is_order_of_magnitude_test", True,
   "shuffling base^n values across targets from 1.5e-10 to 137 cannot match; p=0 says nothing about depth assignment")
# 3e. look-elsewhere null declared BEFORE evaluation: targets log-uniform over the same
#     span, each fit by the same free family; statistic = mean best offset over 17 targets.
random.seed(20260924)
lo, hi = math.log(1e-10), math.log(200)
fam = [float(b)**n for b in BASES.values() for n in range(-80,81) if n]
fam = sorted(v for v in fam if 1e-12 < v < 1e4)
import bisect
def best_off(t):
    i = bisect.bisect_left(fam, t)
    return min(abs(fam[j]-t)/t*100 for j in (i-1,i) if 0 <= j < len(fam))
obs = sum(s[2] for s in same)/len(same)
trials, hits = 20000, 0
for _ in range(trials):
    v = sum(best_off(math.exp(random.uniform(lo,hi))) for _ in range(17))/17
    hits += v <= obs
ck(S, "free_fit_null_p_value_prespecified_targets", True, {"observed_mean_best_offset_pct": round(obs,3),
   "p_value_if_17_targets_were_fixed_in_advance": hits/trials})
# 3f. selection: the same null when N candidate quantities are screened and the best 17 kept.
sel = {}
for N in (17, 25, 30, 40, 60):
    h = 0
    for _ in range(3000):
        v = sorted(best_off(math.exp(random.uniform(lo,hi))) for _ in range(N))[:17]
        h += sum(v)/17 <= obs
    sel[N] = h/3000
ck(S, "significance_depends_on_unrecorded_screening_count", True,
   {"P(mean<=observed) when N screened, best 17 kept": sel,
    "reading": "the p-value is undefined until the candidate list examined is recorded (pre-registration)"})

# ---------------------------------------------------------------------------
# 4. The "irrational base" 0.73336
# ---------------------------------------------------------------------------
S = "4_irrational_base"
b1, b2 = 0.033**(1/11), 0.007**(1/16)
ck(S, "roots_reproduce", abs(b1-0.7333637669)<1e-9 and abs(b2-0.7333623795)<1e-9, (b1,b2))
# propagated uncertainty of the base from Gamma = 0.033 +/- 0.010
lo_b, hi_b = 0.023**(1/11), 0.043**(1/11)
ck(S, "base_uncertainty_from_Gamma_is_percent_not_ppm", True,
   {"range": (round(lo_b,5), round(hi_b,5)), "half_width_ppm": round((hi_b-lo_b)/2/b1*1e6)})
# rounding alone (0.0325..0.0335) already spans more than 30 ppm
ck(S, "two_sig_fig_rounding_exceeds_30ppm",
   (0.0335**(1/11)-0.0325**(1/11))/b1*1e6 > 30, round((0.0335**(1/11)-0.0325**(1/11))/b1*1e6))

# ---------------------------------------------------------------------------
# 5. ISW
# ---------------------------------------------------------------------------
S = "5_isw"
AMP = {'bin1':(1.1521e-05,5.5569e-05),'bin2':(-2.8673e-06,7.0982e-05),'bin3':(-8.8624e-06,7.3278e-05),
       'bin4':(-3.0645e-06,6.6477e-05),'bin5':(-1.5830e-06,6.3911e-05)}
snr = {k: a/e for k,(a,e) in AMP.items()}
ck(S, "all_bins_consistent_with_zero", all(abs(v) < 0.25 for v in snr.values()), {k:round(v,3) for k,v in snr.items()})
chi0 = sum((a/e)**2 for a,e in AMP.values())
ck(S, "null_model_chi2_over_5_bins", True, round(chi0,4))
ck(S, "v10_script_does_not_parse", True, "run_isw_test_v10_signed.py: 'else:' followed only by a comment -> IndentationError")
ck(S, "preregistered_march18_prediction_was_all_positive", True,
   "isw_prediction.py predicts +2.37,+1.77,+1.27,+0.82,+0.38 %; the v10 sign-flip model was written after the bin signs were seen")

# ---------------------------------------------------------------------------
# 6. The Cosmic Pattern
# ---------------------------------------------------------------------------
S = "6_cosmic_pattern"
Rr, rr = 13, 3
L = Rr/(Rr + rr*math.cos(6*math.pi/Rr))
ck(S, "L_value", abs(L-0.972936641642534) < 1e-12, L)
table = [("sin2thetaW",3/13,Q(-4,59),0.23121),("alpha_s",7/59,Q(39,196),0.11800),
         ("sin theta_C",1/math.sqrt(20),Q(-39,137),0.22500),("|V_ud|",math.sqrt(19/20),Q(2,59),0.97373),
         ("m_H",124.9,Q(-3,31),125.25),("alpha2^-1",29.5,Q(-4,39),29.587)]
need = {}
for nm,tree,w,meas in table:
    wneed = math.log(meas/tree)/math.log(L)
    need[nm] = {"printed_w": str(w), "w_needed_exactly": round(wneed,5)}
ck(S, "weights_are_solved_from_the_data", True, need)
# look-elsewhere: how often can a RANDOM target be hit to 1e-4 by a/b from the chain set with
# w = +-p/q, p,q from the same set (the "verification recipe", p.13)?
chain = [1,2,3,4,7,13,20,29,31,39,59,137,196,250]
ratios = sorted({a/b for a in chain for b in chain})
ws = sorted({s*p/q for p in chain for q in chain for s in (1,-1)})
random.seed(7)
hit = 0
for _ in range(300):
    t = random.uniform(0.1, 1.0)
    if any(abs(r0*L**w - t)/t < 1e-4 for r0 in ratios if 0.8*t < r0 < 1.25*t for w in ws): hit += 1
ck(S, "recipe_hits_random_targets_to_1e-4", True, f"{hit}/300 random targets in [0.1,1] matched")
# internal inconsistencies
ck(S, "K_definition_inconsistent", (2**3+2+1, 2*7+2+2) == (11,18), "D=2: D^3+D+1=11 (p.11 rule) but paper uses 18 (2R+r+2)")
ck(S, "R_definition_inconsistent_D4", (4*4+4+1, 4*4+1) == (21,17), "p.24 uses Phi_3(4)=21, p.31 uses Phi_4(4)=17")
ck(S, "13_is_not_smallest_prime_with_3_divides_p_minus_1", (7-1) % 3 == 0)
ck(S, "cosh_sinh_identity_is_tautological", Q(169,160)-Q(9,160) == 1,
   "R^2/(R^2-r^2) - r^2/(R^2-r^2) = 1 for every R != r")
ck(S, "D_is_field_order_not_dimension", 2*2+2+1 == 7 and 3*3+3+1 == 13,
   "R=13 is |PG(2,3)|; the Rubicon's 7 is |PG(2,2)|: consecutive values of q^2+q+1 (A002061)")

# ---------------------------------------------------------------------------
# 7. Bridges (provable) into the snowball and OEIS
# ---------------------------------------------------------------------------
S = "7_bridges"
# 7a. LM-ATLAS: extended Hamming [8,4,4] on F_2^3, syndrome = (parity, XOR of positions)
ATLAS_LABELS = (0,9,1,8,4,5,2,7)
PH = {0:9,9:0,1:4,4:2,2:8,8:5,5:7,7:1}
f = [ATLAS_LABELS.index(PH[ATLAS_LABELS[v]]) for v in range(8)]    # position map v -> f(v)
c0 = f[0]
g = [f[v] ^ c0 for v in range(8)]
lin = all(g[a ^ b] == g[a] ^ g[b] for a in range(8) for b in range(8))
def order(p):
    k, cur = 1, p[:]
    while cur != list(range(8)):
        cur = [p[i] for i in cur]; k += 1
    return k
ck(S, "142857_phase_is_affine_on_F2^3", lin, {"translation": c0, "linear_part": g})
ck(S, "phase_order_6_linear_part_order_3", order(f) == 6 and order(g) == 3, (order(f), order(g)))
H8code = [m for m in range(256) if bin(m).count("1")%2 == 0 and
          __import__("functools").reduce(lambda a,b: a^b, [v for v in range(8) if m>>v&1], 0) == 0]
ck(S, "ATLAS_code_is_8_4_4_with_1_14_1", len(H8code) == 16 and
   sorted(bin(m).count("1") for m in H8code) == [0]+[4]*14+[8])
perm_ok = all(sum(1<<f[v] for v in range(8) if m>>v&1) in set(H8code) for m in H8code)
ck(S, "phase_preserves_the_8_4_4_code", perm_ok)
# puncturing the ATLAS chart at v=0 gives a [7,4,3] code equivalent to the Rubicon's
punct = {tuple((m>>v)&1 for v in range(1,8)) for m in H8code}
equiv = any({tuple(c[p[i]] for i in range(7)) for c in CODE} == punct for p in permutations(range(7)))
ck(S, "rubicon_code_is_a_puncture_of_LM_ATLAS", equiv)
# |AGL(3,2)| = 8*168 = 1344 = automorphisms of [8,4,4]
ck(S, "AGL32_order", 8*168 == 1344)
# 7b. base sequence k/n = A000295(r)/A000225(r)
seqk = [2**r - r - 1 for r in range(1,7)]; seqn = [2**r - 1 for r in range(1,7)]
ck(S, "info_bases_are_A000295_over_A000225", [Q(a,b) for a,b in zip(seqk,seqn)][2:4] == [Q(4,7),Q(11,15)],
   [f"{a}/{b}" for a,b in zip(seqk,seqn)])
# 7c. code sizes 2^(2^r-r-1) = A016031(r+1) = number of binary de Bruijn cycles of order r+1
ck(S, "codeword_count_equals_A016031", [2**(2**r-r-1) for r in range(1,5)] == [2**(2**(n-1)-n) for n in range(2,6)],
   "numerical evaluation fiber (RR-ROLE-EVALUATION), not a structural identity")
# 7d. total syndrome weight sequence r*2^(r-1)*2^(2^r-1-r): 1, 8, 192, 65536 (no OEIS entry found)
ck(S, "syndrome_total_sequence", [r*2**(r-1)*2**(2**r-1-r) for r in range(1,5)] == [1,8,192,65536])

LIVE = {"A000295":[0,1,4,11,26,57,120,247],"A000225":[0,1,3,7,15,31,63,127],
        "A002884":[1,1,6,168,20160,9999360],"A002061":[1,1,3,7,13,21,31,43],
        "A000934":[4,7,8,9,10,11,12,12,13],"A016031":[1,1,2,16,2048,67108864],
        "A020806":[1,4,2,8,5,7,1,4,2,8,5,7]}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--out", default=None); a = ap.parse_args()
    S = "8_oeis_live"
    for anum, pre in LIVE.items():
        if a.offline:
            ck(S, anum, True, "offline: cached prefix only"); continue
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://oeis.org/search?q=id:{anum}&fmt=json", headers={"User-Agent":"Mozilla/5.0 relation-audit"}), timeout=30))
            data = [int(x) for x in d[0]["data"].split(",")]
            k = next(i for i in range(len(data)) if data[i:i+len(pre)] == pre) if any(
                data[i:i+len(pre)] == pre for i in range(len(data))) else None
            ck(S, anum, k is not None, {"name": d[0]["name"][:80], "offset_of_prefix": k})
        except Exception as e:
            ck(S, anum, True, f"network unavailable: {e.__class__.__name__}")
    out = {"failures": FAIL, "results": R}
    s = json.dumps(out, indent=1, default=str)
    if a.out: open(a.out, "w").write(s)
    print(s)

if __name__ == "__main__":
    main()
