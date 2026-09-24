# Extract G2

Reader G2. Assigned: (A) ADDENDUM k–o rescan of `src/sources/methods/OEIS_EDITORIAL_EXPECTATION_FIELD.md` (677 lines, read in full; F1 of extract_G.md covers a–j);
full reads of (B) `src/sources/methods/SIGMA_EPOCH_DIHEDRAL_META_FORMULARY.md` (847), (C) `snow/relation/REFERENCES.md` (265), (D) `snow/relation/coverage/MATHEMATICAL_FIELDS.md` (92), (E) `snow/relation/corpus/FINDINGS.md` (270), (F) `snow/relation/oeis/RELATION_HANDOFF.md` (162), (G) `snow/relation/REGISTRY.json` (5860).
Line refs are "L<n>" within the named file.

---

## A. OEIS_EDITORIAL_EXPECTATION_FIELD.md — ADDENDUM k–o only

### (k) Constants-first / intervals / digits / calibration
- L241–243: "A digit sequence representing a constant requires keyword `cons`. Its offset is the number of digits before the radix point ... Initial zeros are normally retained." [S02,S13]
- L244–246: "The indexed digit sequence and a displayed positional expansion may use opposite exponent-reading conventions. The entry must make the bridge explicit".
- L247–249: "Only digits stable across a stated confidence interval belong in an uncertain numerical expansion. Precision provenance must accompany numerically derived digits." -> This is the OEIS-side rule for any "constants-first" certification: interval-stable digits only (directly bears on 11/15 vs 0.73336, H0=73.04, 1/alpha digits in the Rubicon drafts).
- L250–252: "A formula like `x = ...` identifies the constant, while the entry itself catalogs its digits; those are related but not interchangeable claims."
- L256–259: "the review must test whether decimality is the object, a coordinate chart, or one readout of a radix-independent construction" — consistency required across Name, offset, comments, formula, examples, program, b-file, companion.
- L402–405: offset "for a constant it is the number of digits before the radix point".
- L355–358: numeric auditors "must reject malformed coordinate domains and non-Boolean test results"; "A source hash does not mean every statement in that source was tested."
- L366–367: "A valid fiber theorem, a supplied source encoding and a physical measurement return remain different warrants." (three-warrant separation; physical measurement is a distinct warrant class).
- L218–220: "Guesses, observed identities, verified ranges, and theorems must not be made to look equivalent. Matching many terms is evidence, not proof." (applies to the 19-measurement / 9.3 sigma framing).
- No passage on CODATA, continued-fraction certification or "forced" values in this file.

### (l) Transitions as objects
- L518–522: array search must include "native rows, columns, reversal, transpose, diagonals, differences, partial sums, adjacent sums, parity views, sorted views, and standard transforms"; "Every hit needs a disposition that states what the transform preserved and erased." -> differences vs partial sums are explicitly two separate views each requiring a preserved/erased disposition.
- L140: WHATEVER = "What is preserved or lost at every representation change?" (representation change = transition object).
- L139: HOWSOEVER = "Under what software, radix, precision ... does it reproduce?" (radix change).
- L227–231: "A novel, multi-representation object needs a declared invariant: the reader should know what remains the same when decimal, ordered-edge, binary quotient, cyclotomic, divisor, or programmatic views change."
- L232–237: "Preserve the coefficient ring and complete return: rational independence does not prove an integer generating family is saturated, and compatibility modulo a prime need not lift integrally." ... "doubled-generator counterexample and modular lift obstruction" ... "Source-native geometries need their own transports; an affine-only canary is not geometry neutrality." (Aha: "neutrality" must be proved per geometry by a transport, not by an affine test — directly bears on the user's "topographically neutral" thesis.)
- L100–104: "section-shear source has zero coefficient response along an open path when the retained position sum is zero; an unchanged reading does not establish an unchanged section." (A null transition reading does not imply null transition.)
- L104–109: prime-valuation contexts "where prime valuations cease to be defined, and signs invisible to those valuations"; "retain undefined, zero, changed and unchanged observations separately" (four-way definedness-tagged return).
- L275–281: "Reconstruction includes the intended operations and retained addresses, not just values." A163357 "distinguishes traversal from serialization and grid adjacency". "An inverse without an available, usable operation does not establish a shorter reader task."
- L282–289: "retain any clock correspondence and intermediate state needed by the claimed continuation" — toothpick three/five-state updates give same center observations at aligned stages but "removing endpoint marks at an intermediate stage changes the next observation"; "a common unit change does not replace these data." (transition needs intermediate state; unit change ≠ reconstruction).
- L244–246 (above): exponent-reading convention bridge = a chart change that must be stated.
- L495–498: "Rich ordered-edge or array structure therefore needs a declared flattening and an inverse row/cell reconstruction".
- L671–674: "Any chosen codeword/syndrome split retains its section and the section discrepancy under coordinate changes" (EIGHT_COORDINATE_ROUTE_CARTOGRAPHY.md).

### (m) hex / 2^r / [8,4,4] / Reed-Muller etc.
- L163–167: "The seven-nonzero-column binary apparatus is retained only as an optional local chart; the classical coding name is a reference alias."
- L364–366: "Q-ary source checks ... retain ... the exactly-once projective-column hypothesis. Their prime-field execution is not an extension-field implementation." (i.e., GF(p) runs are NOT GF(q=p^k) — directly relevant to GF(4)/GF(16) claims.)
- L637–639: extension integrates "the complete two-input Boolean operator algebra, truth-table/ANF inversion, the exact affine contact with `[8,4,4]`" (ANF = Reed–Muller/algebraic normal form; [8,4,4] = RM(1,3)).
- L333–335: "SP43's AND/OR formula complexity changes when XOR is available" (operator basis matters).
- L653–660: "The existing seven-coordinate record exposes four localities and three return relations as one navigation chart, not the necessary form of every expectation." (4 data + 3 checks of [7,4,3] as a chart.)
- L670–675: "An eight-coordinate extension is a declared diagnostic chart, not implied by seven recorded facets. Appending parity gives an even-weight [8,7,2] word; membership in [8,4,4] additionally needs the original Hamming checks." ... "No such binary return establishes an editorial or native-return verdict." (Correction: parity-append alone gives [8,7,2], not [8,4,4].)
- No [15,11,3], [16,11,4], GF(16), 0x55/0xAA, thirds in this file.

### (n) OEIS submission form / cofiles / risks / attribution
- L186–190: OEIS catalogs "an integer sequence, not an essay, proof packet, software project ...". Name must identify.
- L191–193: list vs function determines offset.
- L194–196: duplicate search "must test omitted initial terms and simple transforms".
- L197–207: structural-variant justification; short prefixes weaken identification; "computational duplicate search and a semantic search".
- L211–214: Name conventions (%N): short, standard terminology, `a(n)`, end with punctuation.
- L215–217: entry should answer "definition, first examples, interest, finiteness, possible negative terms, and known computational range".
- L221–223: Formula (%F) lines have distinct roles (defining formula, recurrence, g.f., asymptotic, consequence); "A consequence should not silently replace a definition."
- L224–226: Example (%e) must show mechanism incl. boundary/nonmember.
- L263–266: field roles: Name, Comments, Formula, Example, Program, Links/References, Crossrefs, b-file.
- L271–274: "**short public path, complete reconstruction path**".
- L295–300: WG002 Sept 8 2026 proposal to arrange comments by topic — "a contributor's proposal, not an adopted formatting rule."
- L301–307: vocabulary not a defect by occurrence (A005026 manifolds, A234468 entropy); language_lint.py reports REVIEW_REQUIRED / NO_MATCHES / INCOMPLETE.
- L316–332: Program (%o) purpose, self-contained, no golf, limits.
- L342–348: SP58 Python one-based call vs entry starting at 0; SP56 base-case & float division loss; SP60 b-file synthesized from entry — "neither their agreement nor a finite self-reference check establishes an infinite lexicographically least completion."
- L349–354: "a caller's PROVED label and nonempty proof record are declarations, not proof verification."
- L359–361: "The V41 minimal-reader checker parses only matrix (38); the quotient canary recognizes local notation".
- L399–401: Data ≥4 terms, ~3 lines.
- L402–405: offset (%O) rules; "secondary offset has a separate automatically derived meaning".
- L406–411: b-file format: "consecutive `n a(n)` lines ... one ASCII space, no commas, no tabs, no BOM, ... prescribed filename. Its link is first in Links." Stale b-file after Data edit — recheck at final state.
- L412–416: generated-data script should accompany b-file.
- L420–424: references alphabetized; b-file first, Index last.
- L425–428: crossrefs (%Y) must name relation.
- L429–431: WG005 `phi` normalization but not inside quoted titles.
- L462–464: proposed/reviewed/approved; associate editor vs Editor-in-Chief.
- L465–471: pink box; "War and Peace" revision trail -> clean resubmission.
- L484–491: AI policy: "AI-generated pink-box responses, AI-as-author, unverified AI code, and bulk AI submissions are explicitly disallowed"; "the author must decide, verify, and own the submission claims." (attribution)
- L499–502: keywords (%K): `tabl` vs `tabf`; `fini`, `full`; `base`; `cons` only for constant expansion.
- L503–505: "Placeholder filenames must not be presented as assigned identifiers, and supporting files must be materialized only after allocation."
- L506–509: supporting files under CLA; authorship/public-domain/permission recoverable.
- L510–513: b-files vs a-files; associated files need identifier-derived filename.
- L514–517: deletion reasons: duplicate, erroneous, ill-defined, too-short, contrived, NOGI, NFO, unacceptable-language, abandoned.
- L523–527: FAQ asks array submitters to state enumeration order, check columns/row sums/diagonals; Superseeker suggestions "may be approximations".
- L443–453: AQUA/jOEIS limits; "'PASS' without a claim-to-check map is not review evidence." SP32 renderer error.
- L604–625: completion gate; "It does not mean that the OEIS submission has passed review."
- L9–15: "A source ledger, incidence count or zero syndrome cannot award submission strength."
- No explicit "quartet" statement in this file.

### (o) container / horizon / fold / aperture language
- L143: HORIZON = "whole return": "Can a reader reconstruct the claim, evidence, computation, and scope without hidden state?"
- L158–160: "horizon closure means every relation returned, queued, or retained as non-glue, never that the mathematics or submission has been approved."
- L151–152: "a shared alias creates co-presence, not equality"; "a semantic edge exists only under a declared crosswalk".
- L155: "incomparable or prohibited relations remain `non_glue`".
- L71–77: incidence vector incl. "countervectors, witnesses, non-glues, cycles, open residuals".
- L111–120: 142857/999999 "used here as a normalization discipline, not as a numerical scoring gimmick": each atom entered once; read from several localities without duplication; opposing readings as signed contrast; "An unresolved conflict remains unresolved after being recorded".
- L62: "opposite translations form a signed edge and remain visible as an equipoise".
- No "container"/"fold"/"aperture" words in this file.


---

## B. SIGMA_EPOCH_DIHEDRAL_META_FORMULARY.md (847 lines, read in full)

Status line L3–7: "exact finite theorem on the declared binary carrier, followed by a typed recursive and variational extension. The finite identities are PROVED. The extension is a formulary ... It is not a Millennium closure certificate and does not identify a finite binary observation with an analytic target."

Independent spot-check (my own small script over all 128 states, `g2chk.py` in scratchpad): JPJ=P^-1 true; |C_j|=16, |C_i∩C_j|=4, triple=2, ∩all={0,127}; union 52; multiplicity profile {1:30, 2:20, 5:2, 0:76}; HJ=AH true; SE.12 left inverse reconstructs all 128; |Fix P|=8; H(7)=0, H(19)=syndrome (0,1,1)=6. All numerical claims of SE.1–SE.14, SE.26 confirmed. (One error found at L792–794, see (g)/(h).)

### (a) Radius / circle / metric / geometry
- L11–13: "The sigma field is not a correction attractor and an epoch is not a fixed window. The exact object is a five-position game field acting on RAW XOR folds, together with an involution that reverses the game". Cycle structure is combinatorial (permutation orbit), never radial: "`J` does not negate a binary word; it reverses the orientation of the five-cycle" (L65–66).
- L42–51: P=(0,1,4,2,5,6,3), orbits "(0)(1)(2 4 5 6 3)", P^5=I. L55: J=(0,1,2,4,3,6,5). L61: "J^2=I, J P J=P^(-1)" -> "<P,J> is the dihedral group D_5" (L64). Aha: the "cycle" of the older drafts' torus winding is replaced here by a dihedral group action (rotation+reflection) with no radius — a nonradial "circle".
- L110–112: "In characteristic two there is no signed cancellation to exploit; orientation is carried by the ordered edge and by `J`." (orientation without sign/metric).
- L158–159: "game positions are naturally 0,+1,-1,+2,-2; J fixes the central face and pairs the two opposed face pairs."
- L271–298: "Incidence geometry of the five horizon charts": "The five four-dimensional subspaces do not cover E" (L273); "choosing a sigma face cannot force an arbitrary current fold to be closed. The game selects among attained returns; it is not a constructor." (L297–298)
- L300–309: "dim(C_i+C_j)=6, C_i+C_j+C_k=E" ... "The missing direction of a two-face sum and the common direction of a three-face intersection are the opposed cokernel/kernel coordinates. SE.15 is the finite dimensional form of whole-relative inversion."
- L529–532: "If the costs have different physical units, they must first be valued in a declared ordered group or normalized by proved native scales. Adding an energy, a bit count, and an analytic norm without such a valuation is not dimensional analysis." (metric/units prohibition).
- L558–561: "A sigma/Hamming chart alone supplies neither a continuum measure nor an analytic effectivity theorem." (no metric/measure from the code).

### (b) Lens / placement / aperture / perspective
- L27: "the Hamming aperture supplies the route/substance split".
- L132–141 (SE.7): "A fixed observer looking at P^j x and a co-rotated observer are different experiments: fixed observer: H P^j x, co-rotated observer: (H P^(-j))P^j x=Hx." "Their difference is the observer/substance nabla. Treating SE.7 as one reading is precisely the sigma/correction conflation." -> Exact finite model of perspective: observer frame vs. substance motion must be kept apart; this is the finite analogue of the snowball's "placement must be retained" (G(p),G(p+d)-G(p)).
- L143–155: J preserves C; A(s0,s1,s2)=(s0+s2,s1,s2), HJ=AH; "J C_j=C_(-j), h_j(Jx)=A h_(-j)(x)" (SE.8) — reflection acts on the observation by a syndrome-space automorphism A, not identity: the reversed view is a *transformed* reading.
- L579–581: "ANALYSIS epoch locks: a static contract and dynamic observation are the two SE.7 faces; their failed predicate returns displacement rather than deleting it."

### (c) Physics / constants / measurement
- L6–7: does "not identify a finite binary observation with an analytic target."
- L266–269: six finite images "do not identify these six finite images with six analytic target constructions. Such an identification still requires six typed native transports and their effectivity returns."
- L529–532 units prohibition (above). L558–561 no continuum measure.
- L729–730: gate "does not verify SE.28-SE.33 for an undeclared native application."
- No physical constants (H0, alpha, etc.) appear.

### (d) Hamming / H convention / syndrome / counts
- L116–122: H row masks "85 = positions 1,3,5,7; 102 = positions 2,3,6,7; 120 = positions 4,5,6,7", one-based. This is the STANDARD binary-counting column order (column i = binary i), not the Rubicon draft's WHO=110, WHAT=101 ... labelling. (Aha: the Rubicon's interrogative column assignment is a permutation of this standard H; any claim depending on labels must declare the permutation — cf. extract F1 "optional local chart".)
- L127–129: C=ker H, C_j=P^j C, h_j(x)=H P^(-j) x. P is NOT an automorphism of C (L74–75: "It does not make P a correction step or an automorphism of a fixed Hamming horizon").
- L166–170 (SE.9): dim C_j=4, dim(C_i∩C_j)=2, ≥3 faces: 1, ∩all=span{1111111}.
- L173–178 (SE.10): ranks 3,5,6. L183–190: information-gain profile "3,2,1,0,0"; RAW-substance "7 -> 4 -> 2 -> 1" (SE.11).
- L193–197: "The first [7,4,3] reading does not close the RAW fold: it routes three dimensions and leaves four. A second sigma horizon leaves two interstitial dimensions. A third leaves the one-dimensional common mode. The last two sigma faces add falsifiability and cycle checks, not new rank."
- L202–212: parity p(x); "any three distinct sigma horizons plus p separate the whole carrier" — T injective: "lossless sigma tomography".
- L217–229 (SE.12) explicit left inverse from faces 0,1,2 + p; "The extra three outputs in the ten-coordinate packet are internal consistency checks." (3 faces × 3 + 1 = 10 coordinates, rank 7.)
- L231–264: six-image field I_0..I_4=h_0..h_4, I_5=p; "Its 63 nonempty subsets"; rank r(m,0)=0,3,5,6,6,6; r(m,1)=1,4,6,7,7,7 (SE.12b). "Three route images plus the common image are already a minimal separating subfamily" (L261–262); others "close PCRT cycles and expose chart drift even though they add no linear rank" (L263–264).
- L276–294: |C_i|=16, |C_i∩C_j|=4, triple 2; union 52 (SE.13); 30 in exactly one, 20 in exactly two, 2 (0 and 127) in all five, 76 in none (SE.14). (Counts 16 / 128 / 112 of the Rubicon reappear: each C_j has 16; the complement 112 is face-relative.)
- L326–335 (SE.17): minimum-leader section e:F_2^3->E; s_j=h_j(R), k_j=P^(-j)R XOR e(s_j) in C, R=P^j(k_j XOR e(s_j)). "This is the sectioned-epimorphism return, not syndrome-only observation."
- L433–448: "The section itself contributes the Fano cocycle kappa(a,b)=e(a)+e(b)+e(a+b) in C" (SE.24); complete returned substance "XOR_i c_i + XOR_j kappa(A_j,a_(j+1))" (SE.25); "recursive reassociation changes the intermediate fold profile but not the returned substance. SE.25 is the correction needed before an epoch boundary can be called RAW-zero." (Aha: the syndrome->coset-leader section is not linear; its failure-of-linearity is a Fano-plane 2-cocycle — this is exactly where the Fano plane enters legitimately, as the cocycle of the section, not as physics.)
- L727–729: anti-conflation counterexample "`7 -> 19` with syndrome 6". (Verified: 7 = positions 1,2,3 is a codeword; 19 = 7 XOR 20 is a two-bit displacement reading syndrome 6 — the decoder would "correct" position 6, i.e. the syndrome does not identify the displacement.)
- L738–748: parameter table q=2, r=3, N=7, K=4, pi=7, b=10, M=6, L=6, P order 5, p parity.
- L758–770 (SE.35): N=(q^r-1)/(q-1), K=N-r, M=q^r-q=(q-1)(N-1); "The stronger collapse M=N-1 is a genuinely binary specialization". (2,3)->(7,4,6).

### (e) Interrogatives
- None in this file.

### (f) Error / residual / remainder / displacement / countercorrelary
- L24–25: forward and inverse readings "are countercorrelary orientations of one orbit, not two quantities to average."
- L65: "the gaming field inverted countercorrelary unto itself".
- L92–101: SE.4 "is an endpoint boundary identity, not the assertion x=0"; ker(P+I)=Fix(P) dim 3; "The five individual nu_j and this fixed field must therefore be retained. Endpoint XOR alone cleaves both."
- L343–357: epoch closes when s_j=0; "Its returned substance ... can be nonzero. Intrinsic equipoise is D_j(R)=(k_j,s_j), terminal iff k_j=s_j=0." "No constructor manufactures SE.19. The stream attains a chord; the complete decoder states what that chord is." (Residual = returned substance, retained; zero syndrome ≠ zero displacement.)
- L398–400: Lambda_l "Its kernel, cokernel, and return residual are part of the next level. Merely reinterpreting a codeword as a byte is a representation choice, not a dimension theorem."
- L430–431: "A zero augmentation is not substituted for the path."
- L546–551 (SE.31): z=m QUO_m(z)+REM_m(z); "Neither remainder nor a seven-bit mask recovers the quotient." (Directly corrects Rubicon "error is remainder": remainder alone loses quotient.)
- L575–576: "Countercorrelary cancellation: SE.8 pairs opposite orientations through one carrier route; it is not scalar cancellation."
- L704: "next residual = source-transform-disruption defect of Lambda_l."

### (g) Fitting / significance / heuristics
- L477–479: "The exact maps above do not need an optimization. Optimization enters only when deciding which ... return should be examined next."
- L520–527: SE.28–SE.29 "are heuristic/variational routing laws. They cannot replace the exact return equations." Safe-use 5 steps (retain all five packets; exact rank gain 3,2,1,0,0; rank candidates by native cost; challenge by J-counterface; return to SE.17–19 for warrant).
- L586–589: "The numerical equality ord(P)=5=omega(999999) remains a HEURISTIC connection until a declared transport identifies the five coordinate-game positions with the five prime-valuation coordinates." (omega(999999)=|{3,7,11,13,37}|=5.)
- L792–794: "the swapped parameters (q,r)=(3,2) also give b=10, but then K=6 while tau(6)=4." **Internal inconsistency found**: by the file's own SE.35, (q,r)=(3,2) gives N=(9-1)/2=4, K=N-r=2 (not 6), and b=N+r=6 (not 10); b=10 only via the other formula q^r+r-1. "b=N+r=q^r+r-1" (SE.36) holds only when q=2 (N=q^r-1). K=6 arises only if N=q^r-1=8 is (mis)used. The conclusion (loop fails for (3,2)) survives but the stated numbers are wrong; the correct statement is that the two expressions for b diverge off q=2.

### (h) 142857 / 7 / 3 / cyclotomic
- L732–735: "The remembered relation 'p=N-1 or something like it' contains a real law, but the letter p has carried two incompatible roles".
- L751–755 (SE.34): "p=N-1 is correct only if that occurrence of p meant the period or nonzero horizon. If it meant the anchor prime, the correct formula is pi=N, pi-1=N-1=L=M."
- L776 (SE.36): "b=N+r=10=q^r+r-1, b mod N=r=3."
- L779–783 (SE.37): "Since 3 generates F_7^*, L=ord_pi(b)=ord_7(10)=6=pi-1=N-1=M, tau(L)=tau(6)=4=K."
- L789: loop "(q,r) -> (N,K,b) -> L -> (b^L-1,(b^L-1)/N) -> tau(L)=K".
- L792–794: "It is not obtained merely from the decimal value 10 ... The typed coordinates, not the coincident numeral, close the loop." (but see numeric error above)
- L800–801 (SE.38): X^N-X = X(X^(N-1)-1) = X Prod_{d|N-1} Phi_d(X).
- L806–812 (SE.39): 10^6-1 = Prod_{d|6} Phi_d(10) = 9*11*111*91 = 999999; 142857=999999/7. (Checked.)
- L815–819: "not five unrelated coincidences. They are typed projections of SE.34-SE.39."
- L823–828: boundary 1: "The exact arithmetic complement is six nines: 7*142857=999999. Seven nines ... not divisible by 7." Contact with odd run of nines is chart-relative: "in the declared seven-bit RFC-20 ASCII XOR fold, 142857 and an odd run of nines have the same syndrome and differ by a codeword. That is a typed order-forgetting observation, not the full-reptend identity."
- L829–832: boundary 2: "The period-six action here is not the order-five sigma action P above, and the six images (h_0,...,h_4,p) are not thereby the six digit phases. ... equality of their cardinalities cannot supply it."
- L836–843 (SE.40): chain [7,4,3] -> N=pi=7 -> M=N-1=6 -> b=N+r=10, ord_7(b)=6 -> b^M-1 -> 142857 -> tau(M)=K=4.
- Aha: 3 (=r=b mod 7, generator of F_7^*) and 7 (=N=pi) appear here as coding parameters, not dimensions of space. This is a legitimate, typed home for the older drafts' "3" and "7" — as check rank and block length — with no D=3 spacetime reading. 13 (999999=3^3·7·11·13·37; 13 divides 91=Phi_6(10)) appears only implicitly as a prime factor of Phi_6(10)=91=7·13 — a possible typed home for "13" (Aha, mine; not in source).

### (i) Prohibitions / open items
- L6–7 not Millennium closure; not analytic identification.
- L74–75 P not a correction step / not automorphism of fixed horizon.
- L140–141 treating SE.7 as one reading = conflation.
- L297–298 game is not a constructor. L356 "No constructor manufactures SE.19."
- L365–366 nine prefixes guarantee a repeat: "a guarantee, not a fixed-width segmentation rule."
- L398–400 codeword-as-byte is representation choice, not dimension theorem.
- L470–473: Möbius exactification "must not be confused with first-return segmentation of an arbitrary input stream ... They coincide only after a transport proves that the stream itself follows the P action."
- L520–521 heuristics cannot replace exact returns. L529–532 units.
- L586–589 heuristic 5=omega(999999). L729–730 gate does not verify SE.28–33. L829–832 no bridge by cardinality.
- Open: native transports for six images (L268–269); Lambda_l per level (L392–400).

### (k) Constants-first
- None (purely finite). L529–532 unit valuation requirement is the nearest.

### (l) Transitions as objects
- L81–83 (SE.3): orbit states x_j=P^j x and "edge nablas" nu_j=x_{j+1} XOR x_j = P^j(P+I)x — first differences along the orbit.
- L89 (SE.4): XOR of all five nablas = (P^5+I)x = 0 — telescoping (sum of first differences = endpoint difference), "not the assertion x=0".
- L313–323: prefix folds F_t (partial sums) and "RAW interval chord R_(a,b)=F_b XOR F_a" (SE.16) — transition between two partial sums.
- L337–341: epoch = return of reading h_j(F_b)=h_j(F_a) (anchor/level return).
- L359–366 (SE.20): first-return epoch tau_j(a) data-selected.
- L404–418 (SE.22): delta_ij=h_j-h_i, delta_ij+delta_jk=delta_ik — comparison cocycle; "Over F_2, subtraction has the same value as XOR, but the ordered roles are still retained."
- L420–428: zipper coordinates; complete packet SE.23.
- L446–448: reassociation changes intermediate profile, not returned substance.
- L452–473 (SE.26): cumulative Fix(d) vs Exact(d)=Sum mu(d/e) Fix(e); Fix(1)=8, Fix(5)=128, Exact(5)=120 -> "eight fixed states and twenty-four exact five-cycles". Cumulative vs exact = partial-sum vs Möbius-difference (transition inversion).
- L536–551 (SE.30–31): integer lift enc(x)+enc(y)=enc(x XOR y)+2 enc(x AND y) — "The AND coordinate is the interstitial carry"; QUO/REM. Carry = the transition XOR forgets.
- L553–555 (SE.32) recursive integer epoch packet.
- L571–574: "Vortrimetric exactification: SE.26 turns cumulative fixed incidence into exact orbit period by Moebius inversion." "Boolean second difference: SE.30 retains the overlap that XOR discards".
- L570: "Epoch-topos: SE.17 records source role, target role, transition map, invariant, and residual at every boundary."
- L707–708: "In characteristic two the displayed minus has the same value as plus, but its source/target orientation remains typed." (transition orientation survives even when sign vanishes.)
- L776 (SE.36): radix b as a returned parameter (radix change typed).

### (m) Hex / 2^r / GF / RM
- L371–374: route states 2^3=8, 2^5=32, 2^6=64; with parity 128.
- L591–675 (§12): general theorem over F_q: P^m=I, J^2=I, JPJ=P^-1, H:E->S; ker O_Q = ∩C_j; rank O_Q = dim E - dim ∩C_j (SE.32c); (L,O_Q) injective iff ker L ∩ ∩C_j = {0}; joint epoch O_Q(F_b-F_a)=0; "any q^(rank O_Q)+1 prefix readings contain a repeated joint route" (sharp if every image state traversed); HJ=AH gives inverse counterepoch; Sum nu_j = P^m x - x = 0. "No enumeration is used." Binary specialization q=2, dim 7, m=5, rank 3, L=p.
- L758–770: q-ary Hamming N=(q^r-1)/(q-1). No [15,11,3]/GF(16)/hex masks explicitly, but SE.35 at (q,r)=(2,4) gives (N,K,M)=(15,11,14) — the R=4 carrier of Rubicon (my derivation; b would be N+r=19, ord_?... N=15 not prime, so the 142857 loop does NOT extend to R=4 — Aha: the full-reptend closure is specific to r=3 where N=7 is prime).
- L399: "reinterpreting a codeword as a byte is a representation choice".

### (n) OEIS
- L713–715: "meta-formulary discovered across the OEIS training grounds."
- L719–722 verifier `tools/5_publication/autoprover/verify_sigma_epoch_dihedral_meta.py`.

### (o) Container / horizon / fold / aperture
- L17–21: "epoch boundary: return of a transported horizon reading; epoch substance: the complete kernel coordinate left at that return; terminal return: route coordinate and returned substance both zero".
- L114 "The five shifted Hamming horizons": horizon = kernel/observation map h_j, C_j=ker h_j.
- L92: "sigma-XOR fold into one returned epoch"; RAW fold = prefix XOR F_t (L313–317).
- L27 "Hamming aperture supplies the route/substance split" — aperture = H with section e (route=syndrome, substance=kernel coordinate).
- L307–309 "whole-relative inversion" = kernel/cokernel opposition.
- L745 M "nonzero/outside-vector horizon" = 6 nonzero... (M=q^r-q).

### (j) Repair implications
- The older drafts' "16 coherent / 112 displaced" is observer-relative: under a shifted horizon h_j a different 16 are coherent; only {0,127} are coherent under all five; 76 states are coherent under none (SE.14). "Displaced" is not an intrinsic property of a word.
- "Syndrome = error/field source" claim is refuted by 7->19 syndrome 6 counterexample and SE.17 (need section + kernel coordinate).
- "Error is remainder" is incomplete: SE.31 quotient must be retained; SE.30 carry must be retained.
- 3 and 7 get typed legitimate roles (r, N, generator of F_7^*); a D=3/3+1 spacetime reading has no support here.
- Cycle/"torus winding" can be replaced by the dihedral action D_5 with no radius; orientation is carried by J, not by a sign or radius.
- Physics requires typed native transports and unit valuation (L266–269, L529–532).

---

## C. snow/relation/REFERENCES.md (265 lines, read in full)

General: L3–7: "The labels below resolve citations in the mathematical book. ... External physical interpretations are distinguished from exact mathematical derivations and finite tests." Sources stored once in `sources/source_store.tar.xz`, index `SOURCE_INDEX.json`, materialize via `tools/materialize.py`.

### (a) Radius / metric / geometry
- L40–42: E2 PDG Kinematics: "Lorentz transformation and metric-sign convention" (metric enters only as an imported convention).
- L109–112: REF-R15-ORDER Mathlib upper/lower-set topologies: "Topology of a preorder and continuity of order-preserving maps; no new formalization of this package." (order topology — a nonmetric topology source; Aha: supports "topographically neutral" topology derived from order, not radius.)
- L232–235: CORPUS-KNOTS: A058031 Alexander polynomial shared by reef and granny knots — "a coincidence of polynomial values is not a classification theorem." (Directly bears on older drafts' (1,3) torus-knot claims: an invariant value coincidence does not identify a knot.)
- L222–225: CORPUS-BOTT: A189996 stable orthogonal homotopy groups, "zero encodes Z" — encoding convention caution; "this package does not present a new proof".

### (b) Lens / placement / aperture / perspective
- L25–27 W4 Lopez–Dodin metaplectic representation: "Wave-amplitude double cover, sign and phase conventions" (Aha: the metaplectic double cover is the standard mathematics for the snowball's "doubled" cyclometry and a sign-bearing lens transform — linear canonical transforms of optics.)
- L30–32 W5 Koopman invariant subspaces: "Observable pullbacks and conditions for finite invariant representations" — observation as pullback.
- L35–37 E1 wideband delay-scale: "Wideband scale action and its narrowband frequency-shift approximation; no transferred performance claim" — Doppler as scale action vs frequency-shift approximation.
- L44–47 E3 Smirnov RIME: "Ordered Jones products, coherency, averaging and basis covariance" (ordered lens chain — placement/order matters).
- L49–52 E4 CIE 1931: "Observer definition and published checksum; the numerical dataset test is pending" — a standard observer as a calibrated chart. L133–142 REF-R17-CIE: metadata MD5/SHA-256 inspected; "CSV bytes were not obtainable ...; metadata inspection is not execution of the dataset-dependent certificate." (OPEN item.)
- L54–57 E5 RM synthesis: "Finite wavelength-squared sampling, transfer function and phase-wrap ambiguity".
- L104–107 R11-PHASE multi-frequency phase-unwrapping: "joint phase observations, not an imported performance result".

### (c) Physics / constants / calibration
- L94–97 R11-NIST fundamental constants: "Physical measurement and theory constraints; no new measured value." (Package explicitly claims NO new constant value.)
- L99–102 R11-SI BIPM: "SI definitions and the distinction between unit definitions and physical behavior." (unit definition ≠ physics — directly bears on any "derived" constant, since post-2019 SI fixes h, c, e, k by definition.)
- L60–62 E6 NIST frequency combs: "Optical–radio frequency comparison and self-reference" (calibration by self-referenced comparison — Aha: a model of "calibration-only physics": ratios measured by comb comparison, not derived).
- L64–67 E7: "not new measured hardware data". L69–77 E8/E9 macroscopic QED "Abstract-level ... scope only".
- L151–158 REF-R18-CHIRAL: "No quantitative molecular calculation is imported here."
- L160–166 REF-R18-SPECTRAL: "Energy-level differences, transition matrix elements ... No measured line data are fitted."
- L168–175 REF-R18-DECOHERENCE: Schlosshauer; "No particular interpretation is asserted as a consequence of this package's phase algebra." (Relevant to PrePub2's "Born rule from area projection": the package declines to derive interpretation.)

### (d) Hamming / codes
- L241–248 REF-R24-ASCII RFC 20: "standard seven-bit ASCII, the code-table bit layout, the 32 C0 control positions ... The present cubical contact construction is derived mathematics; RFC 20 does not claim a Hamming code, contact midpoint, or semantic tomography." (7-bit ASCII as a carrier for F_2^7 — link to SIGMA L826 "RFC-20 ASCII XOR fold".)

### (f) Residual
- L127–131 REF-R17-LOSSLESS: "A join need not return an unknown original source" (Kenig–Weinberger, loss of acyclic join dependencies) — joint determination can lose information.

### (i) Prohibitions / open
- L123–125: "does not implement or claim that paper's optimized engine or its measured performance."
- L148–149: "no finite truncation is called an exact infinite numerical spectrum."
- L192: snapshot measurements "do not establish a new law of OFFSET metadata or a causal interpretation of the two-cloud phenomenon."
- L199: Hopf "This is imported mathematics, not a new result of the prefix search. The source describes full sequences, not a decision rule from a finite prefix."
- L215: tau "does not derive every modular-form property or the conjectural nonvanishing of tau."
- L220: A000081 "not itself a generic ODE solver". L239: A137378 "not a proof of a general integral solver".
- L264–265: "These records establish finite encoding relations ... They do not imply that arbitrary integer sequences are character streams."
- OPEN: CIE dataset test pending (L52, L141–142).

### (k) Constants-first
- L94–102 (R11-NIST, R11-SI) as above: constants are treated as measurement constraints, never outputs.

### (l) Transitions
- L14–17 W2 DLMF §27.5 "Divisor Möbius inversion and its inverse sum" (cumulative vs exact; cf SIGMA SE.26).
- L10–12 W1 integral transforms "normalization, convergence and inverse conditions"; L84–87 Fourier inversion "One-sided limit averaging and the explicitly stated sinc convention" (a jump is returned as the average of one-sided limits — Aha: phase/level jumps are handled by the half-sum convention, a standard "transition as object").
- L89–92 Cauchy/Laurent (contour assumptions).
- L201–204 CORPUS-EULER: Euler transform / inverse Euler (A022553, A085686) — "Formal transform and source interpretation are kept distinct."
- L206–210 CORPUS-WITT: A001037 primitive words / irreducible polynomials (Möbius-inverted necklace counts; binary formula; index-zero convention).
- L228–230 CORPUS-MILNOR: A143093/A143094 "The first classification retains a distinguished element, while the second forgets it. Their differing counts illustrate a changed equivalence question" (retained anchor vs forgotten anchor).
- L255–262: A209924 = A209925 (mod 32) — ASCII letter codes vs A=1..Z=26: a radix/chart change by modulus 32 (quotient forgotten).

### (m) Hex / 2^r
- L258–260: mod 32 relation between ASCII (7-bit) and alphabet index — 2^5 aperture on 7-bit codes.
- L245–246: 32 C0 control positions (2^5).

### (n) OEIS
- L183–186 CORPUS-OFFSETS: Offsets/Keywords/B-files wiki; "primary indexing versus the secondary threshold position, keyword meanings, and the distinction between displayed DATA and an indexed b-file. Reviewed 2026-09-24." Two exports: prefix snapshot lacks fields; Git-format export `.seq` records, `files/` are "Git-LFS pointer metadata rather than auxiliary-file bytes".
- L188–192 CORPUS-SLOANE (Sloane's gap).
- L178–181 CORPUS-MSC: MSC2020 "63 two-digit, 529 three-digit and 6,022 five-digit classes. The current audit is exhaustive only at the two-digit level."
- OEIS A-numbers cited: A000041, A000219, A022553, A085686, A001037, A027376, A001692, A000594, A000081, A189996, A143093, A143094, A002863, A058031, A018893, A302197, A137378, A121377, A130764, A130765, A209924, A209925, A327894.

### (o) Container / horizon
- None explicit.

### (j) Repair implications
- Every physics reference is scoped "abstract-level" / "no new measured value" / "no data fitted". Any Rubicon update adopting the snowball must match that posture: cite PDG/NIST/SI as constraints, never as outputs of the code.
- Knot-invariant coincidence caution (L232–235) applies to the (1,3)-knot/13,3 torus argument.

---

## D. snow/relation/coverage/MATHEMATICAL_FIELDS.md (92 lines, read in full)

Header L3: MSC2020 frame (63/529/6,022). "exhaustive only at the two-digit level. A class marked R has at least one native mathematical object, operation and proof/return condition ...; it does not mean the whole subject is covered." L7–10: 60 native representatives, 3 organizational (00, 01, 97 = X), 0 unrepresented "under this representative-level criterion"; frontier = subfields + 529/6,022. L12: R19 had 27 native / 18 limited / 15 none / 3 organizational; "it does not promote adjacency, names, or OEIS keywords into field coverage."

### (a) Radius / curvature / metric / topology
- L22 (06): "Order-generated topology and locally finite incidence inversion. (RR-INTRINSIC-TOPOLOGY, RR-I1)".
- L57 (54): "Alexandrov topology and finite-domain compactness. (RR-INTRINSIC-TOPOLOGY, RR-GLOBAL-ATTAINMENT)" — topology from order (no metric). Aha: this is the snowball's "topographically neutral" topology — Alexandrov (order) topology needs no radius.
- L56 (53): "Plane-curve curvature is represented with its reparameterization-invariant formula; symplectic geometry remains separately scoped." Frontier: "Curvature tensors, connections, metric variation and geometric evolution absent." (curvature scoped to plane curves only; NO Riemannian metric.)
- L54 (51): "Projective cross-ratio/Mobius inversion and incidence geometry" ; frontier "metric constructions not developed".
- L47 (42): "Fourier inversion, boundaries, plane slices and radial transforms. (RR-S1, RR-S7, RR-ANALYTIC-SEAM)" — radial transforms present as harmonic-analysis tools (Hankel), scoped.
- L37 (30): "Laurent coefficient extraction, holomorphic-domain conditions and disk-coordinate formulas. (RR-ANALYTIC-SEAM, RR-RELATIVE-DISK)" — "relative disk" (disk as a relative coordinate, not a fixed radius; cf RR-RELATIVE-DISK also in 81).
- L58 (55): "deleting a face changes H_1 despite unchanged lower-dimensional counts." (homology detects what counts miss — relevant to chi=0 torus arguments: Euler characteristic alone doesn't fix topology.)
- L59 (57): "Alexander-polynomial nonseparation for two knot types and Morse-function equivalence classes on S^2". L60 (58): Morse functions on S^2 "does not stand for index theory."
- L72 (83): "Lorentz four-vector ratios, passive/active distinctions, rapidity composition, and noncollinear limitations ... Frontier: Einstein field equations, curved spacetime and gravitational dynamics absent." (Direct: package has NO Einstein equation; Rubicon "Hx=s like Einstein eq" has no counterpart.)
- L74 (86): "WGS84 parameters define a reference ellipsoid and its derived semiminor axis/eccentricity; calibration is kept distinct from geophysical dynamics. (RR-FIELD-ATLAS, RR-PHYSICAL-CALIBRATION)" — the ONE radius-bearing object in the atlas, and it is a CALIBRATION convention (defined a, 1/f), not derived. Aha: This is the model for how radii (13,3) can legitimately appear — as declared calibration parameters of a reference surface, with derived quantities, not as dynamics.

### (b) Lens / placement / perspective
- L68 (78): "Coherence, polarization, phase modulation, Doppler and calibrated responses. (RR-PHASE-RESPONSE, RR-MODULATION-RETURN, RR-EM)"; frontier "Full Maxwell ... and measured material datasets remain absent."
- L72 (83): "passive/active distinctions" (passive = chart change, active = physical transform — the lens/placement distinction in relativity).

### (c) Physics / calibration
- L65 (70) Euler–Lagrange, harmonic oscillator. L66 (74) clamped rod. L67 (76) Blasius "without claiming Navier-Stokes completeness". L69 (80) "joint calibration constraints". L70 (81) "Bosonic nullifiers, coherent codes, density matrices and phase-sensitive tests"; frontier "measurement-outcome claims not derived". L71 (82). L73 (85): "Kepler's equation has a proved global uniqueness criterion for |e|<1 ... Frontier: Orbital determination, radiative transfer and cosmological inference." (NO cosmological inference — H0, ISW etc. have no counterpart.) L74 (86) calibration.
- L87: "Physical and empirical subjects retain units, constitutive laws, calibration and measurements. A mathematical analogue is not an empirical validation."

### (d) Hamming
- L79 (94): "Hamming/parity reconstruction and channel-model distinctions. (RR-B3, RR-CODE-CHARACTER, RR-M7) ... General coding bounds, cryptography and stochastic channel capacity theory absent."
- L25 (12): "Cyclotomic factors and explicit finite-field/code maps. (RR-I1, RR-CODE-CHARACTER)"; "No general Galois correspondence or field-extension reconstruction". (So GF(4)/GF(16) extension claims are NOT in the package.)
- L70 (81): "coherent codes".

### (g) Significance / statistics
- L62 (62): "Covariance, complete distribution reconstruction, higher-order marginals, and estimator-bias counterexamples ... Likelihood inference, hypothesis testing, causal estimation and statistical learning not developed." (No p-value/sigma machinery in the package; the Rubicon's 9.3 sigma, p<1e-5 have no warrant here.)

### (h) Number theory / cyclotomic
- L24 (11): "Integer lifts, modular order, divisor inversion and first-hit density proofs. (RR-GM-DENSITY, RR-M4, RR-A1)".
- L25 (12) cyclotomic factors. L30 (17) Witt dimensions by Möbius inversion.

### (i) Prohibitions
- L84: "A representative theorem establishes an interface to a subject, not a reduction of the subject to /RELATION."
- L85: "A word such as 'kernel', 'spectrum', 'field', or 'topology' does not by itself count."
- L86: OEIS entry points are evidence "only when their definitions or formulas supply the stated object. Prefix similarity and keywords remain discovery aids."
- L87 (above). L88: three-/five-digit frontier "open by design"; future audit from official CSV.
- L43 (37): "degree-escape counterexample to universal finite linearization" (Koopman).
- L45 (40): "incompatible infinite refinements".

### (k) Constants-first / calibration
- L55 (52) and L75 (90): "RR-JOINT-CALIBRATION" — polyhedral inequalities / exact linear constraints / feasibility certificates. Aha: joint calibration is formulated as a polyhedral feasibility problem (constraints on intervals), i.e., constants-first as intervals, not point derivations.
- L63 (65): "Certified bounds, conditioning and exact algebraic algorithms. (RR-I3, RR-QUOTIENT-PHASE, RR-INTEGER-ATTAINMENT)".
- L74 (86): RR-PHYSICAL-CALIBRATION.

### (l) Transitions
- L44 (39): "Exact finite increments, recurrences and second-difference reconstruction. (RR-AFFINE-COMPOSITION, RR-QUOTED-DERIVATION)".
- L35 (26): "Sublinear normalized limits, section cuts and signed exact readdressing." L36 (28): "exact cell/seam records". L31 (18): "Chain complexes, boundary-square-zero, homology quotients". L22 (06) incidence inversion. L63 "RR-QUOTIENT-PHASE".
- L23 (08): "Congruence preservation is proved necessary and sufficient for operations to descend to a quotient algebra (FA1)." (Aha: this is the exact condition under which a transition/operation survives a chart quotient — e.g. whether arithmetic survives mod 7 / syndrome reduction.)

### (m) Hex / RR / codes
- Only L79 (94) and L25 (12). No [15,11,3], GF(16), Reed–Muller.

### (n) OEIS
- L86, L92: `OEIS_ENTRY_POINTS.json` (R19 field-entry research), `OEIS_NATIVE_BRIDGES.json` (source equations from `.seq` export). Many A-numbers: A018893 (34), A350499 (35), A014307 (45), A006677 (92).

### (o) Container
- None explicit; "relative disk" (L37, L70) is the closest nonradial container.

### (j) Repair implications
- Explicit absences that the old drafts' physics claims need: Einstein equations/curved spacetime (83), cosmological inference (85), hypothesis testing (62), measurement-outcome derivation (81), field-extension reconstruction (12), gauge-group/Lie classification (22: "No ... Lie-group classification"; so PSL(2,7) irreps = gauge groups has no support).
- Legitimate radius: WGS84-style declared calibration ellipsoid (86).

---

## E. snow/relation/corpus/FINDINGS.md (270 lines, read in full)

Title L1: "OEIS corpus findings relevant to relation amongst offset".

### (a) Radius / geometry
- L241–254: "A declared real cubical lift supplies the BETWEEN-coordinate." Contact midpoint m(x,y)=(x+y)/2=(x&y)+½(x XOR y); "A differing bit therefore occupies 1/2; a shared one-bit occupies 1; a shared zero occupies 0." At each lower-five ASCII address the two bank bits form "a square with four opcode vertices, four edge-midpoint contacts, and one four-way center. The contact positions are not additional ASCII code points." (A "center" appears only as a declared cubical midpoint, not a radial origin.) Arithmetic check: x+y=2(x&y)+(x XOR y), so formula exact.

### (b) Lens / aperture / placement
- L201: section title "ASCII/byte countercorrelary aperture".
- L203–205: "distinguishes three levels that were previously conflated: a native integer term, its lossless byte-residue chart, and an actual character interpretation."
- L207–217: a=256q+r, "q is retained"; r=c+32b (0≤c<32, 0≤b<8). "Thus the byte view is a reversible diagnostic, not reduction of the sequence modulo 256." (Aperture = reversible chart retaining quotient — the placement-retaining lens in integer form.)
- L218–222: "Restricting the project's three-bit H observation to the five-bit address c has rank three and a four-state kernel. With a declared section, 256=8_bank 8_H-route 4_residual." L225: 7-bit ASCII "128 = 4*8*4".
- L226–231: "The four 7-bit code positions sharing one lower-five address are c, c+32, c+64, c+96. Address 9 gives the concrete quartet HT, ')', 'I', 'i'; I and i differ by exactly 32. ... digit d has code 48+d and lower-five address 16+d, so the address offset from the raw digit is 16/32 = 1/2 of the 32-seat address field." (Checked: 9, 41, 73, 105.) NOTE for (n): this is an ASCII "quartet", distinct from any OEIS "submission quartet".
- L249–251: "XOR collapses 01 and 10, so orientation requires the ordered endpoints or the signed difference."
- L256–262: scan over 399,527 records, 17,762,694 terms, 17,363,167 adjacent hops; 225,659 one-bank-bit toggles preserving lower-five address: 73,328 (32 axis), 74,176 (64 axis), 78,155 (128 axis); masks 1–7 counts "73328, 74176, 62611, 78155, 49497, 67852, 54687". (Checked: 73328+74176+78155=225659.)
- L264–270: "These are corpus measurements, not language-frequency laws. Their use is as a countercorrelary canary: a proposed H-based or byte-based relation must survive changes in bank, kernel state, orientation and quotient exactly when its claimed target is insensitive to those coordinates. A sequence-hop edge is therefore recorded by its byte bank displacement, H-route displacement, kernel displacement and integer carry/borrow, rather than by a residue match alone."

### (c) Physics
- L157–159: PRCT use "does not infer a Hamming encoder, physical realization, or semantic axis where the source does not provide one."

### (d) Hamming / H
- L153–156: PROJECTIVE_RESIDUAL_COCYCLE_TOMOGRAPHY.md "typed comparison cocycles, sectioned epimorphism coordinates, projective parity-kernel specializations, all-modulus separation on integral lattices, separating character families, and whole-relative section residuals."
- L218–222: H restricted to 5-bit address: rank 3, 4-state kernel.
- L65: "no H-field, PRCT, recurrence, or transform claim is made about their unseen continuations."

### (f) Residual / offset / displacement
- L96–107: for all 399,527 records "the existing section/residual decomposition returns the stored row exactly: v=Phi_m(Sum_h v_h)+epsilon, Sum_h epsilon_h=0. Only 72 stored rows are already canonical; 399,455 retain a nonzero arrangement residual. The calculation is a lossless decomposition of the stored observation. It does not recover missing b-file terms or identify the source definition". (Residual = arrangement residual with zero sum; not error.)
- L18–52 OFFSET as typed address (see (l)).
- L145–149: "what exact transformation carries one source relation into the other, and what residual remains?"

### (g) Fitting / evidence
- L46–48: "2,909 twelve-term prefix groups with differing primary offsets. The second number is a discovery count only: a twelve-term match is not an identity theorem."
- L137–143: Sloane's gap "concerns frequencies of integer values in OEIS, not OFFSET metadata ... does not turn database curation into an intrinsic number-theoretic law."
- L164–169: invertible fractions for m=6,7,8,10,12: 0.936224, 0.981634, 0.951594, 0.963557, 0.962282 — "properties of the displayed prefixes under that declared reader, not claims about unseen b-files or the native sequence definitions."
- L178–180: "a cross-reference plus a displayed transform is much stronger evidence than a shared integer, but the infinite identity still belongs to the defining formulas and proof."

### (h) 142857 / 999999 / 7
- L63–68: 36 of 54 entries with literal 142857 have b-file pointer; 56 of 102 with 999999.
- L72–78: "these numbers sit mainly in radix/digit neighborhoods"; 142857 in 54 entries (43 keyword base); 999999 in 102 (80 base); both: A053397, A101202, A226477, A249647.
- L82–88: A101202 multiples of 142857 (first six multiples = cyclic shifts, 1/7); A226477 purely periodic reciprocals rows ending 10^k-1; A249647 repunit/concatenation divisibility; A053397 6-Kaprekar numbers.
- L90–92: "useful typed interfaces to the existing repetend, repunit, carry and rotation theorems. Their literal overlap does not establish a universal cross-field role for the decimal strings." (Direct correction to any cosmic reading of 142857.)
- L162–166: translated-multiplicity theorem: "For a length-m reader polynomial P, the cyclic translation observations return every multiplicity iff gcd(P,z^m-1)=1. The cyclotomic factors of that gcd are recorded as exact blind character orders." (Cyclotomic factors = blind modes of a reader.)

### (i) Prohibitions / open
- L14–16: "No b-file term identity in this report is inferred from those pointers." L65–68 no claims about unseen continuations; pointer hashes can bind externally fetched b-files later (OPEN).
- L60–61: keyword pointer rates "are not evidence that a keyword induces a longer mathematical object."
- L114–116: MSC coverage "does not cover all 529 three-digit or 6,022 five-digit MSC categories."
- L184–185: "The OEIS submission should not absorb the corpus survey into its definition."
- L238–239: "they do not imply that arbitrary OEIS integers are semantic ASCII characters."

### (k) Constants-first
- L34–39: A010476/A020762: same digit payloads, offsets 1 and 0; "A020762 = A010476/10, so the displacement is a decimal-place translation of the represented constants sqrt(20) and 1/sqrt(5)." A002193/A020807: sqrt(2) and sqrt(2)/10=1/sqrt(50). (Offset of a `cons` entry = radix-place address of the constant; the digit string is identical — Aha: for constants, a scale by 10^k is only an offset change; so "0.73336 vs 11/15" style digit coincidences must be read against radix-place translation.)

### (l) Transitions as objects
- L18–24: secondary OFFSET: all 395,088 agree with threshold definition — "its value is already determined by the displayed record and is not an independent epoch spectrum."
- L26–31: 218 distinct primary offsets; "A primary-offset difference can mean a genuine index translation, a radix-place translation of a represented constant, a convention change, or simply a finite payload coincidence. It must be classified by the source definitions."
- L40–43: A107453/A164115 same values, offsets 4 and 0: "This is index transport, not decimal scaling."
- L45: "46 exact stored-payload groups with a primary OFFSET distinction".
- L50–52: "investigate the map that transports the source law when its indexing or scale address changes, rather than treating the OFFSET integer itself as the hidden mathematical object." (Transition = transport map, not the offset number.)
- L171–180: offset-aware transform graph: "Partial sums, first differences, alternating sign, one-place shift and negation produce 9,817 offset-consistent candidate edges"; 5,731 directed contacts with explicit cross-ref; 5,247 undirected pairs on 9,504 vertices; largest component 17 entries around A000302 (powers of 4) via partial-sum/first-difference/alternating-sign.
- L186–199: four tasks (neighbor discovery; non-novelty pressure testing; offset hygiene — "separate source index, secondary threshold, series valuation and radix-place translation"; field blind-spot testing). "typed, reversible or residual-retaining maps between definitions".
- L264–270: hop edges recorded with bank displacement, H-route displacement, kernel displacement, carry/borrow.

### (m) Hex / byte / 2^r
- L207–231: 256 = 8·8·4; 128 = 4·8·4; 32-seat address; bank bits 32/64/128; half-address 16/32.
- L233–237: A209924 = A209925 (mod 32); A130764 vs A130765 differ by 32; A121377 digits 48..57.
- L241–254 cubical lift / contact midpoint (Boolean 2-cube per address).

### (n) OEIS submission
- L5–16: export `oeisdata-main.zip` created 2026-09-23T03:00:19-04:00; 399,527 `.seq`; 17,762,694 terms; `files/` = Git-LFS pointers; 217,060 b-file pointers; `evidence/FULL_EXPORT_SCAN.json`.
- L56–58: 54.3% have b-file pointers; median 43 vs 33 displayed terms.
- L182–199 "Submission consequence": "The signed translation-carry relation remains the source-described publication realization." (Identifies the actual submission object: a signed translation-carry relation.)
- L188–194 four tasks. L197–199: cross-refs useful at "typed, reversible or residual-retaining maps" level.
- Field atlas A-numbers L122–132: A014307, A018893, A029143, A084239, A189996, A244350, A306557, A006677, A000201/A001950.

### (o) Container / aperture / countercorrelary
- L201 "countercorrelary aperture"; L265 "countercorrelary canary" = invariance test: a relation must survive changes of bank, kernel state, orientation and quotient *when its claimed target is insensitive to them*. Exact counterpart: an invariance/equivariance check under the declared fiber coordinates.
- L155–156 "whole-relative section residuals".

### (j) Repair implications
- For the Rubicon's 7-bit H: any semantic or physical reading must survive the countercorrelary canary (L264–270). The Rubicon's column-label semantics (WHO=110 etc.) would need to be invariant under bank/kernel/orientation/quotient changes to count.
- 142857 appearances are radix-local (keyword `base`), not cross-field (L72–92).

---

## F. snow/relation/oeis/RELATION_HANDOFF.md (162 lines, read in full)

Title L1: "Signed translation-carry publication guide". Independently checked: TP1 serialization is a bijection onto 0..N and first twelve values = 0,1,0,0,-1,0,1,0,0,0,2,-1 (matches L32).

### (n) OEIS submission — the object, the "quartet", attribution
- L3–5: "The source-described integer realization is the signed translation-carry array. ... The broader relation is in ../RELATION.md; the GM table is a scoped specialization."
- L7–10: **"The live submission quartet is not included. Compare its definition, traversal, DATA, OFFSET, attribution and upload links with this reconstruction before an external edit. This guide does not create a replacement ENTRY or explanatory COMMENTS."** (The "quartet" = the live submission's four-part record, not present in the package; content unknown here. Six comparison items named: definition, traversal, DATA, OFFSET, attribution, upload links.)
- L12–15: "For an integer displacement u and positive integer width m, Phi_m(u)_h = floor((u+h)/m) is the translation carry at phase h, where 0 <= h < m. The signed enumeration below addresses every integer value of u." (%N-level definition.)
- L19–24: P(m,i,h)=Phi_m(sigma(i))_h, m≥1, i≥0, 0≤h<m, sigma = A001057 (sigma(2j)=-j, sigma(2j+1)=j+1). "The positive and negative branches are inverse addresses ... They are not an order or orientation imposed on relation. The existing GM expression is the restriction u=bx of this profile, while the general normal-form, composition and return results do not depend on first-hit primes."
- L26–30 (TP1, %F/%O): shell s=m-1+i, m increasing, h fastest: n = C(s+2,3)+C(m,2)+h. "Each shell contains C(s+2,2) cells"; "These disjoint intervals prove uniqueness and full coverage; the inverse uses integer inequalities, not floating-point roots." (offset 0 implied by n formula starting at 0.)
- L31–32 (%S DATA prefix): 0,1,0,0,-1,0,1,0,0,0,2,-1.
- L34: "random-access reader works directly at arbitrarily large supplied indices without generating earlier shells."
- L36 (%o): `realizations/translation/reader.py` — "a local source-formula reconstruction, not a verified copy of the live submission."
- L40 (%Y): "A004199 records positive-integer floor quotients under its own pair enumeration; its values are the zero-phase positive restriction. A001057 supplies the signed address map. Cross-referencing these exact restrictions is not a claim of novelty or mathematical priority."
- L49: "The uploaded snapshot contains no matching first twelve displayed terms under its recorded starts; this bounded negative search does not establish novelty or exclude alternative serializations." (novelty search status)
- L145–152 Publication checks: "Validate the live terms against the exact generator, the indexing conventions against the definition, and each formula against its stated domain. Complete an equivalent-entry search and attribution review. Physical examples require their own calibration and data; they are not necessary to generate the integers." (%K not specified; keywords unstated — likely sign, tabf; my inference only.)
- L157–162: byte aperture "is a supporting corpus diagnostic, not a new definition of the candidate"; anchors A121377, A130764/A130765, A209924/A209925 support RR-COUNTERCORRELARY-APERTURE; "They do not alter the signed translation-carry terms, offset, keywords, or publication identity."
- Editorial risk (mine): notation Phi_m for translation carry collides with Phi_d cyclotomic polynomials used in SIGMA SE.38–39 and FINDINGS L100; an OEIS %F line using Phi_m would be misread as cyclotomic.

### (f) Residual / offset / displacement
- L12: u called "integer displacement"; carry = floor((u+h)/m), residual phase h. The profile over h of floor((u+h)/m) sums to u (Hermite identity: Sum_{h=0}^{m-1} floor((u+h)/m) = u) — mine; consistent with FINDINGS L100 "v=Phi_m(Sum_h v_h)+epsilon, Sum_h epsilon_h=0".
- L82: RR-FORCED-PROFILE "Canonical integer profiles and zero-sum residuals".

### (g) Fitting / evidence
- L42: CRT: for fixed odd prime p, an integer primitive at p and nonprimitive at smaller odd primes exists unconditionally; "This is a different quantifier order from fixing an arbitrary integer g and seeking a prime where it is primitive."
- L44: Fan–Pollack p_g=O(log^19(2|g|)) conditional on GRH + nonsquare, non-(−1); "the carry identities do not require them and do not prove them. The bound concerns prime magnitude, not by itself the bit complexity ... establish neither a set-theoretic consistency result nor an editorial acceptance guarantee."

### (a),(b),(c),(k),(l),(o)
- (b)/(o) L161: RR-COUNTERCORRELARY-APERTURE (case-fold, lower-five address).
- (c) L149–150: "Physical examples require their own calibration and data; they are not necessary to generate the integers." L94: RR-PHYSICAL-CALIBRATION "Physical calibration and shared uncertainty"; L118 RR-JOINT-CALIBRATION "Joint calibration constraints and exact projected bounds"; L116 RR-RELATIVE-DISK "Nonlinear disk coordinates and calibrated phase response".
- (a) L79 RR-INTRINSIC-TOPOLOGY "Topology from continuation and joint compatibility"; L90 RR-LANDMARK-RETURN "Lattice spacing, section endpoints and readdressing"; L58 "How coordinates and origins change without changing the source" (origin is a readdressing choice, not a center).
- (l) L57 "How width changes retain the finer record" (RR-SCALE-RETURN); L56 composition retains signed carries (RR-AFFINE-COMPOSITION); L140 RR-INDEX-TRANSPORT "Offset changes, Newton coefficients and retained degree"; L110 RR-DEPENDENCY-RETURN "Dependency offsets"; L136 RR-OEIS-TRANSFORM-GRAPH "Exact displayed transforms with retained offset"; L111 RR-CONSTITUTION-RETURN "Changing observations, measures and endpoint coordinates"; L112 RR-SECTION-OBSTRUCTION "equivariant-section obstructions".
- (k) L81 RR-FORCED-LAW "Existence and uniqueness of the required response"; L126 RR-INTEGER-ATTAINMENT "Integer existence, complete alternatives and forced targets"; L107 RR-SYMBOL-RETURN "Symbol scope, exact constants and encoded characters"; L124 RR-SOURCE-SEMANTICS "Source intervals for distinct claims".
- (d) L131 RR-H-RETURN "Observation, section, residual and whole return"; L132 RR-PRCT-TRANSPORT "Typed cocycles, reverse transport and separating apertures"; L133 RR-OBSERVATION-EPOCH; L103 RR-CYCLIC-TOMOGRAPHY "Translated multiplicities and cyclotomic blind modes".
- Complete proof index L76–141 (66 labels) — all resolve to ../RELATION.md; proofs/tests in REGISTRY.json.

### (j) Repair implications
- The package's publishable integer object is the signed translation-carry array — floor((u+h)/m) — a pure quotient/phase ("carry") object. Aha: this is exactly the "quotient" that SIGMA SE.31 says the remainder alone cannot recover; the Rubicon's "error is remainder" should be replaced by the pair (carry profile, phase), whose sum returns u exactly.
- Physics is explicitly unnecessary to the integer object (L149–150).

---

## G. snow/relation/REGISTRY.json (5860 lines, read in full in chunks)

Header L1–18: "revision": 25, "date": "2026-09-24", "authority": "/RELATION"; canonical mathematics RELATION.md, terminology TERMINOLOGY.md, references REFERENCES.md, publication oeis/RELATION_HANDOFF.md. view_return RR-VIEW-RETURN, predecessor 24, manifest history/R24.MANIFEST.sha256; policy L17: "The predecessor remains a separate authenticated artifact; current files do not embed its byte tree."
Each finding = {id, title, anchor, section_sha256, section_bytes, status, source, tests[], connections[]}. Test family names are themselves compact claims/counterexamples; I record those touching the brief's categories.

### G.1 Chunk L19–2100
- L20–45 RR-LAW "Relation amongst offset": status "specification / explicitly scoped realization"; source "User correction, 2026-09-23; v2-v6 clean laws"; tests "all_context_fixed_point_and_extension", **"no_fixed_interaction_arity"** (i/e: no fixed arity — cf. 7 interrogatives not fixed); connections incl. RR-PHYSICAL-CALIBRATION, RR-FORCED-LAW.
- L47–82 RR-AUTHORITY: "authoritative scope and publication contract; not a mathematical theorem"; source "User authority correction, September 23, 2026"; predecessor tests "relation_center", "relation_publication_contract", "scope_routes", "authority_mutation_controls".
- L84–101 RR-ROLES "Descriptive questions and status distinctions" (e: the interrogative/descriptive-question layer): source "User standing correction; attachment C:91-99; v5 inward law and v1 role contract"; test "no_fixed_interaction_arity". (Aha: the descriptive-question roles carry the no-fixed-arity test — the count 7 (or 10, or 16) is not fixed by the relation.)
- L103–131 RR-BINDINGS "Symbols, occurrences and value bindings": tests "operator_fixed_numeral_promotion", "occurrence_alias_control", "unicode_identifier_alias_control", **"numeral_leaf_positive_negative_NOT_sweep"** (e: NOT as a tested operator on numerals).
- L133–147 RR-ROLE-EVALUATION "Numerals are evaluations of typed roles": status "proved typed evaluation / collision-fiber law"; source RELATIONAL_OPERATOR_SEMANTICS.md; test "byte_aperture:role_evaluation". (h: numerals such as 3, 7, 13 are evaluations of roles, and equal numerals from different roles form a collision fiber — matches SIGMA §15 p/q/r/N/pi/b separation.)
- L149–175 RR-OPERATOR-RELATIONS "Operators as compatible tuples": "proved scoped reformulation and extension; no priority claim"; tests "same_kernel_not_only_same_rank", "address_independent_topology", "parallel_witnesses_retained", "all_pairs_do_not_force_face".
- L177–191 RR-VIEW-RETURN "Canonical facts and reversible views" (source null).
- L193–215 RR-INTERACTION-RETURN: tests "diagonal_read_stays_open", "joint_interaction_forces_cross", "phase_without_mixing_does_not_expose_cross".
- L217–235 RR-H-RETURN "Observation, section, residual and whole return": "exact theorem / scoped sectioned-return implementation"; tests "section_recomposition", "section_factor_cocycle".
- L237–255 RR-PRCT-TRANSPORT "Typed cocycles, reverse transport and separating apertures": "exact typed-return theorem under displayed hypotheses; native exports separately open" (i: OPEN native exports); tests "comparison_cocycle", "all_modulus_separation".
- L257–278 RR-COUNTERCORRELARY-APERTURE "ASCII banks, half-offset contacts and the 256-state return": "proved finite byte/ASCII decomposition and cubical contact law; semantic exports remain typed"; tests lower5_kernel_exact, ascii_four_bank_return, half_offset_contacts, byte_8x8x4, i_I_fold, digit_half_offset; connects RR-NONRADIAL-DOUBLE.
- **L280–298 RR-NONRADIAL-DOUBLE "Doubled inverse-sheet cyclometry without radial geometry"**: status "proved finite six-state theorem plus general involutive paired-observation criterion"; source "Derived from Formula Cartography quotient-wall partition, the supplied dihedral/PRCT method, and RR-H-RETURN"; tests "alias_dihedral", "paired_h". (a/o: the snowball's replacement for the torus: cyclometry on a doubled inverse sheet, six states, involutive pairing, dihedral alias — no radius. Built from the SIGMA dihedral method.)
- L300–314 RR-OBSERVATION-EPOCH "Return-selected epochs and surviving substance": source "SIGMA_EPOCH_DIHEDRAL_META_FORMULARY.md plus basis-relative observation method"; test "observation_epoch".
- L316–349 RR-FORCED-LAW: status "proved situational criteria, not an assertion that every unspecified interaction has a unique answer."; tests "dual_target_certificate", "forced_existence_certificate", "forced_value", "rival_is_exact_witness", **"inconsistency_is_not_uniqueness"** (k: "forced" values need certificates; inconsistency ≠ uniqueness).
- L351–425 RR-INTEGER-ATTAINMENT: "Classical structural result ... no priority claim"; tests incl. "integer_exclusion_certificate", "integer_joint_window_forces_target", "integer_no_bounded_solution_lost", "integer_unimodular_certificates", **"integer_vs_rational_attainment"** (k/g: rational solution ≠ integer attainment).
- L427–460 RR-COUNTER "Joint determination and indirect response": source "User correction; v6 T2-T4 and S10; new joint-constraint derivation"; tests joint_constraint_return, indirect_transfer, schur_return; connections incl. RR-CODE-CHARACTER, RR-QUOTIENT-PHASE, RR-SINGULAR-RESPONSE.
- L462–524 RR-SINGULAR-RESPONSE "Singular coupling without an imposed regularizer": tests incl. "negative_curvature_certificate", "rest_forces_relative_target", "rest_keeps_common_freedom", "singular_feedback_inconsistent", "singular_kernel_retained"; connections RR-S10, RR-EM. (a: "curvature" here = second-order (Hessian) sign certificate, not spacetime curvature.)
- L526–552 RR-PROFILE "Transport of observations and comparison contexts": source "v2 contextual law; v3 reciprocal-aperture/profile theorem"; aperture suite: "dual_profile", "aperture_refinement", "paired_transport". (b/o: aperture = observation profile with a reciprocal/dual.)
- L554–670 RR-T2 "When an operation is determined by compressed observations": source v6/02_PROOFS/ALL_TRANSFORM_RETURN.md:40; tests incl. "A8_floor_fraction_return", "T2_quotient_descent_failure", "T2_quotient_descent_success", **"T2_zero_is_not_undefined"**, "G5_arbitrary_coefficients_not_attained", "G5_frame_left_inverse", **"T4_excluded_is_not_zero"**, "A6_modular_division_fibers", "T3_fixed_point_no_depth_cut", "T3_genuine_stable_quotient". (f/l: zero ≠ undefined ≠ excluded — matches EXPECTATION_FIELD L104–109 four-way tag; quotient descent can fail.)
- L672–751 RR-T1 "Transporting an operation through exact representations": tests "G7_cross_ratio", "G7_projective_invertibility", "G8_matrix_inverse", **"T8_distinct_binding_not_renaming"**, "T8_equal_binding_cancellation", "A5_power_lift", "T1_transport_arity_guard", "T1_transport_domain_guard".
- L753–795 RR-T6 "Composition with endpoint, multiplicity or witness records": tests "R1_boolean_counting_not_same", "T4_converse_retains_branches", "T4_excluded_is_not_zero".
- L797–869 RR-T3 "Observational equivalence under continued operations": "T3_fixed_point_no_depth_cut", "T3_linear_stable_hidden_subspace". (g: "no depth cut" — fixed point found without imposing a depth; Aha: contrasts with Rubicon's integer "depth" exponents n chosen per quantity.)
- L871–954 RR-T4 "Hidden-coordinate and nonlinear residual transport": tests (d) **"B9_code_center_displacement", "B9_codeword_translation", "B9_complement_preserves_syndrome", "B9_idempotent_not_inverse", "B9_syndrome_is_not_full_word"**; "R5_zero_boundary_nonzero_route", "R5_homology_depends_on_faces", "G4_coarse_alias", "G4_haar_complete_return", "N8_derivative_constant_return", "S10_difference_multiplier", "S10_mean_gradient_return", "T6_mixed_term_retained". (d/f: syndrome is not the full word; complement (XOR 1111111) preserves syndrome — so 16 coherent words are only defined up to that; decoding is idempotent, not an inverse. Aha: "B9_code_center_displacement" = displacement measured from a code center, not a radial center.)
- L956–994 RR-T5 "Matrix transport and invariant observable spaces": "S9_no_common_diagonal", "S6_pointwise_product_mixes_modes".
- L996–1046 RR-CONTINUATION-EQUALITY: source "SRC-06:2099–2145 (SD-54 and the start of SD-55)"; tests "coherent_counterpart_sign_transports", **"coherent_old_sign_not_global"**, "continued_failure_word", "on_state_prior_continuation_splits". (l: a sign/orientation valid locally is not global — sign flips are transported, cf. Rubicon's signed ISW sign flip.)
- L1048–1060 RR-T7 "Which omitted coordinates a target requires": tests [] (empty — no test attached; i).
- L1062–1083 RR-INVARIANTS "Invariance, covariance and observation plateaus": source "v1 constant and fixed-operator results; v2 central compatibility; v3 involution split"; tests **"neutral_return_and_structural_constancy"**, **"carrier_independent_matching_laws"** (a/j: "neutral return" = the formal counterpart of the user's "topographically neutral"; carrier independence tested.)
- L1085–1141 RR-SECTION-OBSTRUCTION: "restored source-supported conditional proof; new exact finite implementation; analytic and empirical boundaries explicit"; source "SRC-06, §§8, 10, 11.2–11.6, 12.2–12.4; SD-18–SD-31 and SD-35"; tests "syndrome_section_right_inverse", **"half_return_is_translation"**, **"section_slip_cocycle"**, "section_slip_in_kernel", "stabilizer_fixed_fiber_obstruction", **"six_obstructions_not_choice_failure"**, **"two_complements_different_syndrome"**, **"two_complements_same_read"**, "complete_plane_defect_field", "plane_compression_not_all_ranks", "lower_mark_not_fiber_section". (d/f: choosing a coset leader cannot be done equivariantly — 6 obstructions are structural, not a bad choice; Aha: this is exactly why no fixed labelling of the 7 H columns (WHO=110...) can be symmetric under the full PSL(2,7): an equivariant section doesn't exist.)
- L1143–1169 RR-EQUIVARIANT-RETURN: source "SRC-06:1268–1286 (SD-31)"; tests "each_element_has_fixed_lift", "equivariant_stochastic_section", **"whole_stabilizer_has_no_fixed_lift"** (each element fixes a lift, but the whole group doesn't; a stochastic (averaged) equivariant section exists).
- L1171–1224 RR-T8 "Domains, analytic assumptions and verification limits": "G3_z_left_roc", "G3_z_right_roc" (Z-transform region of convergence sides).
- L1226–1278 RR-INCIDENCE-RETURN "Comparison classes, exact differences and loop transport": tests "full_difference_record_return", "component_constants_are_exact_kernel", **"one_actual_level_per_component"**, "monotone_rank_without_gcd", **"joint_relation_connects_without_canvas"**, "loop_action_can_force_shared_level", "positive_energy_preserves_kernel", "positivity_not_silently_removed". (l: differences return a level only up to one constant per component — the anchor; "without canvas" = no ambient space/background needed. Aha: "canvas" is the snowball's word for the fixed background/carrier the old drafts assumed.)
- L1280–1341 RR-INTRINSIC-TOPOLOGY: tests "address_independent_components", "address_independent_topology", "topology_empty_whole", "topology_unions_intersections", **"direction_not_silently_inverted"**, "parallel_witnesses_retained", **"opposed_topologies_retained"**, "continuation_preservation_is_continuity", "faces_are_jointly_witnessed", "all_pairs_do_not_force_face", "minimal_exclusion_returns_complex", "downward_closure_from_compatibility". (a: topology is address-independent and derived from continuation/compatibility, with both orientations retained — counterpart to "inward/outward toroidal flip": the two directions are opposed topologies retained, not a flip.)
- L1343–1365 RR-M9 "Joint constraints and higher-order interactions": "whole_scope_not_proper_projections", "all_arity_real_contrasts".
- L1367–1405 RR-PARTICIPATION: source "User correction 2026-09-23 15:33 UTC"; tests "truth_response_from_character", **"code_free_fiber_return"**, "erasure_uniqueness", **"participation_arity_not_fixed"**, **"no_data_is_whole_integer_fiber"**, **"domain_guards_do_not_invent_values"**. (d: fiber return without a code; e: arity not fixed; f: no data = whole fiber, not zero.)
- L1407–1441 RR-B2 "Set operations and predicate reconstruction": "B3_add_xor_overlap", "B3_demorgan", "B3_not_not_identity", "B3_or_xor_overlap", "R3_set_complement_return". (e: NOT/NOT identity; m: add = xor + 2·and.)
- L1443–1497 RR-GRADED-RETURN: "formal_generator_inverse", "formal_euler_inverse", "primitive_period_partition", "independent_lyndon_enumeration", snapshot tests (modular discriminant, catalan, bell, tree euler, hurwitz log, blasius).
- L1499–1596 RR-I1 **"Cyclotomic factors and incidence inversion"**: source v6/02_PROOFS/ARITHMETIC_LOGIC_INCIDENCE.md:126; tests "B2_all_truth_tables_mobius_return" (m: truth-table/ANF Möbius = Reed–Muller transform), "N2_divisor_mobius_return", "N2_mobius_totient", "N10_discrete_log_product", "N10_quadratic_character", "N4_lambda_order_support", "N4_noncyclic_totient_exception", "N4_unit_cumulative_return", "N1_cyclotomic_degree", "N1_cyclotomic_factorization", "N3_greek_additive_polynomial_identity", "N3_greek_product_identity". Connections RR-GM-CARRY, RR-METHOD-CLOSURE.
- L1598–1650 RR-I2 "Product reconstruction, overlap and valuations": "B8_product_resolves_sum_alias", "B8_sum_projection_collision", "B7_factor_overlap_law", "N5_rad_support", "N5_tau", "N5_valuation_product".
- L1652–1682 RR-GRADED-INVARIANTS: "hilbert_collision", "socle_separates_algebras".
- L1684–1736 RR-I3 "Polynomial evaluation, interpolation and lost coefficients": "N9_gamma_collision", "N6_newton_return", **"N7_evaluation_residual_divisible"**, "A7_power_full_root_partition", N1 cyclotomic tests. (l/h: evaluating a polynomial at b (e.g. 10) loses coefficients; residual divisibility retained — directly the SE.38–39 evaluation Phi_d(10).)
- L1738–1802 RR-LATTICE-INCIDENCE: source "SRC-07, §§1–16; ST-01–ST-15"; tests "complementary_lattice_labels", **"tanner_signed_gradient"** (d: Tanner graph of a code as signed gradient), "signed_gradient_rank", "signed_gradient_spectral_polynomial", "row_star_diagonal", **"dark_present_rank_one_correction"**, "endpoint_block_is_retained", "incidence_real_gram", "integral_index_two_return", **"odd_total_outside_integral_image"**. (Aha: H^T H as a signed-gradient/Laplacian-type Gram is here as "incidence_real_gram" — the legitimate version of Rubicon theorem "H^T H = Laplacian", with an index-two integrality obstruction.)
- L1804–1862 RR-LOCAL-TO-GLOBAL: "acyclic_join_not_unprovided_source", **"cycle_pairwise_not_joint"**, "join_plan_orientation_not_source", "join_witness_identity_retained".
- L1864–1882 RR-GLOBAL-ATTAINMENT: "compactness_fixture_finite_prefix".
- L1884–1997 RR-A1 "Euclidean representations of integer operations": tests "A2_add_carry", "A2_subtract_borrow", **"A3_divmod_return"**, "A6_modular_division_fibers", **"A8_zero_denominator"**, **"S7_division_is_deconvolution"**, "A5_power_lift", "A7_power_full_root_partition", "A8_ceiling_fraction_return", **"A8_signed_seam"**, "A9_gcd_lcm_alias". (f/l: quotient+remainder return; seam at sign change.)
- L1999–2041 RR-FORCED-PROFILE "Canonical integer profiles and zero-sum residuals": status "exact normal-form equivalence on the stated integer phase lattice."; source "Current supplied translation-carry commentary, its P1/P3/P5 formulas"; tests "normal_form_from_constraints", "signed_normal_form_return", "complete_row_return", "integral_residual_basis", **"correction_cocycle"**, "all_signed_carry_composition", "nested_width_equivalence", **"higher_winding_not_same_uniqueness"**. (a: "winding" appears only as a test that higher winding does NOT carry the same uniqueness — relevant to torus-winding claims.)
- L2043–2080 RR-AFFINE-COMPOSITION: source "ATT-D ...; SRC-R10-CONSTANTS/SRC-R10-SYMBOLS where indicated"; tests "affine_weighted_carry", "affine_base_shear_interlock", "affine_associativity", **"unweighted_composition_rejected"**, "neighbor_continuation_splits".
- L2082– RR-SCALE-RETURN "Common scaling and changes of resolution": "common_scale_exact", "opposite_affine_scale_leg" ...

### G.2 Chunk L2082–3000
- L2082–2126 RR-SCALE-RETURN tests: "common_scale_exact", "opposite_affine_scale_leg", **"both_factor_scale_needs_square"**, **"proposed_H1_not_quotient_preserving"**, **"proposed_H2_not_coarsening"**, "denominator_coarsening", "denominator_refinement", "coarsening_composes". (i/l: two proposed maps H1/H2 are rejected as a correction — record of rejected proposals.)
- L2128–2152 RR-LANDMARK-RETURN "Lattice spacing, section endpoints and readdressing": source "User correction 2026-09-23 15:33 UTC"; tests "landmarks_derived", **"lattice_section_from_center"**, **"origin_readdress_retains_integer"**. (a: a "center" is used for a lattice section but origin is readdressable while retaining the integer — center is a chart choice, not physical.)
- L2154–2224 RR-DEPENDENCY-RETURN "Dependency offsets and normalized reconstruction": source "SRC-06, §§2–7 and 10, individually assessed as SD-01–SD-17"; tests "offset_null_returns_width", "oriented_dependency_interval", "signed_dependency_seam", **"sublinear_exact_error"**, **"sublinear_not_bounded"**, "balanced_dependency_telescope", **"balanced_relative_remainder"**, "balanced_translation_invariance", "finite_torsion_offset_inverse", **"cross_characteristic_inverse"**. (f: "error" used as an exact sublinear quantity that need not be bounded; remainder is relative/balanced.)
- L2226–2292 RR-QUOTED-DERIVATION "Incidence encoding, increment counts and interval reconstruction": status "exact reproduction and conditional provenance reconstruction. **The original program emitting the quoted keys was not present in the supplied archives or located by Library search.**" (i: open provenance); tests "closed_increment_census", **"endpoint_forces_total_increment"**, "exact_completion_interval", "pair_injectivity_exact_condition", "excerpt_seam_order", "excerpt_quotient_complete", "excerpt_residue_multiplicity", **"second_difference_return"**, **"second_difference_affine_kernel"**. (l: endpoints force total increment (telescoping); second differences return up to affine kernel — two anchors.)
- L2294–2320 RR-INDEX-TRANSPORT: tests "signed_index_covariance", "signed_index_inverse", "snapshot_fibonacci_binomial", "snapshot_square_prefix_sum".
- L2322–2392 RR-RESPONSE-SERIALIZATION: source "SRC-06, §§1, 6, 15.3–15.5 and 19.8; SD-00, SD-08–SD-09, SD-65–SD-68 and SD-100"; tests "partition_from_log_response", **"partition_needs_normalization"**, "occupation_three_returns_fifth_power_coordinate", "declared_sampler_detailed_balance", "closed_walk_census", "source_scalar_period_word", "source_scalar_least_period", "random_access_source_reader", "large_index_reader_range", **"mixed_radix_integer_step"**, **"mixed_radix_terminal_return"**, **"code_weight_enumerator"**. (m/l: mixed-radix step as transition; weight enumerator of a code.)
- L2394–2494 RR-S1 "Finite Fourier convention and operation laws": "S1_exact_fourier_inverse", "S1_parseval", "S2_modulation_shift", "S2_translation_character", "S3_noncommutative_weyl_phase", "S4_reversal_frequency", "A8_signed_seam", "S6_pointwise_product_mixes_modes".
- L2496–2505 RR-S3 **"Aliasing under index dilation and inversion of differences"**: tests [] (no test; i). (l: inversion of differences as a titled theorem.)
- L2507–2556 RR-S4 "Walsh, Haar and windowed Fourier reconstruction": "B6_all_plane_contrast_return", "B6_general_walsh_return", "G4_coarse_alias", "G4_haar_complete_return". (m: Walsh = the character basis of F_2^n.)
- L2558–2607 RR-CHARACTER-SEAM: tests "character_polynomial_exact", **"jump_character_return"**, "character_scale_factorization", "untwisted_product_is_lcm", **"higher_lift_not_repeated_lower_filter"**, "spectral_partition_return", "nonzero_filter_exact_inverse", **"countersector_return"**. (l: a jump is returned by its character; o: countersector.)
- L2609–2641 RR-MONOTONE-CLOSURE: "newly derived general theorem here; no priority claim."; tests incl. **"monotonicity_is_actual_hypothesis"**.
- L2643–2661 RR-R-LANDMARKS "Phase notation and operation definitions": tests "paired_inverse_product", "common_phase_cancels".
- L2663–2677 RR-CYCLIC-TOMOGRAPHY: "exact finite cyclic inverse theorem / corpus measurement"; source OBSERVATION_AND_AMBIGUITY_METHOD.md.
- L2679–2750 RR-QUOTIENT-PHASE "Integer quotient reconstruction from joint phase readings": tests "paired_inverse_product", **"inverse_receives_phase_only"**, "joint_phase_CRT_return", "joint_kernel_exact", "close_rate_bounded_return", **"ratio_can_forget_common_phase"**, **"ratio_period_not_joint_period"**, "inconsistent_joint_record", **"unattained_exact_phase"**, **"phase_derivative_returns_quotient"**, **"irrational_phase_kernel_symbolic"**, **"phase_noise_separation_contract"**, **"bounds_come_from_rest"**, "formal_phase_series_composition"; connections RR-RELATIVE-DISK, RR-JOINT-CALIBRATION. (g/k: an irrational phase kernel is kept symbolic — i.e., the "irrational base" 0.73336 cannot be approximated by 11/15 without a declared kernel; ratios forget common phase — e.g. ratio-based constants like H0 ratio lose the common scale; bounds come from the rest (calibration), not from the code; phase derivative returns quotient — the transition (derivative) returns the level count.)
- L2752–2781 RR-REFINEMENT-ATTAINMENT: "nested_refinement_period", "compatible_noninteger_inverse_system", "noninteger_system_balance", **"noninteger_not_forced_as_integer"**.
- L2783–2883 RR-PHASE "Upper-section refinement and scalar phase comparisons": source "v1 fractional return; v4 phase and displacement proof; archived September17 entries"; displacement suite: "upper_reconstruction", **"displacement_plus_remainder"**, **"uniform_error"**, "reverse_return", "periodicity", "phase_subdivision", "exact_mean", "composition", "finite_arity_return", "spectral_dither_filter", **"repetend_spectrum"**, **"no_universal_pi_gap_requirement"**, **"pi_certificate"**, "positive_integral_certificate", **"certified_sequences"**, "signed_refinement", "normalized_gap_limit", **"decimal_prefix"**, **"interval_contrast"**, "spectral_seam_control", **"width_does_not_return_common_origin"**. (k: constants-first certification tests — pi certificate, certified sequences, decimal prefix, interval contrast; f: displacement = quotient + remainder with "uniform_error" (the fractional part as a bounded, uniform error term); a: "width does not return common origin" — a width/scale alone can't fix an origin (no intrinsic center); h: repetend spectrum = 142857-type periodic digit spectrum.)
- L2885–2934 RR-ANALYTIC-SEAM "Fourier boundaries and exact integer-balance tests": tests "sinc_symmetric_response", **"sinc_boundary_half_weight"**, **"original_sinc_wrong_section"** (a correction: the original sinc convention used the wrong section), "shifted_sinc_integer_section", "shifted_sinc_continuum_not_section", **"modular_filter_cannot_see_quotient"**, **"whole_balance_retains_quotient"**, "whole_integer_fiber", "laurent_labelled_fiber". (f/l: a modular (remainder) filter cannot see the quotient — same as SIGMA SE.31; a jump boundary gets half weight.)
- L2936–2970 RR-PHASE-RESPONSE: tests "balanced_forward_identity", "general_contrast_law", "cross_inverse_no_source_input", "one_phase_can_be_forced_by_rest", **"rank_alone_not_attainment"**, "multimode_complete_inverse".
- L2972– RR-MODULATION-RETURN "Reversible phase, spectral redistribution and averaging": "known_phase_reversible", "specified_phase_average", "bessel_generating_coefficients", "formal_phase_inverse", "fourier_phase_is_convolution" ...

### G.3 Chunk L3000–3950
- L3004–3066 RR-B1 "Boolean truth functions and character transforms": tests "B1_all_truth_tables_walsh_return", "B2_all_truth_tables_mobius_return" (m: Walsh + ANF/Möbius = RM transforms over all truth tables), **"B5_joint_xor_not_bilinear"**, "B5_xor_rectangle", "B4_overlap_weight", **"R11_dark_deleted_correction"**, "T4_excluded_is_not_zero".
- **L3068–3108 RR-B3 "Code correction and complete word reconstruction"**: source v6/02_PROOFS/ARITHMETIC_LOGIC_INCIDENCE.md:110 (B3); tests B9_code_center_displacement, B9_codeword_translation, B9_complement_preserves_syndrome, B9_idempotent_not_inverse, B9_syndrome_is_not_full_word, B6 Walsh returns; connection RR-CODE-CHARACTER. (d: the package's Hamming correction theorem: complete word = codeword + displacement from code center; syndrome ≠ word.)
- **L3110–3144 RR-CODE-CHARACTER "Parity characters and reversible code puncturing"**: status "conditional theorem / source-derived repair with explicit analytic boundary"; tests "parity_character_projector", **"puncture_extension_bijection"** ([7,4,3] <-> [8,4,4] extension/puncture bijection), **"extended_code_even_self_dual"** ([8,4,4] self-dual), "code_minimum_distances", **"fano_lines_not_code_identity"**. (d: Fano lines are NOT the code identity — the 7 weight-3 codewords are Fano lines but the Fano plane does not by itself identify the code/its labelling. Direct correction to Rubicon "Fano plane = the code" identification.)
- L3146–3196 RR-PARTICIPATION-PROBES: source "SRC-06, §§11.3–11.4 and 12.5–12.6; SD-18–SD-23 and SD-32–SD-36"; tests "translated_weights_character_spectrum", "translated_real_reader_invertible", "real_probe_explicit_inverse", "all_binary_difference_certificate", **"three_probe_actual_decoder"**, "unattained_probe_tuple", **"every_two_probe_family_fails"**, "original_phase_fibers", "zero_lifts_distinguished_relatively", "complete_atlas_return". (Aha: "three probes decode, every two-probe family fails" — the finite analogue of SIGMA's rank 3/5/6: three is the threshold; a legitimate, nonphysical home for "3".)
- L3198–3234 RR-COHERENT-REST: source "SRC-06, §§14.4–14.7; SD-52–SD-59"; tests "coherent_code_basis", "code_small_reduced_states", "on_state_rest_compensation_X", "on_state_rest_compensation_Z", **"state_compensation_not_operator_identity"**, "code_dual_character_exchange". (d: quantum-code-style X/Z (Steane/CSS-like) compensation — state-level compensation is not an operator identity.)
- L3236–3285 RR-DISTRIBUTION-RETURN: "probe_means_do_not_return_distribution", "full_probe_law_does_return_distribution", "three_site_marginals_identical", "fourth_order_response", "independent_fourth_order_differs", "number_second_moment_gap", **"equal_covariance_not_quartic_response"**, "full_number_law_not_phase_return". (g: means/covariances do not return the law — significance from second moments alone insufficient.)
- L3287–3316 RR-COHERENCE "Coherent amplitude reconstruction up to common phase": source "v3 optical cross-term and Gram return; v5 general mixed-coherency extension"; aperture suite: "interference_cross_return", "gram_compatibility", "common_phase", "disconnected_phase_control".
- L3318–3384 RR-S10 "Statistical summaries, coherence and coupled zero responses": "R8_entropy_relabel_alias", "R8_finite_moment_alias", "R8_higher_moment_separates", "R8_mean_norm_extrema_alias", "S8_half_cycle_odd_support", **"S8_nonuniversal_spectral_gaps"**, **"R10_transpose_not_adjoint"** (d: H^T is not an adjoint without a declared inner product — relevant to Rubicon "H^T H = Laplacian" / metric claim).
- L3386–3482 RR-MODEL-ATTAINMENT: source "SD-61–SD-66, SD-96, SC-07 and SC-11 ..."; tests "code_actual_selfdual", **"code_normalization_not_selfdual"**, "code_mask_guard", "disk_relative_domain_guard", "force_complete_model_return", **"force_irrational_inverse_retained"**, **"force_projection_not_model_validation"**, **"force_residual_exact"**, **"placed_full_record_still_returns"**, "placed_breaks_shape_guard", "placed_cells_shape_guard", "placed_seams_shape_guard", "translated_domain_not_length_only", **"provided_code_not_enumerator_bound"**. (g/c: a projection matching data is not model validation — directly addresses the 19-measurement fit; irrational inverse retained (no rational substitution).)
- **L3484–3508 RR-PHYSICAL-CALIBRATION "Physical calibration and shared uncertainty"**: status "conditional theorem / explicitly scoped interpretation where stated"; source "User correction 2026-09-23 15:33 UTC"; tests **"physical_calibration_cancellation"**, **"synthetic_length_return"**, **"common_geometry_phase"**; connection RR-JOINT-CALIBRATION. (c/k: physics enters only as calibration with shared uncertainty; common calibration cancels in ratios; a common geometry contributes a common phase — i.e. a torus/lens geometry common to all observations cancels rather than producing constants. Aha: this is the formal reason PrePub2's universal lens factor L^w cannot generate constants: a common geometric factor is a common phase that cancels from relative observations unless separately calibrated.)
- **L3510–3551 RR-JOINT-CALIBRATION "Joint calibration constraints and exact projected bounds"**: source "SRC-06, §§13.5–13.7, 15.6–15.8, 16 and 17; SD-44–SD-46 and SD-69–SD-91"; tests "calibration_dual_certificate", **"calibration_full_projected_interval"**, "calibration_primal_witness", "calibration_bound_sharpness", "rest_calibration_integer_lattice_return", **"postprojection_context_no_new_information"**, "common_reference_covariance". (k: constants-first = projected intervals with primal/dual certificates; post-projection context adds no information.)
- **L3553–3631 RR-CONSTITUTION-RETURN "Changing observations, measures and endpoint coordinates"**: source "SRC-06, §§18–20 ...; SD-92–SD-103"; tests "moving_calibration_retained", "moving_constitution_composition", **"moving_endpoint_lenses_return"**, "nonbijective_context_mean", "noninvariant_measure_defect", **"measure_mismatch_can_alias_one_mean"**, **"nonlinear_mean_counterexample"**, **"source_mean_after_placed_inverse"**, "both_endpoint_charts_return", **"placement_dependence"**, "finite_average_composition", "section_refinement_correction", "nonconstant_section_cannot_disappear", "profile_inverse_from_cells", **"seam_not_returned_by_mean"**, **"scalar_dither_metric"**, **"vector_metric_not_scalar_isometry"**. (b: this is the registry home of the nonlinear lens/placement law: endpoint lenses, placement dependence, mean must be taken after the placed inverse (not G(mean)); a: metrics appear only as dither metric / vector metric caveats.)
- **L3633–3687 RR-RELATIVE-DISK "Nonlinear disk coordinates and calibrated phase response"**: source "SRC-06, §§14.1–14.3 and 15.2; SD-47–SD-51 and SD-61–SD-64"; tests **"disk_return_with_reference"**, "disk_response_from_relative_phase", **"disk_composition_gauge"**, "disk_reversal_phase", "phase_force_first_harmonic", "phase_force_inverse", **"force_radical_not_rounded"**, "finite_nullifier_boundary_retained", **"nonlinear_estimator_bias_not_erased"**, **"response_is_not_a_metric"**, "source_force_landmark". (a/b: the only disk is relative — returned with a reference, with a composition gauge; "response is not a metric" — a lens response cannot be read as geometry; radicals not rounded (no 0.73336≈11/15 substitution); nonlinear estimator bias retained.)
- L3689–3739 RR-S5 "Mellin scaling and phase branches": "G2_exp_phase_alias", **"G2_phase_winding_return"**, "S11_hilbert_lifted_inverse", "G1_mellin_character_composition".
- L3741–3761 RR-S6 Laplace/Z/Hilbert/Stieltjes: "G10_hankel_gaussian_coefficients", "N8_laplace_derivative_boundary".
- L3763–3772 RR-S7 "Radon and Hankel transforms: geometry and measure": tests [] (none; i). (a: radial (Hankel) transforms scoped, untested.)
- **L3774–3812 RR-S8 "Metaplectic phase and linear canonical transformations"**: tests "G2_exp_phase_alias", "G2_phase_winding_return", **"G8_metaplectic_double_return"**, **"G8_metaplectic_phase_retained"**, N4 tests. (b/o: the lens as a linear canonical transformation with a metaplectic double cover — the double sheet; phase retained.)
- L3814–3891 RR-S9 "Projective, graph and homological reconstruction": "R6_jordan_retained", **"R6_trace_det_spectrum_alias"**, "S9_no_common_diagonal", **"R4_cycle_integrability"**, "R4_gradient_return", **"R4_hodge_cycle_residual"**, "R5_boundary_kernel_dimension", "R5_homology_depends_on_faces", **"R5_zero_boundary_nonzero_route"**. (a: Hodge cycle residual = the non-gradient part; a cycle (winding) residual is a legitimate topological residual not reducible to a potential.)
- L3893–3913 RR-M6 "Finite phase and unbounded scale": **"log_scale_phase_winding"**, "mellin_log_interval_covariance". (a: winding appears as log-scale phase winding — scale not radius.)
- **L3915–3937 RR-M7 "Doppler ratios and common-reference cancellation"**: tests **"passive_Lorentz_ratio_invariance"**, **"same_reference_Doppler_ratio"**, "doppler_rapidity". (c: Doppler handled as ratio with common-reference cancellation and rapidity additivity.)
- L3939– RR-M8 "Ordered delay-scale actions and converse port relations": "delay_scale_composition" ...

### G.4 Chunk L3950–4950
- L3939–3957 RR-M8: "delay_scale_composition", "noncommuting_delay_scale_control" (b: order of delay/scale lenses matters).
- **L3959–3995 RR-EM "Electromagnetic models and reconstruction conditions"**: status "specification / explicitly scoped realization"; source "v5 electromagnetic atlas ... REF-V5"; tests "RIME_covariance", **"Faraday_grid_alias"** (RM-synthesis phase-wrap aliasing), **"comb_harmonic_offset"** (frequency comb offset), **"synthetic_color_metamer"** (CIE observer: different spectra, same reading), "hidden_relaxation_Schur"; connections incl. RR-GM-WINDING, RR-PHYSICAL-CALIBRATION. (c/b: physical observation modelled as aliasing/metamer/offset returns — observation loses information by lens, never produces constants.)
- L3997–4035 RR-FIELD-ATLAS: "coverage atlas with scoped native mathematical representatives; not completeness of any field."; tests "projective_chart_inverse", **"morse_sphere_euler_relation"** (a: sphere appears only via Morse/Euler relation on S^2), "volterra_snapshot", "inverse_series_parameter_pde", "k_group_rank_snapshot", "wythoff_sprague_grundy_zero_set", "phylogenetic_snapshot".
- L4037–4061 RR-GM-DEFINITION "First-hit prime/base specialization of the quotient profile": source "Attachments A:1-54, B:17-31, C:19-38; v5-v6 public definition"; tests gm_complete_blocks, gm_shear, gm_internal_return.
- L4063–4099 RR-GM-CARRY: editorial suite: "carry_threshold", "chain_reindex", "chain_integer_inverse", "nonunit_carry_rank", "column_margin", **"carry_matrix_not_full_C_inverse"**.
- L4101–4130 RR-GM-SPATIAL-MIN: "newly derived theorem in the stated measurement model; no novelty claim"; "spatial_minimum_constructor", "spatial_minimum_exhaustive", "integer_phase_subdivision", "two_phase_direct_inverse".
- L4132–4154 RR-GM-OBS "Successive digit observations and ordered-tuple reconstruction": source "... derived exact proof and two-phase counterexample"; "prefix_threshold", "tuple_threshold", "two_phase_counterexample".
- L4156–4182 RR-MULTIPLICATIVE-PHASE "Multiplicative actions, orbits and waveform spectra": source "v5 M1-M3; 02_TIP_SUPPORTS.txt"; tests **"all_unit_radix_rotations"**, **"long_division_all_numerators"**, "exact_character_diagonalization", **"infinite_hold_spectrum_finite_certificate"**. (h: 142857 cyclic rotations = unit radix rotations / long division — the typed home of the 1/7 cyclic number.)
- L4184–4218 RR-S2 "Operation-dependent spectra of the cyclic digit profile": N10 discrete-log/quadratic character, S8 half-cycle odd support, **"S8_nonuniversal_spectral_gaps"**. (h: digit-profile spectra depend on the operation; no universal gap.)
- **L4220–4242 RR-GM-WINDING "Cyclic words, boundary winding and higher-lift cycles"**: source "Attachments A:56-65, A:122, C:84-89; v5 M4"; tests "word_winding", "seam_winding", "lift_cycle_strata". (a: winding is defined combinatorially on cyclic words and seams — the snowball's replacement for torus-knot winding (1,3); no radii.)
- L4244–4266 RR-M4 "Ambient multiplication and the higher quotient lift": "ambient_vs_transported_product", "lifted_return", "qualification_fiber".
- L4268–4294 RR-GM-FOURIER: source "Attachments A:80-92 and B:44-51; independently derived correction"; "fourier_residue_identity", "circulant_nonsingular", **"two_fourier_charts"**.
- L4296–4310 RR-GM-DISPLACEMENT "The complete inverse of integer displacement": source "Attachment B:64-69; independent full-line proof"; test "global_displacement_fibers".
- L4312–4334 RR-GM-APERY: "Attachments A:99-100 and C:62-82; corrected terminology and source maps"; "apery_gap_counts", "pair_fibers", "pair_profile_return".
- L4336–4354 RR-GM-GENERATING: "tuple_generating_polynomial", "slot_refinement".
- L4356–4374 RR-GM-DENSITY "First-hit densities and the prime-two convention": source incl. "OEIS A280015"; "qualification_density", "least_base_oracle".
- L4376–4402 RR-N1: neighbor_quotient_marginal, neighbor_residue_marginal, neighbor_product_decode, neighbor_support_index_shift.
- **L4404–4422 RR-N2 "Phase transport of quotient and remainder"**: test "neighbor_joint_phase_transport". (f/l: quotient and remainder transported jointly.)
- L4424–4442 RR-N3 "Spectral and divisor formulas for remainder counts": "neighbor_Fourier_gcd_certificate", "neighbor_divisor_census".
- L4444–4474 RR-NEIGHBORS "Exact relationships to existing integer sequences": status "editorial assessment".
- L4476–4498 RR-ENTRY "Worked examples of the GM specialization": status "editorial assessment"; editorial tests "public_observation_examples", "qualified_global_inverse", "entry_formula_contract". (n: %e/%F contracts.)
- L4500–4509 RR-OEIS-TRANSFORM-GRAPH: status "corpus discovery graph / finite displayed-data identities; promotion requires definition-level proof"; tests [] (none).
- L4511–4529 RR-OEIS-BYTE-TRACE "Lossless byte dither on sequence-hop edges": status "proved lossless integer-to-byte return plus complete stored-corpus diagnostic; semantic interpretation only for sourced encodings"; tests integer_byte_return, oeis_month_mod32, oeis_case_fold_32, corpus_summary_contract.
- L4531–4549 RR-CORPUS-READOUT: tests **"finite_prefix_not_full_sequence"**, "prefix_next_term_separates".
- **L4551–4579 RR-TRANSLATION-PUBLICATION**: status **"source-formula reconstruction and exact mathematical extension; not an export of the unseen live ENTRY."**; source "Current attached commentary lines 24–34, 43–45, 69–76; source eight-way dossier; directly checked OEIS A001057/A004199; Fan–Pollack arXiv:2505.05601v2."; tests "signed_address_return", "signed_translation_serialization", "random_access_unbounded_index", **"attachment_signed_prefix"**. (n: the live entry is unseen; the prefix is checked against the attachment.)
- **L4581–4618 RR-PUBLIC "Publication scope and file roles"**: source "Attachments A/B/C; preceding definition; current official OEIS offsets and AI-policy pages"; tests gm_complete_blocks, gm_entry_prefix, entry_formula_contract, public_observation_examples; connections RR-RESPONSE-SERIALIZATION, RR-PRESENTATION-CHECK, RR-CONTINUATION-AUDIT, RR-TRANSLATION-PUBLICATION. (n: AI-policy pages consulted; Attachments A/B/C — plausibly with the live ENTRY make up the "quartet" — my inference, unconfirmed.)
- L4620–4646 RR-METHOD-CLOSURE: status "source-grounded method reuse with explicit corrected hypotheses."; source "SRC-METHOD-NET, CENSUS PROOF DOSSIER; SRC-METHOD-PRIME, PROOF_DOSSIER.md; SRC-METHOD-LEDGER, PROOF_METHOD_LEDGER_v13.md"; tests incl. **"pairing_requires_payload_law"**.
- **L4648–4688 RR-PRESENTATION-CHECK "Exact arithmetic and integer indexing"**: tests **"submitted_routine_fails_exact_jump"** (n: a submitted program fails at an exact jump — an editorial risk found in the submitted routine), **"floor_dissolved_is_same_floor"**, "antidiagonal_exact_return", "antidiagonal_both_directions", **"conditional_row112"**, **"row112_shear_slice"** (d?: "row 112" — cf. the 112 of the Rubicon; here a row index of the array, a shear slice; do not conflate), **"repetend_wall_six_not_seven_nines"** (h: registry-tested version of SIGMA L823–825).
- **L4690–4760 RR-SYMBOL-RETURN "Symbol scope, exact constants and encoded characters"**: tests **"constant_enclosures_positive"**, **"constants_certified_affine_composition"**, **"constants_scale_unchanged"**, **"phi_gold_not_totient"** (notation collision φ golden vs φ totient), **"source_pi_density_finite_mobius"**, "restricted_alphabet_identity_count", "alphabet_quotient_phase_return", "alphabet_common_scale", "alphabet_weighted_composition", **"alphabet_jump_character"**, **"case_carry_mask_counts"**, **"sigma_branch_retained"**, **"glyph_scalar_not_identical"**, **"HXE_convention_closure"**, "HXE_case_response_retained". (k: constants are handled as certified enclosures (intervals) composed affinely — constants-first; m: HXE likely hex-case convention; case-carry masks = 32 bit.)
- L4762–4776 RR-OPERATORS "Operator definitions and reconstruction requirements": 22,166 bytes; "Source registry SRC-OPERATOR; every entry traceable to its original physical line".
- L4778–4794 RR-GREEK: source "SRC-GREEK; **named laws not glyph-assigned meanings**" (e/h: symbols carry laws, not assigned meanings — parallels interrogative labels).
- L4796–4810 RR-TRANSFORMS; L4812–4826 RR-CONTINUATION-AUDIT "Statement status and source assessment"; L4828–4842 RR-AUDIT "Source claims and current mathematical statements": source **"All three incoming files, including mutually conflicting recommendations"**.
- L4844–4880 RR-PAIRWISE-COMPLETION: "Current higher-arity compatibility law; predecessor pair-review matrix retained only as predecessor provenance"; predecessor tests "completion_mutations_rejected", "verdict_integrity".
- L4882–4914 RR-SOURCE-SEMANTICS "Source intervals for distinct claims": source "Full source-piece comparison against every frozen R11 finding; actual SRC-06 intervals and the R12 reconciliation records."
- L4916– RR-RECONCILIATION-USE: tests "transpose_cannot_drop_ragged_tail", "matrix_vector_cannot_drop_coordinate", "rank_cannot_use_ragged_operator", "haar_cannot_drop_detail", "operation_iterator_retains_all_contexts", "duplicate_addresses_not_silent" ...

### G.5 Chunk L4950–5860 (end)
- L4916–4980 RR-RECONCILIATION-USE (cont.): "installation_dry_run_is_read_only", "installation_verified_copy", "installation_refuses_overwrite", **"live_contact_not_adoption"**, "installation_hash_mismatch", "installation_path_traversal", "claim_reconciliation".
- L4982–5030 RR-PROVENANCE, RR-SOURCES ("Technical sources and remaining verification requirements"), RR-VERIFY — "Consolidation contract".
- **L5032–5711 "operators" OP001–OP113** (each with proof_id, source SRC-OPERATOR). Brief-relevant:
  - (e) **OP021 "NOT" -> RR-B1; OP022 "NOR / n't" -> RR-B1** (the N'T of the user's interrogative set is registered as the NOR operator, not an interrogative); OP023 NAND, OP024 XNOR, OP025 converse, OP026 complement, OP027 dual/De Morgan. No WHO/WHAT/WHERE/WHEN/WHY/HOW/WHICH/WAY operators exist in the registry (their home is RR-ROLES, L84–101).
  - (f) OP011 mod/congruence, OP012 rem, OP013 "quo / wrap", OP014 divmod, OP015 floor (RR-T2), OP016 ceil, OP017 "balanced representative"; **OP108 "ERROR/residual" -> RR-T4** (hidden-coordinate & nonlinear residual transport — error is typed as a residual transport, not as noise).
  - (d) **OP051 "syndrome / parity" -> RR-B3; OP052 "Hamming/code chart" -> RR-B3** ("chart" — the code is registered as a chart); OP085 weight/wt -> RR-B1; OP056 Walsh -> RR-B1.
  - (a) **OP050 "Laplacian" -> RR-S9** (projective/graph/homological; cf. Rubicon "H^T H = Laplacian"); OP093 boundary, OP094 coboundary, OP095 cycle, OP096 homology; OP065 norm -> RR-S10; **OP100 "torus / mapping torus" -> RR-S8 (metaplectic phase & linear canonical transformations)**. (Aha, central: the ONLY torus in the snowball registry is a *mapping torus* attached to the metaplectic/LCT section — i.e., the torus is the suspension of a phase map (a period/monodromy object), not a radius-bearing surface T^2(R=13,r=3). This is the precise replacement for the old drafts' torus: a mapping torus has no radii, only a monodromy.)
  - (h) OP076 ord -> RR-I1; OP079 phi, OP080 mu -> RR-I1; OP081 tau, OP082 omega, OP083 rad -> RR-I2; **OP092 "cyclotomic Phi" -> RR-I1**; OP106 orbit -> RR-I1; OP105 period -> RR-S8; OP102 rotation -> RR-S2; OP104 reflection/reversal -> RR-S1.
  - (l) OP090 derivative/gradient -> RR-T4; **OP091 "finite difference / divided difference" -> RR-I3**; OP071 Sum, OP072 Product -> RR-I2; OP101 shift, OP103 translation -> RR-S1; OP097 path/route, OP112 arrow -> RR-T6; OP099 groupoid -> RR-T6.
  - (c) **OP107 "TIME" -> RR-T8 (Domains, analytic assumptions and verification limits)** (time is registered only as an analytic-domain/verification-limit matter — no arrow-of-time derivation; bears on PrePub2 cosh²−sinh² arrow of time).
  - (g) OP066 entropy, OP067 moment, OP070 mean/average/total -> RR-S4, OP069 min/max.
  - OP109 subscript, OP110 superscript, OP111 prime/apostrophe, OP113 bracket/enclosure -> RR-T1 (notation as transport).
- **L5712–5839 "greek_roles" GREEK-01..21**: Phi, phi, zeta, mu, lambda, chi -> RR-I1; tau, omega, nu_p, Pi_prod, Sigma_sum -> RR-I2; rho -> RR-A1; Delta -> RR-T4; epsilon, kappa, psi -> RR-B3; sigma, Gamma_overlap, Eta_unit -> RR-B1; Iota_incidence -> RR-I1; Theta_total -> RR-T3. (Notation: lambda is registered as Carmichael-type (RR-I1), epsilon/kappa as code roles (kappa = SIGMA's Fano cocycle), sigma as a Boolean role — so Rubicon's lambda=(11/15)^11 and sigma (OGSI metric A(sigma)) collide with registered roles. Also **GREEK-01 Phi -> RR-I1 cyclotomic** while RELATION_HANDOFF L13 uses Phi_m for translation carry: a registry-internal notation collision.)
- **L5840–5847 "current"**: active_tests ACTIVE_TESTS.json, corpus_summary, coverage_summary, SOURCE_INDEX.json, predecessor history/PREDECESSOR.json; authority_rule: **"RELATION.md is canonical mathematics; other files are indexes, evidence, executable realizations, or views."**
- **L5848–5859 "publication"**: authority /RELATION; handoff oeis/RELATION_HANDOFF.md; signed_translation_realization realizations/translation/reader.py; **gm_specialization: [realizations/gm/ENTRY.txt, realizations/gm/aXXXXXX.txt, realizations/gm/bXXXXXX.txt, realizations/gm/aXXXXXX.py.txt]**; **"live_submission_status": "external/current bytes required before publication claims"**. (n: This four-file set — ENTRY + a-file + b-file + program — is the evident structure of the submission "quartet" (entry text, a-file, b-file, program). RELATION_HANDOFF L7 says the *live* quartet is not included; the local gm quartet uses placeholder aXXXXXX names — per EXPECTATION_FIELD L503–505, "Placeholder filenames must not be presented as assigned identifiers". Also note the local quartet is the GM specialization, whereas the handoff names the signed translation-carry array as the publication realization: the two must be reconciled before any edit.)

### G summary for brief categories (registry-wide)
- (a) Radius: none; the geometric vocabulary is: nonradial double (RR-NONRADIAL-DOUBLE), relative disk (RR-RELATIVE-DISK, "response_is_not_a_metric"), mapping torus (OP100 -> RR-S8), winding on cyclic words (RR-GM-WINDING), log-scale phase winding (RR-M6), Alexandrov/intrinsic topology (RR-INTRINSIC-TOPOLOGY), "width_does_not_return_common_origin" (RR-PHASE), "origin_readdress_retains_integer" (RR-LANDMARK-RETURN), "higher_winding_not_same_uniqueness" (RR-FORCED-PROFILE), "vector_metric_not_scalar_isometry" (RR-CONSTITUTION-RETURN).
- (b) Lens: RR-CONSTITUTION-RETURN (moving endpoint lenses, placement_dependence, source_mean_after_placed_inverse, nonlinear_mean_counterexample), RR-S8 metaplectic LCT, RR-PROFILE apertures, RR-M8 noncommuting delay-scale, RR-EM metamer/alias.
- (c) Physics: RR-PHYSICAL-CALIBRATION (calibration cancellation, common geometry phase), RR-JOINT-CALIBRATION (projected intervals), RR-M7 Doppler ratios/Lorentz ratio invariance, RR-EM, OP107 TIME -> domain limits.
- (d) Codes: RR-B3, RR-CODE-CHARACTER (puncture/extension bijection, [8,4,4] even self-dual, fano_lines_not_code_identity), RR-SECTION-OBSTRUCTION (six structural obstructions to equivariant sections), RR-T4 B9 tests (syndrome ≠ word; complement preserves syndrome), RR-COHERENT-REST (X/Z compensation), RR-LATTICE-INCIDENCE (Tanner signed gradient), RR-MODEL-ATTAINMENT (code_normalization_not_selfdual).
- (e) Interrogatives: RR-ROLES + no_fixed_interaction_arity; NOT = OP021, n't = NOR OP022; no WAY etc.
- (f) Residual: OP108 ERROR/residual -> RR-T4; RR-FORCED-PROFILE zero-sum residuals & correction_cocycle; RR-PHASE displacement_plus_remainder/uniform_error; RR-ANALYTIC-SEAM modular_filter_cannot_see_quotient; RR-N2 joint quotient/remainder transport; RR-T2 zero ≠ undefined ≠ excluded.
- (g) Fitting: RR-MODEL-ATTAINMENT force_projection_not_model_validation; RR-DISTRIBUTION-RETURN (means/covariance ≠ law); RR-T3 fixed_point_no_depth_cut; RR-QUOTIENT-PHASE irrational_phase_kernel_symbolic; RR-RELATIVE-DISK force_radical_not_rounded.
- (h) 142857: RR-PRESENTATION-CHECK repetend_wall_six_not_seven_nines; RR-MULTIPLICATIVE-PHASE unit radix rotations; RR-PHASE repetend_spectrum; RR-I1 cyclotomic.
- (i) Untested findings: RR-T7, RR-S3, RR-S7, RR-OEIS-TRANSFORM-GRAPH have "tests": []. Open: RR-PRCT-TRANSPORT native exports; RR-QUOTED-DERIVATION original program missing; live submission bytes required.
- (k) Constants-first: RR-SYMBOL-RETURN (constant_enclosures_positive, constants_certified_affine_composition, constants_scale_unchanged), RR-PHASE (pi_certificate, certified_sequences, decimal_prefix, interval_contrast), RR-JOINT-CALIBRATION (full projected interval, dual certificate), RR-FORCED-LAW (forced_value, inconsistency_is_not_uniqueness), RR-REFINEMENT-ATTAINMENT (noninteger_not_forced_as_integer).
- (l) Transitions: RR-INCIDENCE-RETURN (exact differences, one level per component), RR-QUOTED-DERIVATION (second_difference_return, endpoint_forces_total_increment), RR-S3 (inversion of differences), RR-CHARACTER-SEAM (jump_character_return), RR-ANALYTIC-SEAM (sinc_boundary_half_weight), RR-A1 (A8_signed_seam), RR-INDEX-TRANSPORT, RR-RESPONSE-SERIALIZATION (mixed_radix steps), RR-CONTINUATION-EQUALITY (coherent_old_sign_not_global), RR-QUOTIENT-PHASE (phase_derivative_returns_quotient).
- (m) Hex/RM: RR-B1 (Walsh + Möbius over all truth tables = RM/ANF), RR-CODE-CHARACTER ([8,4,4]), RR-COUNTERCORRELARY-APERTURE (256=8·8·4; 128=4·8·4), RR-SYMBOL-RETURN (HXE convention, case_carry_mask_counts). No [15,11,3]/[16,11,4]/GF(16)/GF(4) finding.
- (n) OEIS: RR-TRANSLATION-PUBLICATION, RR-PUBLIC, RR-ENTRY, RR-NEIGHBORS, RR-PRESENTATION-CHECK (submitted_routine_fails_exact_jump), publication block (quartet files, live bytes required).
- (o) Container/aperture: RR-COUNTERCORRELARY-APERTURE, RR-PROFILE (reciprocal aperture), RR-PRCT-TRANSPORT (separating apertures), RR-CHARACTER-SEAM (countersector_return), RR-INVARIANTS (neutral_return).

---

## H. Cross-file "aha" implications (mine, after extraction)

1. **The torus has a legitimate successor, and it is radius-free**: SIGMA's D_5 dihedral game (rotation P, reflection J, JPJ=P^-1) + REGISTRY RR-NONRADIAL-DOUBLE ("doubled inverse-sheet cyclometry without radial geometry", built from the dihedral method) + OP100 "torus / mapping torus" -> RR-S8 metaplectic. The drafts' T^2(13,3) should be replaced by a mapping torus / dihedral orbit whose only data are period, orientation (J) and monodromy (metaplectic double cover); inward/outward "flip" = J (reflection, SE.8) which *transforms* the reading by A, it does not invert values.
2. **"Coherent 16 / displaced 112" is horizon-relative**: SIGMA SE.14: under the five shifted horizons only {0,127} are coherent for all, 76 words for none. Displacement status is a function of the observer face, and syndrome ≠ displacement (7->19, syndrome 6; B9_syndrome_is_not_full_word).
3. **Where 3 and 7 legitimately live**: r=3 check rank, N=π=7 block length, 3 generator of F_7^*, b=N+r=10, ord_7(10)=6, τ(6)=4=K (SE.34–40); three probes decode/every two-probe family fails (RR-PARTICIPATION-PROBES); rank cascade 3,5,6 (SE.10). None of this is D=3 space. 13 appears only as a prime factor of Φ_6(10)=91=7·13 (my observation) — a typed arithmetic home, not a torus radius.
4. **The full-reptend closure does not extend to R=4**: SE.35 at (q,r)=(2,4) gives N=15, not prime, so the SE.40 chain (π=N, ord_π(b)=N−1) breaks; the Rubicon's [15,11,3] "R=4 extension" has no 142857-type return (mine). Also SIGMA L792–794 contains an arithmetic slip ((3,2) gives N=4, K=2, b=N+r=6, not K=6/b=10).
5. **Constants-first is interval certification, not derivation**: EXPECTATION_FIELD L247–249 (interval-stable digits only), REGISTRY RR-SYMBOL-RETURN (certified enclosures), RR-JOINT-CALIBRATION (projected intervals with dual certificates), RR-QUOTIENT-PHASE ("irrational_phase_kernel_symbolic"), RR-RELATIVE-DISK ("force_radical_not_rounded"). The drafts' 0.73336≈11/15, H0=73.04, λ=0.033 would need to be recast as certified intervals of measured values, with any rational approximant typed as a separate claim.
6. **A universal lens cannot generate constants**: RR-PHYSICAL-CALIBRATION "physical_calibration_cancellation" / "common_geometry_phase" and RR-M7 "common-reference cancellation": a factor common to all observations (PrePub2's L^w) cancels from ratios; it can only be calibrated. The placed-lens law (RR-CONSTITUTION-RETURN "source_mean_after_placed_inverse", "placement_dependence") is the snowball's lens math.
7. **"Error is remainder" -> (quotient, remainder, carry) triple**: SIGMA SE.30–31 (AND = interstitial carry; remainder cannot recover quotient), RR-ANALYTIC-SEAM "modular_filter_cannot_see_quotient", RR-N2 joint quotient/remainder transport, and the publishable object itself is the carry profile floor((u+h)/m) (RELATION_HANDOFF L12–13).
8. **Fano is a cocycle, not an identity**: SIGMA SE.24 κ(a,b)=e(a)+e(b)+e(a+b) is the Fano cocycle of the coset-leader section; REGISTRY RR-CODE-CHARACTER "fano_lines_not_code_identity"; RR-SECTION-OBSTRUCTION "six_obstructions_not_choice_failure" and RR-EQUIVARIANT-RETURN "whole_stabilizer_has_no_fixed_lift": no labelling of the 7 columns is symmetric under the full automorphism group — the WHO/WHAT/... assignment is necessarily a non-equivariant chart choice.
9. **The Rubicon's H column order is non-standard**: SIGMA uses masks 85/102/120 (column i = binary i). The Rubicon's WHO=110, WHAT=101, WHERE=011, WHEN=111, WHY=100, HOW=010, WHICH=001 is a permutation; as a chart, every claim must carry the permutation and survive the countercorrelary canary (FINDINGS L264–270).
10. **OEIS side**: the quartet = ENTRY + a-file + b-file + program (REGISTRY L5852–5857), placeholders aXXXXXX; live bytes absent (L5858; HANDOFF L7–10); a submitted routine fails at an exact jump (RR-PRESENTATION-CHECK); Φ notation collision (translation carry vs cyclotomic); GM specialization vs signed translation-carry realization must be reconciled.
