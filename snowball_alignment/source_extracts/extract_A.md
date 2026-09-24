# Extract A — SOURCES.md lines 1–3700

Line numbers are SOURCES.md file lines (L###). "src" numbers are the embedded original line numbers where helpful.
Header L1-5: "The canonical mathematics is RELATION.md. Supplied commentary below may contain claims corrected there." -> everything below is evidence, not authority.

## ATT-A (L7-174) Pasted text.txt — "mutual scaffolding" of view-master-9 (generator/selector) and /relation/ (carrier)
- L13-15: v9 and /relation/ are "not competing options ... exact structural scaffolding to each other's gaps"; GM = "exact mathematical junction".
- L19: v9 gap: "The generator has no physical arena in which to act." (the word "physical" used for a chart = arena; metaphorical, cf. category-error risk (c)).
- L20: carrier R_m = {(d,x,h,q,r): dx+h = mq+r} "unconstrained, all-slope manifold (m^3 terms per block)"; "lacks an intrinsic arrow of dynamical motion".
- L33: unified vessel T(n,px+h)=floor((beta(n)x+h)/p).
- L51-54: row x=1 sums to beta(n); block sum beta(n)p(p-1)/2; "the chart manufactures the selector on its first non-trivial row. The relation is the body; the selector is its boundary trace."
- (h) L58, L63: repetend 142857 treated mod Q=b^{p-1}-1; "reduction modulo Q discards the overflow carry". Operator identity L62: b(Wx)=W r(x)+Q g(x), L=p-1, W=(b^L-1)/p, Q=pW. L64: g(x)=C(x,0) "the exact integer winding that counts how many times the word wraps past Q". L65: "modular projection and the integer lift of the exact same operator. Neither is complete without the other."  [aha: this is the exact arithmetic form of "error is remainder": the winding g lost by mod-Q reduction is the discarded carry — i.e., a residual that is information, not error.]
- L71 complete phase profile: sum_h C(x,h)=bx (instantaneous inversion across all phases). L74/77: observation threshold b^N>=p (Theorem B10) across time at fixed phase. L78: (7,10): one step separates all 42 pairs; (11,6): 6<11<=36 requires 2 steps; "space-time trade-off of the relation" (metaphor: spatial phase vs temporal iteration).
- L84: Fourier: sum g(x) theta^x = -b/(1-theta) + 1/(1-eta) != 0 (Theorem D6).
- (a) L87: Christoffel sequence of step differences; boundary closing step Delta_close = -floor((m-1)b/m) enforces "oint dDelta = 0". L89: Midy g(x)+g(p-x)=b-1 kills every nonzero even Fourier mode. L91: "holonomy jump ... ensures that the discrete steps close with zero net curvature on the torus." [radius/torus: here "torus" is the periodic Z/m boundary — a discrete cyclic closure with zero curvature, no radii. Contrast Rubicon T^2(13,3).]
- (f) L96: Sigma(u,v)=q(u)+q(v) "missed the value 14 ... diagnosed as an 'imbalance' requiring external explanations" — corrected L99-100: (Sigma, Delta) injective on p(p-1) pairs; "missing 14" = gap set {3,6} of numerical semigroup <7,10> transported to pairs (8+6: 6 gap; 7+7: u=v forbidden; 9+5: 9>q(6)). [aha: a "missing value" initially read as imbalance/anomaly is a structural gap — direct precedent for reading Rubicon's residuals as structural, not as errors to be explained externally.]
- L101: Z/p^2 lift (d,x)->(r(d), bx+g(d) mod p); L-step return adds omega*d to carry. omega = Fermat quotient residue.
- L106: "every number and structure is an intrinsic counter or an adjacent counterbalance."
- L111-147: draft OEIS entry. %N L115: least b>=2 primitive mod p and modulo no smaller odd prime. %C L116: "Euclidean division relative to a movable bound: z = a + m*q + rho". L118 phase jump C(x,h+1)-C(x,h)=[h=p-1-r(x)] "locates the remainder on the boundary". L119 column h=0 = first base-b digit of x/p and Apéry gap counts of <p,b>. L122: omega!=0 one p(p-1)-cycle; omega=0 p cycles of length p-1; (Wx)(Wy)=W omega xy mod pW. L123 base-shear invariance floor(((b+tp)x+h)/p)=tx+floor((bx+h)/p); "fundamental domain for the base-shear gauge action" ("gauge" = shear orbit, purely arithmetic).
- (h) L134-143: (7,10) block; x=1 row 1,1,1,1,2,2,2 sums 10 = 7*1+3; zero-phase column 0,1,2,4,5,7,8; remainder orbit 1,3,2,6,4,5 reads 1,4,2,8,5,7 "the repeating digits of 1/7 in base 10"; column sums 27..33; total 210 = 10*7*6/2.
- L144 Cf A000537, A020806, A280015, A393470.
- L173: claim "every artificial constant, decimal bias, and ad-hoc premise disappears" (commentary rhetoric: "pure, unassailable").

## ATT-B (L176-319) — re-evaluation: GM retreated from v9
- L193-195: three layers: v9 1D scalar beta(n); GM 2D floor((bx+h)/p); relation 3D affine floor((dx+h)/m) "(Base-free, selector-free)".
- L202-206: a(n)=min{b>=2 primitive mod prime(n), not primitive mod any smaller odd prime}; terms 2,3,10,6,15,91,21,120,55,1035,616,399,2155,510,7665; precedent A280015 (Robert Israel) admits prime 2 so bases even; a(n)<=A280015(n) equality iff even; "proven natural density 1".
- L212: "Uncanny Valley" critique of GM (later reversed by ATT-A L21: "never an awkward hybrid") — [ambiguity/correction pair: ATT-A and ATT-B contradict on GM].
- L220-222: Theorem B10 (b^N>=p) over ordered k-tuples: S=sum g(x_i), D_i=g(x_i)-g(x_1).
- L229-231: Theorem D6; eta=theta^{b^{-1} mod m}; "eta=(b-1+theta)/b cannot lie on the unit circle" -> C invertible for all coprime (m,b). (circle = unit circle in C, spectral, not geometric.)
- L238-242: Theorem D7: Z(s,u,v)=sum s^x u^{g(x)} v^{r(x)}; k![z^k] prod (1+z u^{g(x)}).
- (f) L247-250: Theorem D2: E(x)=x-r(x)=m g(x)-(b-1)x ("displacement"), E: Z->cZ c-to-one, c=gcd(b-1,m); global inverse x=e+((-b(b-1)^{-1}e) mod m); "E(7)=7 reconstructs the integer 7, whereas the residue-only inverse erroneously returned 0." [correction: residue-only reading loses placement/lift — same pattern as nonlinear lens needing placement.]
- L254: (11,6) counter-model: duplicates/zero counts; "single-observation recovery is impossible when b<p"; "essential boundary that prevents over-generalization".
- L262-265 base shear B=sm+d. L268: omega; (7,10) omega=1 vs (7,31) omega=0 "identical low residue orbits but totally different higher-order product algebras". [aha: same low-order observation, different lift — a direct model of observational underdetermination; cf. "Rubicon fits" that match at one order but not the lift.]
- L291-311: Track 1 (generator) vs Track 2 (carrier: row m lists floor((dx+h)/m), block sums A000537(m-1)=(m(m-1)/2)^2, AGL(1,m)).
- L317: Option C: justify beta(n) because it "maximizes orbit length (p-1)".

## ATT-C (L321-...) — Theseus's Ship trajectory
- (d)(j) L333-334: "Over-Constrained Hardware/Alphabet Metaphors: The 7-bit ASCII/Greek alignments, [7,4,3] Hamming torsor coordinates, and hardware register masks were initially conflated with the parent object. They are now recognized as typed source maps (specific discrete apertures) rather than the definition of the arithmetic itself." ** KEY: Hamming [7,4,3] demoted from definition to a typed aperture/source map. Directly repairs Rubicon's treatment of the Hamming code as ontology. **
- L332: "Isolated Decimal Bias: ... (7,10), the repetend 142857, and the two-track lift coefficient 18 = 2(b-1) as unique standalone objects" -> planks replaced.
- L336: invariant keel: z = a + mq + rho, chart as pullback z=bx, a=-h. L337: sum_{h} floor((u+h)/m)=u "a complete finite phase scan is equivalent to all possible integer phase continuations".
- L352-357: pullback chain R_m -> base-shear -> section m=p, B=beta(n) -> GM.
- L364: GM 6,404 terms verified; affine candidate needs new packet.
- (e)(f) L390-399: Sigma maps 42 pairs to 14 attained values, fibers {2:8, 4:5, 6:1} "appeared as an information loss"; Delta(u,v)=q(v)-q(u) "acts as the differential selector (WHO)"; q(u)=(Sigma-Delta)/2, q(v)=(Sigma+Delta)/2; "fiber stratification is not an error, but the signature of a symmetric projection awaiting its dual anti-invariant." ** WHO = differential/anti-invariant selector (orientation), not a Hamming column. **
- (h) L403: q(0..6)=[0,1,2,4,5,7,8] skips {3,6} = gaps of <7,10>; Sigma attains 1..13 and 15, missing 14. L408: Sylvester genus g=(m-1)(b-1)/2=27, Frobenius F=mb-m-b=53 "govern the global volume of this missing space".
- (a) L412-415: step differences of q = lower Christoffel word C(10/7)=[1,1,2,1,2,1] summing +8; Delta_close=-floor((m-1)b/m)=-8; "oint_{T^2} dDelta = 8+(-8)=0 ... zero net curvature flux on the periodic boundary. This bridges discrete difference sequences with continuous torus geodesic flows." [torus appears as T^2 of a discrete periodic chart — note overreach "continuous torus geodesic flows" is commentary; no radii. The only "curvature" is a telescoping holonomy count.]
- (e) L418-425 ** TEN interrogatives as FIVE apposed countercorrelary pairs **:
  1. WHO (Selector/Seed u) <-> WHAT (Attained image q(x)): "Domain choice versus evaluated image."
  2. WHEN (Time/Phase h) <-> WHERE (Space/Seat x/Bound m).
  3. WHY (Boundary invariant/loop integral oint dDelta=0) <-> HOW (Local step bx=mq+y).
  4. WHICH (Fiber stratification/equivalence class) <-> WAY (Direction/differential observable Delta).
  5. WITH (Joint arity/pair sum Sigma) <-> NOT (Complement/semigroup VOID/Unresolved fiber n't).
  [Note: this list has WITH as a 10th item, not "N'T" separately; set = WHO WHAT WHEN WHERE WHY HOW WHICH WAY WITH NOT(n't). Conflicts with ATT-C L395 where Delta = WHO; here Delta = WAY and WHO = seed u. Ambiguity to flag. Rubicon's 7 = these minus WAY, WITH, NOT; Rubicon's 7->H-column mapping has no counterpart here: roles are pairwise (5 dual pairs), not 7 nonzero vectors of F_2^3.]
- L428-441: OEIS core %C(1..7) list. L447: keep GM 6,404-term candidate.
- (b)(d) L451-452: "Preserve Specialized Lenses as Typed Source Maps ... Unicode Greek/ASCII 7-bit congruence, [7,4,3] Hamming torsor, and optical Gram readers ... as declared observational apertures. Treating them as typed projections rather than literal physical causes protects the mathematical credibility". ** lens = typed source map/aperture, explicitly NOT a physical cause. **

## SRC-OPERATOR (L457-...) RELATIONAL_NOTATION_EPOCH_AUDIT.md — HORIZON-FOLD / POST-0 notation audit
- L467-479 governing chain: unlocalized relation -> HORIZON/FOLD -> local zero/reference + typed post-0 notation -> seal/cancel or retained nabla -> return/re-localization. Correction L467: previous audit "incorrectly treated the horizon as merely something that must be declared before an operator is used".
- L483: "The horizon is ... not one more value in the aperture. It is the topological fold that supplies the locality in which a value, identity, orientation, algebra, order, representative convention, or phase can exist." Zero = locally sealed face, "not universal nothing". "a local face may seal while an uncancelled residual remains."
- L485: ordinary symbols = "post-0 notational forms", not parent ontology.
- L490: READ(locality)->FOLD->ROUTE->STRIKE->{CANCEL,RESIDUAL}.
- L494: "a statistic computed inline creates a false epoch; a position-producing operation read through a permutation-invariant fold erases its only product; and a zero result must be diagnosed for cleaving before being called absence."
- (i) L504: "What must not happen at H: assigning distances, weights, thresholds, phases, bases, or meanings by hand." ** direct prohibition against Rubicon hand-set bases 11/15, 4/7, radii 13,3, weights w. ** L505: "a rank-1 horizon reading is a degeneracy, not a universal constant."
- L508-510: 0 = local cancellation/return face; not "global nothing".
- (f) L516: "if cancellation does not close, the uncancelled face is retained as nabla; ... locally closed but not annihilated."
- (e) L520: N'T = counterroute, "not generic Boolean NOT"; "every executable positive head requires a counter-head/route-not-taken"; reversal leaves Sigma invariant and negates Delta.
- L526-537 table of fold-supplied coordinates (identity, source/target, substrate/rung, orientation, ambient bound, order/representative, algebraic law, epoch, inverse coordinate, route/placement "a fold destroys WHERE/arrangement").
- L543-659 operator registry (each: H/0 supplies, local function, cleave if isolated, retained partner, legal epoch). Consequential rows:
  - L553 DIV "can silently discard remainder". L554 power "^": "makes phase/index look intrinsic and can merge distinct exponents with same quotient behavior" [directly relevant to Rubicon base^n depth exponents].
  - L557 mod "deletes winding/quotient history". L561 floor erases fractional displacement.
  - L564 XOR "linearizes; folds are permutation-invariant; drops overlap and route placement".
  - L588 dimension: "equal dimensions masquerade as isomorphism/meaning" [vs Rubicon "3 rows = 3+1 spacetime", "rank-3 metric"]. L587 rank: "equal ranks do not identify maps/semantics".
  - L596 Laplacian: "erases orientation when formed from directed shift" [vs Rubicon H^T H = Laplacian theorem].
  - (d) L597 syndrome/parity: "zero syndrome is a fiber, not necessarily zero word; common tally can be lost". L598 Hamming/code chart: "compressed local chart | one rung can masquerade as universal family | ... only on declared code specialization". ** Hamming is legal only as a declared specialization. **
  - L601 Fourier: selected modes lose phase; only full transform reconstructive.
  - (a) L607 sin/cos/tan: "imports Euclidean angle and can hide orientation/branch | ... after circle/Fourier geometry is selected" ** circle/angle is post-0, needs declaration — relevant to PrePub2 lens cos(6pi/R). **
  - L609 log "branch and base are hidden if omitted". L611 norm "erases direction/phase" (vs ||Hx|| = action). L612 entropy; L614 correlation; L616 mean/total "self-balancing systems make total a conservation law and erase signal arrangement" [vs Rubicon "sum 192 conserved charge"].
  - L619 integral: "can look like a numeric recipe when only a structural constraint is intended".
  - L625 phi "scalar count can be confused with unrelated dimension". L630 binomial "count equality does not transport structure".
  - L638 cyclotomic Phi: "evaluation can be conflated with formal factor coordinate" ** vs PrePub2 cyclotomic chain producing 137, 59, 13. **
  - (a) L646 "torus / mapping torus | periodic action plus gluing | return geometry | endpoint data alone does not determine winding | winding/path class | after periodic gluing is declared" ** torus defined as periodic action + gluing; no radii; winding class retained. **
  - L653 TIME: "inline measurement manufactures false epochs"; partner "ERROR/residual as uncancelled face". L654 ERROR/residual: "uncancelled face of displacement | debug-error semantics can misclassify retained signal".
  - L655 subscript can create "fictitious bounded flow"; L658 arrow "can imply time/causation where only relation/transport exists".
- L665-682 helper-symbol audit:
  - L674 ** "`H` as parity-check matrix | ... collides semantically with fundamental HORIZON and localizes the universal law to one code chart | never use bare `H` in the parent; call it a typed parity map only in proofs" ** — directly bears on Rubicon's H matrix and "Hx=s field equation".
  - L672 `Loc`,`Disp`,`Rel` "asserted mechanisms without source-native maps".
  - L676 F,DF terminal response of "the 142857 chamber" deleted (linearizes one chamber, hides wall crossing).
  - L677 epsilon_cast: "keep the mismatch as an unnamed retained residual at the 6/5 hinge".
  - L680 "`K_6`, `F_2^3`, Hamming | exact finite specializations | one rung can masquerade as the universal family | proof/audit only".
  - L682 numbered L_k succession "reintroduced Cartesian/time order into a simultaneous field".
  - L684: retained parent symbols: Sigma, Delta, nabla; H/Z/N'T as fold/counterroute roles.
- (f) L690-713 residual table: ADD/Sigma needs Delta; mod/rem needs wrap ("source = modulus·wrap + rem"); "remainder is the next carrier state"; XOR needs AND carry; "parity / syndrome zero | codeword/leader/common tally | zero local address does not imply zero word"; "zero-sum filter ... designed cancellation, not evidence of absence"; "norm/magnitude | direction/phase | energy return is not oriented return"; "aggregate total/mean | arrangement/WHERE | self-balanced total is the conservation law"; "equality is a collapsed face of the residual relation"; "FOR/AFT/UN reconciliation | retained mismatch | failure of local reconciliation is the signal, not a defect to normalize away".
- L717-721 Cancellation rule: valid only when every coordinate needed for inverse/next locality is (i) returned, (ii) retained as nabla, or (iii) proved irrelevant to declared target.
- L730-791 implementation passes. L736 "If these are not available, leave the post-0 operator unresolved rather than inventing values." L753 CLEAVER flag for permutation-invariant aggregates. L756 reversible local readings. L760-770 Pass 7 zero classes (native identity, zero-fringe, syndrome/kernel fiber, zero-sum, conservation, empty output, instrument cleave). L779 Pass 9 "Only native annihilation can be deleted. Projection-only cancellation remains attached ... eligible to become the next locality." L782 Pass 10 "Never turn the rung into a free parameter while holding the substrate fixed." ** L786 Pass 11: "Equal counts, shared carriers, equal dimensions, identical zeros, or familiar glyphs do not join categories. Require an exhibited map that preserves the operation being compared and state what it forgets." ** (kills Rubicon's numerological joins: 168=PSL(2,7) -> gauge groups; 3 rows -> 3+1D; 0.033 = Pantheon+ step.)
- L796: 9=PRESENCE and 0=VOID "outer/local chart faces, not additional scalar capacities in the 8…1 matrix".
