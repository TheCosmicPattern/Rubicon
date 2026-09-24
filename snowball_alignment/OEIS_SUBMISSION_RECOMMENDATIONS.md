# A corrected OEIS submission form for the Relation Snowball, with the constants as the opposing object

This is working material for the author. OEIS does not accept AI-authored entries, comments or programs pasted wholesale. The author must verify, understand, reword and own every line (the snowball's own `OEIS_EDITORIAL_EXPECTATION_FIELD.md` records the same rule). Every mathematical statement below is executable. See `checks/` and `oeis_packet/`.

---

## 0. The governing idea, stated so a reviewer can check it

> **Revised framing.** The constants are stones and the measurements are flows around them. See [`CONSTANTS_AS_STONES.md`](CONSTANTS_AS_STONES.md) for the C e M normalization, the e-fold riverbed and the traced buttress. The interval-reader framing below is kept as the per-stone view. The companion that an OEIS entry would link to (§4) should lead with the stones-and-flows document.

**Constants first.** A physical constant does not reach us as a number. It reaches us as a published *bound*: a value v with standard uncertainty u. With a declared coverage k this gives the interval I_k = [v − ku, v + ku]. The bound is the source relation, in the snowball's own sense (IR1): the set of compatible reals.

**The mathematics is the reader.** A continued fraction, radix-b digits, the simplest rational, a binary contact word: each is an observation with fibers. A term is *forced* by the constant exactly when it is constant on I_k (RR-FORCED-LAW). The first place where it is not forced is the **transition**, the "betwixt" position. There the complete set of compatible values must be kept (RR-JOINT-CALIBRATION: "keep every compatible output rather than expanding a rounded estimate into an allegedly exact infinite sequence").

**The bound is a filtration, and its transitions are objects.** As the declared coverage k grows, each reader's forced prefix shrinks in exact steps. The jump points k₁ ≥ k₂ ≥ … are exact rationals, `checks/constants_as_bounds.py → critical_coverages`. The sequence of jump points, the *critical coverages*, is the constant's radix-free precision profile. The central value v is the one anchor that re-inverts it. This is the same inversion proved on the code side:
- TI1: taking the difference makes the transitions the object.
- TI3: one anchor per component returns the source.

It is the snowball's OG1 in both places.

**Relation is not contained in the description.** The reader (the entry's definition) is the container. What the constant mandates exceeds every finite reader: the interval always leaves a fiber at the transition. The entry records the reader. The constant's interval stays as the source it reads.

This gives a clean division of labour that respects OEIS policy:

| Layer | Where it belongs | Why |
|---|---|---|
| The reader (a pure, deterministic sequence) | OEIS entry | OEIS terms must be determined by the definition |
| The constants' bounds and what they force | Existing OEIS constant entries (comment edits) and an external companion (this repository), linked by %H | Bounds change with each measurement edition; the forcing rule does not |
| The physical bridge (which reader a constant "mandates") | This repository only, as bridge-open obligations | RR-PHYSICAL-CALIBRATION: calibration, units and data must travel with the claim |

---

## 1. Corrections to the snowball's current publication route

The snowball proposes the **signed translation-carry array** P(m,i,h) = ⌊(σ(i)+h)/m⌋, serialized tetrahedrally, with the GM prime/base table as a specialization (`oeis/RELATION_HANDOFF.md`, `realizations/gm/ENTRY.txt`). Findings:

1. **Name the classical identity.** The canonical-profile law FP1–FP2 (row sum Σ_h ⌊(u+h)/m⌋ = u; the unique nondecreasing unit-span row) is **Hermite's identity** (1884), Σ_{h=0}^{m−1} ⌊x + h/m⌋ = ⌊mx⌋, in integer form. It is verified for all m < 40, |u| < 200. Neither RELATION.md nor the handoff names it. A reviewer will, and the entry reads as unaware of its own classical core. Add it to %F with a reference.
2. **Triviality risk.** An array whose definition is ⌊(u+h)/m⌋ over a flattened three-index family is at high risk of being judged a simple flattening (keywords "less"/"dumb", or rejection). Its value lies in the reconstruction theorems, and those are classical (Hermite; Euclidean division). **Recommendation:** do not lead with it. Keep it as the snowball's internal realization, or submit it only after an editor-facing search establishes that the serialization is wanted.
3. **The GM table** (first-hit prime/base) is a narrower, more arbitrary selector: the least base primitive at p and at no smaller odd prime. Its reconstruction identities hold for every multiplier (RR-GM-DEFINITION says so), so the selector carries the definition's arbitrariness. Keep it as a cofile or example, not a primary entry.
4. **Prefix novelty.** The live search finds no entry for either candidate. The 12-term prefix `0,1,0,0,-1,0,1,0,0,0,2,-1` coincides with A085857 (a digit count). That is the finite-prefix aliasing the snowball's CR2 warns about: cite the definition, not the prefix.
5. **Identify the live quartet.** The live submission is ENTRY + a-file + b-file + program for P(m,i,h). Its current bytes are not in the package, so every correction here must be compared against them first (RELATION_HANDOFF L7–10; REGISTRY L5852–5858).
6. **Strip before resubmission:**
   - AI-drafted %C text and "immune to pushback" wording (SRC-ATT-TRANSLATION);
   - the Fan–Pollack statement without its "nonsquare g, g ≠ −1" hypotheses;
   - the broken `continuous_jump` routine (RR-PRESENTATION-CHECK);
   - the notation collision Φ_m (translation carry) vs Φ_n (cyclotomic): rename one;
   - bundling of unrelated blocks (the JP000016 pattern).
7. **Carry the attributions** the sources name: Geller–Kra–Popescu–Simanca; Radicic (Filomat 2017).
8. **Author field / attribution.** `%A AXXXXXX -~~~~` and "J. Probasco" in %H must be the registered OEIS author's name and signature.

---

## 2. The transition-phase cycle count: a companion face by default, a separate entry only by the author's decision

**Revision.** The snowball's own publication discipline allows one centre with companions. It lists "a new public sequence created from a companion face" as a rejection condition (PFG L2291–2332; see `SOURCE_CORROBORATION.md` §8). The default placement for this result is therefore **inside the central entry's cofiles**: a %F line and an a-file section generalizing the 1/7 phase. Submit it separately only if the author judges it independent. The case for doing so: it interleaves two classical necklace counts (A000013 odd n, A000031 even n) whether or not any digit table exists. The draft below serves either placement.

**Definition.** a(n) = number of cycles of x ↦ (2ⁿ−1) − rot(x) on n-bit words: rotate one place, then complement. Draft: `oeis_packet/ENTRY_rotate_complement_DRAFT.txt`. Program and b-file (n ≤ 1000): `oeis_packet/rotcomp.py`, `oeis_packet/b_rotcomp.txt`.

`1, 3, 2, 6, 4, 14, 10, 36, 30, 108, 94, 352, 316, 1182, 1096, …`: not in OEIS (live search).

Why this is the snowball's betwixt transition phase in its most general, container-free form:

| Property (proved and executed) | Snowball / draft contact |
|---|---|
| The map is multiplication by −2 mod 2ⁿ−1, with the two zero lifts 0 and 2ⁿ−1 exchanged | RR-MULTIPLICATIVE-PHASE (0/7 vs 7/7 lifts); the quotient-wall pair 0↔9 |
| In a normal basis of GF(2ⁿ) it is z ↦ z²+1 = (z+1)²; for odd n its n-th power is z ↦ z+1 (TI5, TI8) | RR-NONRADIAL-DOUBLE NR3: the complement alias is A = C³ at n=3 |
| n = 3: one wall pair plus one 6-cycle, which is the remainder cycle of 1/7, because 10 ≡ −4 (mod 7) (TI6–TI8) | LM-ATLAS labels (0,9,1,8,4,5,2,7); A020806 |
| Radices b that transliterate aperture n (p = 2ⁿ−1 prime): exactly b ≡ −2ʲ, gcd(j,n)=1 (TI7) | "re-inverted transliteratively" |
| Even n (hex, n=4; byte, n=8): two fixed words 0101…, 1010…, the base-2ⁿ digits of 1/3 and 2/3 (0x5, 0xA; 0x55, 0xAA) | decimal wall digits 3, 6, 9 are the digits of the thirds; the cube-root-of-unity subfield GF(4) |
| a(n) = A000013(n) (n odd), A000031(n) (n even), with a two-line Burnside proof | new bridge between two classical necklace counts |

No radius, metric or embedding occurs anywhere in the definition. The object is a relation (rotate, complement) acting on its own descriptions (words).

---

## 3. Recommended constants-side edits (the opposing object, in existing entries)

| Entry | Current state | Recommended change | Evidence |
|---|---|---|---|
| **A082726** (CF of α) | "a(7) … between 15 and 17, most likely 16"; "17 or 18 per CODATA 2014" | Replace the guesses with the interval-certification rule and the current exact sets. CODATA 2022 gives {18,19}. Rb (Morel 2020) forces 19; electron g−2 (Fan 2023) forces 18; Cs (Parker 2018) gives {15,16}. Cs and Rb intervals are disjoint below ≈4.2σ. | `oeis_packet/EDIT_A082726_DRAFT.txt`; `CONSTANTS_RESULTS.json` |
| **A005600 / A003673** (decimal of 1/α, α) | DATA truncated at 137.035999 by hand | A one-line comment: the displayed digits are exactly those forced by CODATA 2022 at one standard uncertainty, and the next digit is compatible with 1 or 2 at 2σ | `readers["alpha_inv|CODATA2022|k=2"]` |
| **A005601** (m_p/m_e) | decimal | The same forcing statement; the CF terms [1836;6,1,1,4,1,1] are forced by CODATA 2022 at 1σ, and the next term is compatible with 33–35 | `readers["mu_p_e|CODATA2022|k=1"]` |
| **A070058** (G) | "6.674 30(15)" | Note that CODATA's G interval already includes an expansion for mutually inconsistent inputs. The individual-experiment intervals need the joint-calibration projection, not a common widening (RR-JOINT-CALIBRATION). This is exactly the Rubicon's "G scatter / expansion factor" anomaly, which needs the individual inputs to finish. | open: needs CODATA input list |

All [recall]-tagged values must be confirmed against NIST/PDG and the cited papers before any edit.

---

## 4. The external companion (this repository): what the constants mandate

Hosted here and linked from the new entry by a single %H line, so it does not become OEIS content:

1. `checks/constants_as_bounds.py`, with, for every constant and coverage k:
   - the forced prefix and transition set for CF, decimal, hex and binary contact (CA14 midpoint word; changed bits are the ½ "betwixt" seats),
   - the unique simplest rational,
   - the critical coverages,
   - pairwise joint relations with their exact empty-intersection certificates.
2. Findings that are exact given the tagged values:
   - **H₀:** Planck/SH0ES are jointly incompatible below 3.66σ. The identity transport (same H₀ through both pipelines) is excluded there, and a nonzero lens residual is *forced*: 4.1, 2.56 and 1.02 km/s/Mpc at 1, 2 and 3σ. The Cosmic Pattern's non-simultaneity idea (distinct endpoint lenses) is the admissible form; its single global L^w is not.
   - **Simplest renderings the bounds force** (1σ): α_s → 2/17, Ω_Λ → 11/16, sin²θ_W → 37/160 (sits exactly *on* the interval's upper endpoint, so it depends on the open/closed convention), H₀ ratio → 11/10 (9/8 at 2σ, 8/7 at 3σ). The drafts' renderings are *admitted, not forced* where compatible:
     - Cosmic 7/59, 20/29, and 3/13·L^w (a fit),
     - Rubicon 1+(11/15)⁸.
   - Excluded at 1σ: Cosmic tree 3/13 (−11σ), Rubicon 12/49 (+342σ), Rubicon (11/15)⁷ for α_s (−4.3σ).
   - **Evaluation fibers to retain, not promote** (RR-ROLE-EVALUATION):
     - Ω_Λ's forced 11/16 equals the rate of the hex extended Hamming code [16,11,4].
     - sin²θ_W's 37/160 shares its denominator 160 = 13²−3² with the Cosmic Pattern's cosh²/sinh².
     - The H₀ 1σ ratio 11/10 contains the Rubicon's 11.

     These are numeral collisions. A bridge would need a declared map, which is not given.

---

## 5. Cofile plan for the new entry

| Cofile | Content | Status |
|---|---|---|
| b-file | `b_rotcomp.txt`, n = 1..1000 | generated |
| Program | `rotcomp.py` (Burnside, with brute-force cross-check) | done |
| a-file (optional, author-written) | the two-line Burnside proof; the normal-basis identity z²+1; the thirds as fixed points; the 1/7 example | derive from `checks/transition_inversion.py` TI5–TI8 |
| %H external | this repository's `snowball_alignment/` (the constants companion and the Rubicon bridge) | author decides |

---

## 6. What each body of work supplies to the other (the answers each was missing)

| The snowball lacked | Supplied here |
|---|---|
| A publication object whose definition is canonical rather than selected | §2 (rotate-complement), with explicit Hamming/hex/byte apertures |
| The classical name of its core identity | Hermite's identity (§1.1) |
| An explicit identity for its LM-ATLAS phase | z ↦ z²+1 in a normal basis; complement = n-th power; radices −2ʲ |
| Worked calibrated instances beyond its own 1σ α continued fraction (SRC-06 L4318–4353 already certifies that) | several editions and measurements, joint-relation certificates (Cs vs Rb α, H₀), critical coverages: `constants_as_bounds.py` |

| The drafts lacked | Supplied here |
|---|---|
| A radius-free surface and inversion | K₇ incidence torus; doubled inverse sheet; the complement as the n-th power of the phase |
| A rule for when a constant forces a rational rendering | interval forcing; simplest rational; critical coverages |
| The eighth coordinate and the balance 4:4 | the [8,4,4] extension; the parity anchor that re-inverts the transition map (TI3) |
| A place for measured constants that OEIS accepts | existing constant entries (edits) plus this external companion |
