# Claim ledger — THE RUBICON PrePub v1 and THE COSMIC PATTERN PrePub2 against Relation Snowball R25

Every claim in both drafts, one row each. For every claim the table records its status and its snowball contact. It also records the exact repair or the missing bridge. Numbers marked **[A]** come from `checks/audit_drafts_vs_snowball.py`. That script re-runs in about two seconds and writes `AUDIT_RESULTS.json`.

Status vocabulary (the snowball's own, TERMINOLOGY.md):
- **FORCED**: proved in its stated domain.
- **FORCED-REPAIRED**: true after the stated correction.
- **FIBER**: the claim collapses a non-singleton fiber; the missing coordinate is named.
- **BRIDGE-OPEN**: a legitimate claim whose transport (encoder, calibration, held-out data) is not yet supplied. The obligation is written out.
- **N'T**: admissible but not attained by the record given.
- **NOT**: excluded under stated conditions. A counterexample is given.

"Bridge-open" is not rejection. Per the author's direction, RR-LAW's "representations do not produce physical constants" is read as *the transport to physics has not been built yet*. Each such row lists what the bridge requires.

---

## A. THE RUBICON: code layer (pp. 2, 4, 8, 9)

| # | Claim (page) | Status | Snowball contact | Repair / bridge |
|---|---|---|---|---|
| A1 | 16 coherent of 128 states; 112 displaced; 8 per basin (p.2) | FORCED [A] | RR-B3, RR-CODE-CHARACTER | none |
| A2 | Every pair differs in ≥3; XOR-closed; perfect radius 1 (p.2) | FORCED [A] | RR-B3 | none |
| A3 | 168 symmetry-preserving permutations (p.2) | FORCED [A] (automorphism group enumerated = 168) | RR-SECTION-OBSTRUCTION (LM-ATLAS) | Add: the **eight-coordinate** completion has 8·168 = 1344 = \|AGL(3,2)\| symmetries. The 142857 phase is one of them (order 6, affine; [A] 7_bridges). |
| A4 | Printed 16 rows = kernel of printed H (p.2 vs p.4) | FORCED [A] | — | none |
| A5 | WHO+WHAT=WHERE, WHY+HOW=WHO, WHAT+WHEN=HOW, WHERE+WHEN=WHY (p.8) | FORCED [A] | RR-B1 (XOR = F₂ addition) | The identities are exact. **The labels are a chart**: the automorphism group moves any column to any position ([A] orbit = all 7). A labelled identity holds in every chart only after its labels are transported with the chart (RR-T1). |
| A6 | WHEN = 111 is "the timelike convergence position" (p.8) | FIBER | EIGHT_COORDINATE ER.3 (affine non-ownership); RR-ROLES | "Weight-3 column" is not invariant: every column is weight-3 in some equivalent chart. To make WHEN special, **declare** it (a basis B, BASIS_RELATIVE_INTERROGATIVE_TOMOGRAPHY). It is not *found*. |
| A7 | "Self-dual: [1,0,0,7,7,0,0,1]" (p.4) | NOT → FORCED-REPAIRED | RR-CODE-CHARACTER | [7,4,3] is not self-dual. Its dual is the [7,3,4] simplex code, with 8 words [A]. The **[8,4,4] extension** is self-dual [A], with weight enumerator 1,14,1 (LM-ATLAS Z(t)=1+14t⁴+t⁸). The palindromic enumerator [1,0,0,7,7,0,0,1] is correct. |
| A8 | "4 free vs 3 constrained — the ratio balances perfectly" (p.3) | NOT → FORCED-REPAIRED | RR-CODE-CHARACTER, ER.1–ER.4 | 4:3 is not balanced. The self-dual completion [8,4,4] is balanced **4:4**: content = mechanism = 1/2, with a lossless 4-bit substance + 4-bit route split (ER.4). The balance the text reaches for exists one coordinate up, at the WAY/zero point. |
| A9 | A single displacement returns home 112/112; double displacement aliases 336/336 (p.5) | FORCED [A] | RR-B3; RR-H-RETURN | Reframe per HR2: the double displacement is not "error". It is the part of the source **outside the section** (the syndrome no longer names it). The full return is the pair (codeword, leader) = (κ, ε). |
| A10 | Six "encounters" (Fano 1892, Hamming 1950, octonions, Steane 1996, Pauli, Pantheon+) map "the exact same relational topology" (pp.4, 8) | FORCED for the first four, as documented isomorphisms (EIGHT_COORDINATE §2: C8=RM(1,3), octonion support = XOR). BRIDGE-OPEN for Pauli and Pantheon+ | RR-COHERENT-REST (Steane-type self-dual stabilizer states) | Pauli antisymmetry ψ(x₁,x₂) = −ψ(x₂,x₁) has no declared map into F₂⁷. The Pantheon+ mass step is a two-population split, not a [7,4,3] basin. Both need an encoder. |
| A11 | [15,11,3] "R=4"; 15 Fano planes; "every pair shares 3 points" (pp.7, 9) | FORCED (PG(3,2) has 15 planes; two planes meet in a line of 3 points) | RR-FIELD-ATLAS projective charts | "15 toroidal tilings" has no stated construction. It needs the K₇ torus embedding (A15) per plane, written out. |
| A12 | "7-position reading IS the 15-position reading with top bit unread" (p.9) | FIBER | RR-H-RETURN; RR-T2 | Shortening versus puncturing matters (ER.1: puncturing C8 gives [7,4,3], shortening gives [7,3,4]). [7,4,3] is obtained from [15,11,3] by **shortening** at the 8 positions whose columns have top bit 1. Those 8 coordinates are held at zero, leaving 11 − 8 + 1 = 4 free dimensions, because the top check row becomes vacuous. "Leaving the top syndrome bit unread" is a different operation: it projects the observation, and every 3-bit syndrome fiber then grows from 8 to 2¹² words. State both as distinct maps (RR-H-RETURN; ER.1 "puncturing, not shortening"). |
| A13 | [15,7,5] "drops content to 47%" (p.9) | FORCED (7/15) | — | none |
| A14 | Content ratios 4/7 → 11/15 (p.9) | FORCED; **BRIDGE, OEIS** [A] | — | k/n = A000295(r)/A000225(r): 0/1, 1/3, 4/7, 11/15, **26/31**, 57/63. The draft's "next threshold" is r=5, 26/31, not an independent choice. |
| A15 | Fano plane on genus-1 surface: V−E+F = 7−21+14 = 0 (p.10 Thm 9) | FORCED [A] | RR-INTRINSIC-TOPOLOGY | **This is the radius-free torus.** K₇ triangulates the torus with 14 faces, which split into two Fano planes. It is a combinatorial surface derived from incidence (IT2): no R, no r, no embedding. See §D. OEIS A000934 (Heawood number of genus 1 = 7). |
| A16 | "Inverted torus", R=13, r=3, (1,3) knot, "flange" (pp.9–10; ISW v10) | NOT as a derivation → replaced by A15 | RR-NONRADIAL-DOUBLE NR8–NR13; OP100 (mapping torus needs an actual gluing) | The inward/outward "inversion" is the doubled inverse sheet (C, C⁻¹) joined by the reflection J (JCJ = C⁻¹). No radius occurs. The "flip" is the involution J, not a flange crossing. |

## B. THE RUBICON: the nine "theorems" (pp.10–11)

| # | Claim | Status | Snowball contact | Repair / bridge |
|---|---|---|---|---|
| B1 | Thm 1: S[x] = syndrome weight; S=0 ⇔ codeword; "δS=0 is least action" | FORCED (first part) / BRIDGE-OPEN (second) | RR-FIELD-ATLAS FA5 (Euler–Lagrange); RR-SINGULAR-RESPONSE | A zero-set indicator is not a variational principle. The legitimate discrete action is quadratic over ℝ (FA5: ½Σ(x_{i+1}−x_i)², whose minimizer is affine). Over F₂ there is no derivative. Bridge: declare the real lift (CA14, midpoint contacts ½) and a quadratic whose kernel is the code. |
| B2 | Thm 2: HᵀH "is the Laplacian"; "4 null eigenvalues span the code subspace" | NOT [A] | OP050; RR-LATTICE-INCIDENCE ("Real rank is not enough") | Over ℝ, H·1111111 = (4,4,4) ≠ 0, so the real null space is **not** the binary code. A Laplacian needs a graph, an inner product and boundary data (OP050). The real Gram of the seven nonzero columns is 2I+2J (RR-LATTICE-INCIDENCE), a different object. |
| B3 | Thm 3: Σ‖Hx‖ = 192 "conserved charge, Noether" | FORCED as an identity / NOT as a symmetry charge [A] | RR-INVARIANTS (invariant vs plateau) | 192 = 2^(n−r)·r·2^(r−1) for **every** surjective H [A]. It is a counting identity. The script's "permutation invariance" permutes both H and x, so it is a tautology. Sequence over r: 1, 8, 192, 65536. No OEIS entry was found (candidate entry, §E). |
| B4 | Thm 4: rank-3 metric, 3+4 split | FIBER | RR-T4; OP041–042 | Rank 3 is correct (real and binary). "Metric tensor" needs a positive pairing on the source (OP-norm), which HᵀH does not supply on F₂⁷. |
| B5 | Thm 5: Hx = s "structurally identical to Einstein" | BRIDGE-OPEN (N'T) | RR-H-RETURN HR1–HR4; OP051 | Hx = s is an observation with an exact inverse fiber (8 words per syndrome). Any analogy to G_μν = 8πT_μν needs a declared transport of carriers (RR-EM "physical equivalence needs correspondences of states, operations, units, dynamics and predictions"). |
| B6 | Thm 6: 3 rows + sequential reading = 3+1 spacetime | BRIDGE-OPEN | TEN_INTERROGATIVE: "durations, frequencies and physical simultaneity remain unavailable until a source supplies a clock, units and a covariant transport"; OP107 (TIME is a role, not a clock) | The row-order of H is a serialization. Permuting rows preserves the code. Time needs an epoch law (RR-OBSERVATION-EPOCH EP1–EP2). |
| B7 | Thm 7: λ = (k/n)^k = (11/15)^11 = 0.032985 matches Γ = 0.033 ± 0.010 | FIBER + BRIDGE-OPEN | RR-JOINT-CALIBRATION; RR-QUOTIENT-PHASE QP5 | The measured value carries ±30 %, so "0.05 % off" is not a resolved match. The ±0.010 band admits 0.023–0.043, and its 11th roots span 0.7097–0.7512 [A]. Bridge: pre-register (k/n)^k for other (n,k) before comparing. |
| B8 | Thm 8: PSL(2,7) irreps 1,3,3̄,6,7,8 → Higgs, SU(2), colour, gluons | FORCED (dimensions) / N'T (mapping) | RR-ROLE-EVALUATION RE1 (equal numerals ≠ equal roles) | 1²+3²+3²+6²+7²+8² = 168 is correct. "3 → SU(2)" and "8 → gluons" are evaluation collisions (same numeral, different typed roles). The 3 and 3̄ are a complex-conjugate pair, not SU(2)'s real adjoint. |
| B9 | Thm 9: winding → Top/Higgs = 15/11, W/Z = 7/8 | N'T | RR-GM-WINDING (winding is an integer lift of a declared action) | No winding number is computed. 15/11 and 7/8 are code ratios, not windings. The draft's own caveat (BIN 3) stands. |

## C. THE RUBICON: measurement layer (pp.1, 3, 5–10; experiment_corrected.py)

| # | Claim | Status | Contact | Repair / bridge |
|---|---|---|---|---|
| C1 | H₀ = 67.4·(1+(11/15)⁸) = 73.04 | FORCED arithmetic / BRIDGE-OPEN meaning | RR-PHYSICAL-CALIBRATION; RR-CONSTITUTION-RETURN (placed displacement under a lens) | n=8 is "basin size". The same argmin as C4 [A]. Bridge: a declared map from the distance-ladder / CMB pipelines to a depth, fixed before seeing H₀. |
| C2 | "Planck 3 layers cross at R=4; SH0ES 5 layers check at R=3" | FIBER | BASIS_RELATIVE: "a basis must come from the source or an explicitly declared experiment; it cannot be selected because it makes a desired result appear" | Layer counts are selected, not derived from the pipeline documentation. The record of **which** layer counts were tried is missing. |
| C3 | Mapping function f(measurement) → (R, side, direction, n) (pp.6–7) | BRIDGE-OPEN (the right object!) | RR-INTERACTION-RETURN IR1; RR-FORCED-LAW | This is exactly the snowball's intervention/observation map. It must be **written as a rule** that receives instrument documentation and returns (R, side, n) **without** the measured value. It then acts as a held-out predictor (see §E, pre-registration protocol). |
| C4 | 19 measurements, "No fitting", avg offset 1.56 %, p < 1e-5 | NOT as stated / BRIDGE-OPEN | RR-FORCED-LAW (forced only if a single value survives *before* data) | [A] (1) All 17 base^n assignments equal the global argmin over 6 bases × \|n\|≤80. (2) W/Z has a code bug: the script returns the measured value, so it shows 0.00 % instead of 0.73 %. The honest average is 1.60 %. (3) The permutation test only shuffles magnitudes spanning 10⁻¹⁰…10², so p=0 is uninformative. (4) Against the free-fit null, p ≈ 5×10⁻⁵ **if** the 17 targets were fixed in advance. It is 0.06 / 0.26 / 0.75 if 25 / 30 / 40 quantities were screened. The significance is undefined until the screening record exists. |
| C5 | 9.3σ upper bound; >5σ lower bound from 5 "pipeline-locked" | NOT (conditional on C4) | RR-SOURCE-SEMANTICS | Recompute only after C3 is frozen and the candidate list is published. |
| C6 | Irrational base 0.7333637669 vs 0.7333623795, "agree to 1.4 ppm", "30 ppm self-refraction" | NOT as precision [A] | RR-PHASE (22/7 − π = ∫x⁴(1−x)⁴/(1+x²) is the model for an *exact* rational/irrational gap) | Inputs are 2-significant-figure. Rounding alone spans 2,755 ppm and the Γ band spans ±28,321 ppm [A]. The "chord vs arc" idea has a correct form in the snowball: an exact integral residual (RR-PHASE η), never a ppm read off rounded data. |
| C7 | G CODATA expansion 5/2 "exact" | FIBER | RR-ROLE-EVALUATION | 5/2 = (3+2)/2 is one of many role expressions evaluating to 2.5. The fiber must be retained. |
| C8 | Ising β = (4/7)² = 0.3265 vs 0.326419 (0.03 %) | FORCED arithmetic / N'T meaning | RR-ROLE-EVALUATION | A numerical coincidence until a map from the 3D Ising universality class to F₂⁷ is declared. |
| C9 | Mass ratios 15/11 (1.1 %), 7/8 (0.73 %) | FORCED arithmetic / N'T | same | as B9 |
| C10 | ISW: +2.37 % … +0.38 % (Mar 18 prediction) | BRIDGE-OPEN (a genuine pre-registered prediction) | RR-MODEL-ATTAINMENT (y = y∥ + y⊥) | The data give SNR 0.21, −0.04, −0.12, −0.05, −0.03, with null χ² = 0.062 over 5 bins [A]. They neither confirm nor refute. The prediction's **signs** (all +) disagree with bins 2–5, but inside noise. Keep the Mar-18 prediction as the registered test; it needs ~10× more S/N. |
| C11 | ISW v10 "signed refraction", sign flip at z=0.5 "confirmed" | NOT (post hoc) | BASIS_RELATIVE (no result-shaped choice) | The v10 model was written after the bin signs were seen (its docstring states the measured signs). The script does not parse ("else:" with only a comment). |
| C12 | "Error is remainder" (p.1) | FORCED (in the snowball's form) | RR-H-RETURN HR2: "The second term is not an error by definition"; OP108 | **The draft's founding sentence is a theorem of the snowball.** x = e(Hx) + R_H(x): residual relative to a declared section. Rewrite the thesis in HR2's words. |
| C13 | Yeo-7 networks 4/4, Wierzbicka 7 interrogatives (p.9) | BRIDGE-OPEN | EIGHT_COORDINATE §5 ("eight semantic roles are not the eight affine bit positions"); RR-ROLES (10 roles, extensible) | The snowball uses **10** question jobs (WHO…WHICH, WAY, N'T, NOT) with a 10+ continuation, not 7 fixed axes. The Rubicon's 7 are the punctured chart; WAY is the eighth (whole-return) seat. |

## D. THE COSMIC PATTERN

| # | Claim | Status | Contact | Repair / bridge |
|---|---|---|---|---|
| D1 | Observer is "2.5-D"; codim(T² in ℝ³)=1 → 2+½ | N'T | RR-LAW (no radial origin/external observer) | "2.5" is not a dimension in any declared sense. The snowball's **½** is exact elsewhere: CA6 (decimal glyph half-address) and CA14 (midpoint contact coordinate ½ between two inscriptions). That is the rigorous "between". |
| D2 | Lens L = R/(R + r·cos(6π/R)) = 0.97294 | NOT as a derived constant / BRIDGE (the only legitimate radius is a calibrated lens) | RR-CONSTITUTION-RETURN "Nonlinear endpoint coordinates"; RR-RELATIVE-DISK ("the scalar a is the actual calibrated radius") | A lens may carry a radius **only** as a calibrated parameter of that lens. A lens then acts on a *placed* displacement (G(p), G(p+δ)−G(p)), never as a global multiplier L^w on every constant. This is the author's "topographical neutrality except in lensing", in theorem form. |
| D3 | Q_obs = Q_true·L^w with rational w | NOT (fit) [A] | same; RR-FORCED-LAW | The weights are solved from the data (w_needed = ln(Q_meas/Q_tree)/ln L [A]). The recipe matches 187/300 random targets to 10⁻⁴ [A]. |
| D4 | sin²θ_W = 3/13, α_s = 7/59, 1/α = 137, Ω_Λ = 20/29, N_gen = 3 from D=3 | FIBER | RR-ROLE-EVALUATION | The integers are evaluation collisions of typed roles. Keep them as a **numeral chart** (RE1–RE2), not a derivation. |
| D5 | "D = 3 unique": knots, PG(2,3), Whitney, cyclotomic closure | NOT (as argued) [A] | RR-I1 | (a) T² embeds in ℝ³; Whitney's 2n is an upper bound. (b) K is defined two ways (D³+D+1 vs 2R+r+2), which disagree at D=2. (c) R is Φ₃(4)=21 on p.24 but Φ₄(4)=17 on p.31. (d) "13 is the smallest prime with 3∣p−1" is false (7). (e) **D is a field order q, not a dimension**: 13 = \|PG(2,3)\| and the Rubicon's 7 = \|PG(2,2)\|. These are consecutive values of q²+q+1 (OEIS A002061). |
| D6 | cosh² − sinh² = 169/160 − 9/160 = 1 → arrow of time | NOT (tautology) [A] | RR-NONRADIAL-DOUBLE | True for any R ≠ r. An arrow needs an ordered action; the snowball's doubled sheet (C forward, C⁻¹ inverse, J exchange) is the orientation-bearing structure. |
| D7 | Hubble tension = non-simultaneous comparison through the lens | BRIDGE-OPEN (correct *instinct*) | RR-CONSTITUTION-RETURN: "If the two endpoints use distinct lenses, their source difference is G_d⁻¹(b) − G_c⁻¹(a). Those endpoint maps must not be silently replaced by one inverse." | **This is the most transferable Cosmic Pattern idea.** Formalize as two placed endpoint lenses (CMB pipeline, ladder pipeline), each calibrated, and test whether G_CMB⁻¹(67.4) = G_ladder⁻¹(73.0) is attainable. |
| D8 | Born rule from area-preserving projection | N'T | RR-DISTRIBUTION-RETURN; RR-MODULATION-RETURN ("Neither an unread cross term nor an infinite spectral expansion establishes physical collapse") | Needs a stated projection with a measure. |
| D9 | Strong CP θ̄ = 0 + 2π/3 + 4π/3 ≡ 0 | N'T | RR-S1 (character sums) | The sum of cube-roots-of-unity phases vanishing is PA1. A map to the QCD vacuum angle is not declared. |
| D10 | 29 modes, 20 invisible → Ω_Λ | N'T | RR-CYCLIC-TOMOGRAPHY (blind modes are exact cyclotomic factors of a declared reader) | If "invisible modes" is meant, the snowball has the exact machinery: blind-order signature B_m(q). It needs the reader P(z). |
| D11 | Zero free parameters; 17+ verified predictions | NOT [A] | RR-FORCED-LAW | Weights and trees are selected (D3). |

## E. Summary of what each draft is missing, stated as obligations

1. **A frozen observation map** (Rubicon C3). It receives instrument documentation only and returns (R, side, n). The snowball calls it Oₑ in IR1.
2. **A screening record** (C4). This is every quantity examined, including rejects. The significance of C4 is undefined without it; with it, the free-fit null gives an exact p-value.
3. **The eighth coordinate** (A7, A8, C13). The self-dual [8,4,4] completion (LM-ATLAS) supplies balance 4:4, self-duality, the WAY/whole-return seat, and the 142857 phase as a symmetry.
4. **A radius-free surface** (A15, A16). K₇ on the torus is incidence-derived (IT2). Inward/outward is the doubled inverse sheet (NR8–NR13).
5. **Lens as calibrated placement** (D2, D7). A radius appears only as the lens's calibrated parameter, acting on placed displacements. Two distinct lenses give G_d⁻¹(b) − G_c⁻¹(a).
6. **Exact residual in place of ppm** (C6). Use an integral/interval residual (RR-PHASE, RR-JOINT-CALIBRATION), never ppm from rounded inputs.
7. **OEIS anchors** (A14, D5, B3) are verified live [A]: A000295/A000225 (bases), A002061 (7 and 13), A002884 (168), A000934 (Heawood 7), A016031 (16 codewords, a numerical fiber), A020806 (142857). The syndrome-total sequence 1, 8, 192, 65536 has no entry.
