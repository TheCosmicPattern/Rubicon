# What the snowball's source store says: cross-reader synthesis

Every line of the snowball's retained source material (≈1.3 MB) was read by parallel readers against one brief, [`source_extracts/BRIEF.md`](source_extracts/BRIEF.md). Their itemized, line-referenced extractions are preserved verbatim in [`source_extracts/`](source_extracts/):

| File | Source covered |
|---|---|
| `extract_A.md`, `extract_A2.md` | SOURCES.md L1–3700 (ATT-A/B/C, operator audit, SRC-GREEK, SRC-01…06 §0–14.3A) |
| `extract_B.md` | SOURCES.md L3701–7300 (SRC-06 §14.4–20, SRC-07 trueform, REF-V5/V6, ATT-D, SYMBOL_AUDIT) |
| `extract_C.md` | SOURCES.md L7301–11143 (archives SC-01…12, Census dossier, prime dossier, ledger, SRC-ATT-TRANSLATION) |
| `extract_D.md` | CLOSURE_WEB_RESIDUAL_SYNTHESIS.md |
| `extract_E.md` | PROJECTIVE_RESIDUAL_COCYCLE_TOMOGRAPHY.md |
| `extract_F.md` | PROOF_FIELD_GENERATOR.md; OBSERVATION_AND_AMBIGUITY_METHOD.md |
| `extract_G.md`, `extract_G2.md` | OEIS_EDITORIAL_EXPECTATION_FIELD.md, SIGMA_EPOCH…, REFERENCES, MATHEMATICAL_FIELDS, FINDINGS, RELATION_HANDOFF, REGISTRY.json |

The small method files were read directly: BASIS_RELATIVE…, EIGHT_COORDINATE…, FORMULA_CARTOGRAPHY, HAMMING_CONVENTION_BOUNDARY, RELATIONAL_OPERATOR_SEMANTICS, TEN_INTERROGATIVE…, VORTRIMETRIC….

Process note: the B reader reports that it deleted notes written before one read had returned and then rewrote them from the text.

Items marked ✔ were re-derived in `checks/` (see `TRANSITION_RESULTS.json`).

---

## 1. The container is gone; the source itself says so

- **Hamming is an aperture.** ATT-C: "[7,4,3] Hamming torsor coordinates … were initially conflated with the parent object. They are now recognized as typed source maps (specific discrete apertures) rather than the definition of the arithmetic itself." PRCT L11–19: "[7,4,3] is only the (q_field, r_rank) = (2,3) chart." The general object is PG(r−1,q) with N = (qʳ−1)/(q−1).
- **The general Hamming object is [8,4,4]; [7,4,3] is a puncture, and "the puncture moves"** (A2: L2091–2099, L2341–2356; |AGL(3,2)| = 1344, of which 168 is the linear part).
  - ✔ TI9: GL(3,2) has element orders {1,2,3,4,7}, with no 6. The 142857 phase (order 6) therefore needs the translation, i.e. the eighth coordinate (CLOSURE_WEB L241–245).
- **H must not be bare.** Operator audit L674: "`H` as parity-check matrix … collides semantically with fundamental HORIZON and localizes the universal law to one code chart; never use bare `H` in the parent." SYMBOL_AUDIT: "H must not silently turn into a physical Hamiltonian."
- **The horizon is the fold that supplies locality**, "not one more value in the aperture" (operator audit L483). This matches the author's "the description is the container".
- **No hand-set values at the horizon:** "What must not happen at H: assigning distances, weights, thresholds, phases, bases, or meanings by hand" (L504). "Do not default to decimal, binary, rank three, seven positions, or unit cost" (PFG L64–67).

## 2. The torus, rebuilt with no radii (three concordant sources)

| Source | Radius-free torus | Line refs |
|---|---|---|
| PRCT, PFG | 0 → T⁴ → T⁷ → T³ → 0, split exact; the binary code is the 2-torsion kernel; Sierpinski 7-simplex transversal: "a split torus plus a fractal transversal rather than a finite code relabelled as a manifold" | PRCT L1157–1212; PFG L1340–1356 |
| SRC-06 | H = E/Λ, a lattice quotient with Haar measure: "reducing context modulo a return lattice is not reducing source displacement modulo it" | B: L5565–5585 |
| Operator audit, RELATION OP100 | torus / mapping torus = "periodic action plus gluing … winding/path class after periodic gluing is declared" | A: L646 |
| This work | K₇ triangulates the torus: 7 vertices, 21 edges, 14 faces (two Fano planes), so χ = 0; incidence-derived (IT2) | ✔ audit §1 |

**The Cosmic Pattern's radii are one parameter** (✔ TI11). 169/160 and 9/160 are cosh²s and sinh²s with tanh s = r/R = 3/13. So the two radii are one point |z| = 3/13 in the snowball's relative unit disk (RR-RELATIVE-DISK), where a radius is "the actual calibrated radius": the lens-calibration role, and only that.

## 3. Lensing is the one place that requires placement

- **Placed lens.** Δ_G(p,δ) = G(p+δ) − G(p): "a lens can ignore placement only if it is affine" (B: L5851–5903; A2: L1746–1754, "a nonlinear displayed average cannot impersonate that inverse").
  - Counterexamples: x² gives 2 in place of 4 (A2 L1521–1526); 2ur + r² (F: OAM L719–726).
- **Moving lenses carry their measure and Jacobian.** Ignoring the Jacobian "fabricates a response under a pure rescaling" (A2 L3338–3370).
- **A lens common to all readings cancels from ratios and can only be calibrated** (G2: RR-PHYSICAL-CALIBRATION "common_geometry_phase", RR-M7). Absolute gain is a gauge; "relative transfers, not the absolute latent sample path" are recoverable (D: CW.96–100).
- **Kernel-inclusion test for any observable carried through a lens or aperture:** C(Bx) = Ax exists iff ker B ⊆ ker A (D: CW.211; F: PFG L2128–2142).
- **Neutrality is shown per geometry, not once.** "An affine-only canary is not geometry neutrality": each source-native geometry needs its own transport (G2: EXPECTATION_FIELD L232–237). This is the precise obligation attached to "topographically neutral except in lensing": it holds for every geometry whose transport is exhibited.
- **"Guaranteed 2.7 % error" is contradicted:** "A nonzero residual is not guaranteed for every comparison … every failure of global integrability has an exact cycle witness" (E: PRCT L1880–1883). The calibration offset m_c − m_d is "determined placement calibration, not unexplained noise" (B: L5812–5820).

## 4. Constants first: what the source already had, and what this work adds

- **Already in the source.**
  - SRC-06 certifies 1/α = [137; 27, 1, 3, 1, 1, …] from the ±1σ interval (B: L4318–4353). "A finite prefix alone cannot decide whether an entire expansion is … governed by a proposed geometry."
  - "Constants only move where transition cuts fall; the inverse is an interval, no midpoint or least-squares fit" (B: L4429–4500).
  - A chosen target is "NOT a predicted value of alpha" (B: L4112–4128).
  - The one worked physical relation is E_B/(m_e c²) = α²μ/[2(1+μ)] (B: L4817–4849).
- **Scheme dependence.** sin²θ_W has on-shell 0.22342, effective 0.23154 and MSbar 0.23122 values (B: L4232–4303). "3/13 = sin²θ_W" must name its scheme.
- **Added here** (`checks/constants_as_bounds.py`):
  - several editions and measurements side by side;
  - exact joint-relation certificates (Cs vs Rb α, incompatible below 4.21σ; CODATA 2018 vs 2022, below 2.21σ; H₀, below 3.66σ);
  - critical coverages, where transitions are inverted into objects;
  - forced simplest renderings;
  - the A082726 correction.

## 5. The 19-measurement argument, as the source would grade it

- "Intersect the routes; never tally them … their number supplies no residual warrant" (F: PFG L1796–1815).
- "Treating ten correlated readers as ten independent successes" is forbidden, as is "searching for a flattering match" (B: L4363–4366).
- The method never replaces readings by "sum, mean, variance, or a scalar score" (E: PRCT L290–294).
- Previously falsified classes include "bit-position semantics not in the fold" and "forced exponents" (C: L10462–10467). These are the Rubicon's interrogative bit semantics and depths n = 8, 11.
- A companion matrix matches any Euler factor for free (D: L2892–2903). This is the same move as fitting base^n or L^w.
- Relabelings are not neutral: only 6 of 5,040 commute with a fixed operation (C: L7403–7411). The interrogative-to-column assignment must exhibit the operation it preserves. No labelling of the seven columns is invariant under the full automorphism group (G2: RR-EQUIVARIANT-RETURN).

## 6. Where 3, 7, 13 and 168 legitimately live

- **3.**
  - r = 3 is characterized by 2^r = 2(r+1). ✔ TI10: dim D(C) = dim C⊥, the single-cycle condition for z²+1, and 2(r+1) = 2^r are *one* equation read three ways.
  - An independent route is τ(2^r−2) = 2^r−1−r, again only at r = 3 (C: L10329–10330). ✔
  - A radix-dependent route: "10 localities force r = 3" (B: SRC-07 L6047–6117). The source itself notes the tension with "radix is serialization only".
  - "a chart fact, not a limit" (A2: L2408–2415).
- **7.** It is a block length, and the 7 planes through each point of [8,4,4] (B: L3773–3805). The 1/7 digit positions have symmetry AGL(1,7), of order 42, not PSL(2,7) (F: OAM). That symmetry acts on Z/7, while TI6's AGL(3,2) acts on F₂³: different carriers, both correct.
- **13.** 999999 = 3³·7·11·13·37 and Φ₆(10) = 91 = 7·13, both "base-10 specific" (C: L10254–10265). The Walsh spectrum of the 142857 weights contains 11 and −13 (A2: L2961–3007).
- **16 / 112 depends on the horizon.** Under five shifted horizons only {0,127} are coherent for all, and 76 words are coherent for none (G2: SIGMA SE.14, L290–294). "Coherent" is a relation between word and horizon, not a property of the word.
- **Not in the package:** Einstein equations or curved spacetime, cosmological inference, hypothesis testing, Lie-group classification (G2: MATHEMATICAL_FIELDS L34, L62, L72–73). Its only radius-bearing object, the WGS84 ellipsoid, is a calibration convention (L74).
- **112, 168.** In OAM these count five-element minimal ambiguous omissions and five-circuits in F₂⁴ (F: OAM L236–255). The same numerals appear with different roles, i.e. evaluation fibers.
- **R = 4.** One pair field yields [7,4,3], then [8,4,4], and then the shortened code [14,10,3], which is [15,11,3] minus one column (F: OAM L169–196). That is a non-geometric origin for the drafts' step to R = 4. The full-reptend closure breaks at N = 15, which is not prime (G2).

## 7. Interrogatives

The sources give different counts: 10 roles (RELATION); 8 channels + 2 operators (PFG L193–204); five countercorrelary pairs (ATT-C L418–425); 16 editorial rows (EXPECTATION_FIELD); and a 10+ continuation (BASIS_RELATIVE). They agree that these are "auditing roles, not ten independent bits" (C: L7744–7761) and "provisional functional assignments, not discoveries about English, spacetime, consciousness" (A2: L2434–2437). PFG pairs WHY with observability and WAY with controllability, the Kalman dual (F: PFG L381–399). So the Rubicon's 7 are one chart of an open family.

## 8. OEIS: the source's own publication discipline

- **The live quartet** is ENTRY + a-file + b-file + program for the signed translation-carry array P(m,i,h) (C: L10925, L10986–10994; G2: REGISTRY L5852–5857). Live bytes are absent from the package, and novelty is not cleared (B: L6568, L6893–6897).
- **Companion faces must not become new entries.** "A new public sequence created from a companion face" is a rejection condition; there is one centre with companions (F: PFG L2291–2332). **This overrides the earlier recommendation** that the rotate-complement count be a separate entry. See the revised `OEIS_SUBMISSION_RECOMMENDATIONS.md` §2.
- **Attributions** to carry: Geller–Kra–Popescu–Simanca, and Radicic (Filomat 2017) (F).
- **Risks to strip** before resubmission:
  - SRC-ATT-TRANSLATION's AI-drafted %C lines, "immune to pushback" language, and a Fan–Pollack sentence missing its "nonsquare g, g ≠ −1" hypotheses (C: L11020–11096);
  - ATT-D's broken `continuous_jump` and its contour integral of floor (B: L6918–7029; RR-PRESENTATION-CHECK);
  - the Φ notation collision (translation carry versus cyclotomic);
  - JP000016's "stitched unrelated blocks" (A2);
  - SIGMA L792–794 arithmetic slip ((3,2) gives N=4, K=2, b=6) (G2).

## 9. Open residuals recorded by the sources themselves

- The CIE colour test was not performed (B: L6688).
- The Riemann TS29/TV58/TV435 items are open, and "PRCT does not supply its sign" (E: L2097).
- Every Millennium-problem realization in CLOSURE_WEB is OPEN, with "no Millennium promotion" (D).
- RR-T7, RR-S3, RR-S7 and RR-OEIS-TRANSFORM-GRAPH have no tests (G2).
- GREEK_OPERATOR_COMPOSITION_TABLE_v14.tsv exists only as a path (B).
