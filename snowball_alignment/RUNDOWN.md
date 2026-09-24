# Rundown: The Rubicon repository vs. the Relation Snowball (R25)

Scope. This document compares four things:
- the state of this repository (THE RUBICON prepub staging area),
- the attached earlier draft THE COSMIC PATTERN (PrePub2),
- the later snowball package "Russels' Relation / Relation amongst offset", R25,
- the mathematics derived here where the three meet.

Every mathematical statement is executable. `checks/` holds the scripts; the `*_RESULTS.json` files hold their outputs.

Companion files:
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md): every draft claim, with status, snowball contact and repair.
- [`OEIS_SUBMISSION_RECOMMENDATIONS.md`](OEIS_SUBMISSION_RECOMMENDATIONS.md): the corrected publication form.
- [`oeis_packet/`](oeis_packet/): draft entry, b-file, program, and the proposed A082726 edit.

---

## 1. What is in the repository now

| Item | State | Notes |
|---|---|---|
| `THE_RUBICON_PrePubv1.pdf` (25 pp., Mar 20 2026) | Pre-snowball draft | [7,4,3] Hamming/Fano core; "refractive bases" 4/7, 11/15, …; 19-measurement test; nine "theorems"; inverted torus T²(13,3); signed ISW |
| `experiment_corrected.py` | Runs | Differs from the PDF's Appendix A: a permutation test replaces the base^n Monte Carlo. **Bug:** the W/Z entry never matches its "exact" branch and returns the measured value (0.00 % shown instead of 0.73 %) |
| `isw_prediction.py` | Runs | The genuine pre-registered prediction (Mar 18): +2.37 % … +0.38 % ISW enhancement, all positive |
| `run_isw_test_v10_signed.py` | **Does not parse** | An `else:` is followed only by a comment. Its sign-flip model was written after the bin signs were seen (the docstring states them) |
| `rubicon_physics_derivation.py` | Runs | Computes the nine "theorems"; see §4 |
| README | Data note | Planck SMICA + DESI DR1 (~50 GB) needed for the ISW run |
| PDF appendix | Layout duplication | Pages 20–22 repeat blocks of the derivation script |

The snowball package verifies itself. `verify.py` gives **PASS**: 855,288 mathematical assertions over 22 suites, and it regenerates `evidence/RESULT.json` byte-identically.

---

## 2. What changed between the drafts and the snowball

Both drafts start from a **container**, a torus with radii (R, r) = (13, 3), and then add abstract topology to counterbalance it. The Rubicon draft gets its "inverted torus" and "(1,3) knot" this way; the Cosmic Pattern gets its lens L = R/(R + r cos(6π/R)). The snowball starts from **relation**:

- RR-LAW: "No fixed carrier, radix, arity, radial origin or external observer defines the general relation."
- RR-H-RETURN: an observation H has a complete inverse fiber. The part left outside a section is a residual, "not an error by definition". The Rubicon's founding sentence, "We call it error; the Cosmos calls it remainder", is this theorem.
- RR-NONRADIAL-DOUBLE: inward/outward is a doubled inverse sheet (C, C⁻¹) joined by a reflection J with JCJ = C⁻¹. "No metric, center, radius or spherical embedding occurs."
- RR-CONSTITUTION-RETURN: the **only** place a placement-dependent geometry is required is a **nonlinear lens**. A placed displacement is (G(p), G(p+δ) − G(p)), not G(δ), and distinct endpoint lenses give G_d⁻¹(b) − G_c⁻¹(a). RR-RELATIVE-DISK: a radius appears only as a lens's *calibrated* parameter.

This is the author's "topographical neutrality except in lensing", as an existing theorem. The source history confirms the reclassification. ATT-C records that the "[7,4,3] Hamming torsor coordinates … were initially conflated with the parent object. They are now recognized as typed source maps (specific discrete apertures) rather than the definition of the arithmetic itself."

**Hamming as an aperture without a container.** The code is defined by a relation alone: a set of positions whose labels sum to zero. The description (the parity map H, the reader) is the container; what it cannot contain is the fiber over each reading. The relation is not in the description. It is the countercorrelary of all the descriptions taken jointly (IR1, RR-COUNTER).

---

## 3. New mathematics (not stated in the zip or in either draft)

All of the following are machine-checked in `checks/transition_inversion.py`, for r = 3…7 plus the reciprocal r = 3 chart.

**TI1: transitions as the object.** Let D(w) = w ⊕ shift(w), multiplication by (1+x). D maps the cyclic Hamming code C_r onto its even-weight subcode. The kernel is exactly {0, all-ones}.

**TI2: syndrome action.** syn(Dw) = α^{Z(1)} · syn(w), where Z is the Zech logarithm. The transition operator rotates the nonzero syndromes, i.e. the points of PG(r−1, 2). The step depends on the chart (3 or 5 for the two reciprocal cubics at r = 3; 4 at hex). The cycle it generates does not.

**TI3: re-inversion.** (Dw, parity(w)) is lossless. The class D loses is named by exactly one anchor bit, the eighth coordinate of the [8,4,4] extension (the snowball's WAY/whole-return seat). This is OG1 ("a difference loses one common level per component; one anchor returns it"), realized on the code.

**TI4: object = description only at seven.** D(C_r) equals the dual code C_r^⊥ if and only if r = 3. Equivalently, the extension is self-dual only at r = 3.
- r = 3 is the fixed point where the contained and its description coincide.
- From hex onward, the relation's dimension 2^r − r − 1 outgrows its description r without bound. This is the boundless open field, in exact form.

**TI5–TI8: the transition phase is z ↦ z² + 1.**
- In the snowball's own LM-ATLAS chart, the 142857 phase (with 0↔9) is exactly z ↦ z² + 1 over GF(8). There are 6 compatible field identifications.
- On r-bit words it is "rotate, then complement", which is multiplication by −2 mod 2^r − 1. Decimal is the case r = 3 because 10 ≡ −4 (mod 7).
- For odd r, the r-th power is z + 1, the complement half-turn. At r = 3 this is NR3's A = C³.
- The phase is a single cycle outside the wall pair if and only if r = 3.
- Transliterating radices are exactly b ≡ −2ʲ (mod 2^r − 1).
- At even r (hex, byte) the fixed points are 0101…, 1010…: the base-2^r digits of 1/3 and 2/3 (0x5, 0xA; 0x55, 0xAA). These are the analogues of decimal's wall digits 3, 6, 9.
- NR4's reflection J is a linear transvection.

**Cycle-count sequence (new to OEIS).** The number of cycles of this phase on r-bit words is 1, 3, 2, 6, 4, 14, 10, 36, … It equals A000013(r) for odd r and A000031(r) for even r (Burnside; checked to r = 200).

**Radius-free surface.** The complete graph K₇ triangulates the torus with 7 vertices, 21 edges and 14 faces, so χ = 0. The 14 faces split into two Fano planes. The torus the drafts reach for is incidence-derived (IT2) and needs no radii.

---

## 4. The Rubicon draft against the snowball (summary; full detail in the ledger)

**Forced (true as mathematics):**
- 16/112/128 states, d = 3, perfect radius 1;
- the 336 aliasing double displacements;
- automorphism group of order 168 (enumerated);
- the XOR interaction lines;
- weight enumerator 1,0,0,7,7,0,0,1;
- the [15,11,3] and PG(3,2) facts;
- χ(K₇ on the torus) = 0;
- "error is remainder", which is HR2.

**Repaired:**
- "Self-dual" is true only of the [8,4,4] extension, and "balance" holds there as 4:4.
- WHEN = 111 is a chart choice: the automorphism orbit of that column is all 7 positions.
- HᵀH is not the code's Laplacian: over the reals H·1111111 = (4,4,4).
- 192 is a counting identity for every surjective H, not a conserved charge.
- The 7-code is a *shortening* of [15,11,3].

**Bridges open (legitimate, not yet built):** the mapping function f(measurement) → (R, side, n) is exactly the snowball's intervention/observation map. It must be frozen before the data are read. For each theorem that points at physics (B5–B9 in the ledger), the ledger names the missing transport.

**Statistics:**
- All 17 base^n "deduced" assignments equal the global best fit.
- Against the free-fit null, p ≈ 5×10⁻⁵ *if* the 17 targets were fixed in advance.
- With about 30 or about 40 quantities screened and the best 17 kept, p rises to about 0.26 and about 0.75.
- The screening record is the missing datum.

**Irrational base 0.73336:** the inputs have 2 significant figures. Rounding alone spans 2,755 ppm, so the "30 ppm" and "1.4 ppm" figures are below the data's resolution. The snowball's exact form of the rational/irrational gap is RR-PHASE's integral residual 22/7 − π = ∫x⁴(1−x)⁴/(1+x²).

**ISW:** every bin has |S/N| ≤ 0.21, and the null χ² over 5 bins is 0.062. The Mar-18 all-positive prediction is untested at this depth; it needs about 10× the S/N. The v10 sign flip is post hoc.

## 5. The Cosmic Pattern against the snowball

- The lens L and the weights w are fitted. The recipe matches 187 of 300 random targets to 10⁻⁴.
- cosh² − sinh² = 1 is a tautology in R and r.
- The "D = 3 uniqueness" argument has three defects:
  - K is defined two ways;
  - R is defined two ways;
  - "13 is the smallest prime with 3 | p − 1" is false (7 qualifies).
- Its **D is a field order q, not a dimension**. 13 = |PG(2,3)| and the Rubicon's 7 = |PG(2,2)| are consecutive values of q² + q + 1 (A002061).
- Its most transferable idea is the *non-simultaneous comparison of H₀ through two lenses*. That is exactly RR-CONSTITUTION-RETURN's distinct endpoint lenses.
- Its Z₃ / "θ̄ = 0 + 2π/3 + 4π/3" has an exact home: the GF(4) cube roots of unity, which first appear in the phase at the hex aperture.

## 6. Constants first: the bounds as the opposing object

Computed exactly in `checks/constants_as_bounds.py`. Values tagged [recall] must be confirmed at the source.

- A constant's published bound is a **filtration** of intervals indexed by coverage. Each reader (continued fraction, digits, simplest rational, binary contact word) has exact **critical coverages**: the points where a term stops being forced. The inverted transitions are objects; the central value is the anchor.
- **α:** the first seven CF terms of 1/α, [137; 27, 1, 3, 1, 1, …], are forced by every CODATA edition at 1σ. The next term is not:
  - CODATA 2014 allows {17, 18}, 2018 {16, 17}, 2022 {18, 19};
  - Rb forces 19, and electron g−2 forces 18;
  - Cs and Rb are jointly incompatible below 4.21σ.

  OEIS A082726's comment on that term is a guess, which this computation corrects.
- **H₀:** jointly incompatible below 3.66σ. A nonzero lens residual is *forced*: 4.1, 2.56 and 1.02 km/s/Mpc at 1, 2 and 3σ.
- **Simplest renderings the bounds force** (1σ): α_s → 2/17; Ω_Λ → 11/16; H₀ ratio → 11/10. Also sin²θ_W → 37/160, which lies exactly on the interval endpoint and is therefore convention-dependent.
  - The drafts' renderings are admitted-not-forced (Cosmic 7/59, 20/29; Rubicon 1+(11/15)⁸) or excluded (Cosmic 3/13 tree; Rubicon 12/49, (11/15)⁷).
  - Numeral coincidences such as 11/16 = the rate of the hex [16,11,4] code are kept as evaluation fibers (RR-ROLE-EVALUATION), not promoted to derivations.

## 7. What each body of work was missing, and the answer found

| Missing from | Missing piece | Answer |
|---|---|---|
| Rubicon | the eighth coordinate; real balance | [8,4,4]: self-dual, 4:4, the anchor of TI3 |
| Rubicon | a torus without radii | K₇ incidence torus; doubled inverse sheet |
| Rubicon | a rule for when data force a rational | interval forcing; simplest rational; critical coverages |
| Rubicon | honest significance | a pre-registered screening record, then the free-fit null |
| Cosmic Pattern | a lens that is not a fit | a calibrated placed lens, one per endpoint |
| Cosmic Pattern | a meaning for "D" | field order q; A002061 |
| Snowball | a canonical publication object | rotate-complement cycle count (new entry candidate) |
| Snowball | the classical name of FP1–FP2 | Hermite's identity |
| Snowball | an explicit form of its ATLAS phase | z² + 1 in a normal basis; radices −2ʲ |
| Snowball | worked calibrated instances | α, H₀, CODATA editions |

## 8. Open items (retained residuals)

1. Confirm every [recall]-tagged measurement value at its source.
2. Freeze the Rubicon mapping function and publish the full screening list. Then recompute §4's statistics.
3. G: obtain CODATA's individual input values and run the joint-calibration projection in place of the expansion factor.
4. ISW: run the pre-registered Mar-18 prediction on the full data with a covariance model. Repair the v10 script's syntax, while keeping it labelled post hoc.
5. Reader extracts of the snowball source store: integrated as they complete (see the PR log).
6. OEIS: an equivalent-entry search for the rotate-complement sequence. The author then rewrites all draft text in their own words.
