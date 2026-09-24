# Extract G

Reader G. Assigned sources:
- F1 `src/sources/methods/OEIS_EDITORIAL_EXPECTATION_FIELD.md` (677 lines)
- F2 `src/sources/methods/SIGMA_EPOCH_DIHEDRAL_META_FORMULARY.md` (847 lines)
- F3 `snow/relation/REFERENCES.md` (265 lines)
- F4 `snow/relation/coverage/MATHEMATICAL_FIELDS.md` (92 lines)
- F5 `snow/relation/corpus/FINDINGS.md` (270 lines)
- F6 `snow/relation/oeis/RELATION_HANDOFF.md` (162 lines)
- F7 `snow/relation/REGISTRY.json` (5860 lines, 169 KB)

Line numbers refer to each file. Quotes are exact short excerpts. The brief's category letters (a–j) tag each item.

---

## F1: OEIS_EDITORIAL_EXPECTATION_FIELD.md

This file is an editorial-review method for a novel OEIS submission. It is not physics. It matters here because it spells out how interrogatives, Hamming, 142857, residual and "no verdict from syndrome" are meant to be used: as review overlays and not as a source of meaning.

### (e) Interrogatives
- F1 L124: "The interrogatives are an editorial-review overlay. They are not claimed to be OEIS terms."
- F1 L126–143: a **16-row** interrogative table. The rows are WHAT=identity, WHO=warrant, WHEN=indexing, WHERE=placement, HOW=derivation, WHICH=discrimination, **WAY=orientation** ("Which choices, signs, directions, or branches make the construction determinate?"), WHY=interest, WHENCE=provenance, WHITHER=family, WHEREFORE=necessity, HOWSOEVER=portability ("software, radix, precision"), WHATEVER=information ("preserved or lost at every representation change"), WHICHSOEVER=coherence, WHOMSOEVER=maintainability, HORIZON=whole return.
  - Aha: this is neither 7 nor 10. The interrogative set is open and grows with the task. Rubicon v1's fixed "7 universal interrogatives" is one chart among several. WHERE here means *placement*, which is the same word the snowball uses for the lens (the pair (G(p), G(p+d)-G(p))). WAY means orientation/sign/branch. Neither is a radius.
- F1 L20–22: companion `OEIS_INTERROGATIVE_RELATION_FIELD.tsv` "source tangibles translated across the interrogatives". L39–41: it supplies "navigable translations, not automatic judgments of importance or independent corroboration."

### (d) Hamming / [7,4,3] / [8,4,4] / syndrome
- F1 L163–167: "The seven-nonzero-column binary apparatus is retained only as an optional local chart; the classical coding name is a reference alias. The general review does not project prose into bits, infer meaning from a syndrome, or compare fields without a crosswalk."
  - Direct repair for Rubicon v1: its label-to-column assignment (WHO=110, and so on) is a chart. A syndrome does not carry meaning unless a declared crosswalk exists.
- F1 L172–173: "L02's declared code decomposition is an exact return with its syndrome retained, not evidence for L01's physical or security claims."
- F1 L12–14: "A source ledger, incidence count or zero syndrome cannot award submission strength."
- F1 L364–367: Q-ary checks keep "the exactly-once projective-column hypothesis. Their prime-field execution is not an extension-field implementation. A valid fiber theorem, a supplied source encoding and a physical measurement return remain different warrants." This is the three-way separation: theorem vs encoding vs physical measurement.
- F1 L545: "Decimal, binary kernel/quotient, and structural views state one invariant" (resonates), versus "Equal-looking projections are silently identified as the same object" (deadens).
- F1 L637–639: "the exact affine contact with `[8,4,4]`".
- F1 L653–677, "7,4,3 pushback field": "The existing seven-coordinate record exposes four localities and three return relations as one navigation chart, not the necessary form of every expectation. Unrepresented distinctions must remain in the source" (L656–659).
  - L670–674: "An eight-coordinate extension is a declared diagnostic chart, not implied by seven recorded facets. Appending parity gives an even-weight [8,7,2] word; membership in [8,4,4] additionally needs the original Hamming checks. Any chosen codeword/syndrome split retains its section and the section discrepancy under coordinate changes". See `EIGHT_COORDINATE_ROUTE_CARTOGRAPHY.md`.
  - L675: "No such binary return establishes an editorial or native-return verdict."
  - Correction relevant to Rubicon: 4 data + 3 check = "four localities and three return relations". The split into codeword and syndrome is a *section* choice and is not invariant under coordinate change. So "3 rows = 3+1 spacetime" and "H^T H = Laplacian" type readings depend on the section.
- F1 L663–668: "Pareto-layers active pressure sets by inclusion", "The analyzer does not assign taste scores."

### (f) Residual / error / correction
- F1 L6–7: the document "does not assume that any requirement is already satisfied."
- F1 L117–120: "An unresolved conflict remains unresolved after being recorded; this is not satisfaction of the criterion."
- F1 L150–160 (Rubicon return mechanics): 1 "each tangible remains at its source locality"; 2 "a shared alias creates co-presence, not equality"; 3 "a semantic edge exists only under a declared crosswalk"; 4 source motion is typed (boundary, method, feedback, countervector, authority, protocol/harm, historical, material, witness, silence); 5 "incomparable or prohibited relations remain `non_glue`"; 6 "closure contracts generate exact residual sets for missing companions"; 7 "a correction walk appends one changed observation and reports both resolved and newly exposed residuals"; 8 "horizon closure means every relation returned, queued, or retained as non-glue, never that the mathematics or submission has been approved."
  - Aha: the same word ("alias") appearing twice gives co-presence, not equality. This directly blocks Rubicon's move from "137 appears in both" to "137 is derived".
- F1 L169–171: "L01 proposes residual-only reconstruction; centering removes a mean, not arbitrary stochastic interference. Its retained signal plus the mean has an exact return, while correlation alone can retain further ambiguity."
- F1 L100–109, response domain: "The section-shear source has zero coefficient response along an open path when the retained position sum is zero; an unchanged reading does not establish an unchanged section." Prime valuations can become undefined, and signs are invisible to them. "retain undefined, zero, changed and unchanged observations separately".
  - Aha: an unchanged observation does not mean the underlying state is unchanged. This is fiber non-injectivity, and it corrects "zero syndrome = coherent/physical".
- F1 L595–596: "The executable emits every `IMPROVE` and `OPEN` row as an unresolved editorial residual, so graph density cannot conceal manual work."

### (g) Fitting / significance / evidence
- F1 L66–69: "Imperative wording, source count and agreement do not supply a strength verdict. A source-valid objection can require a change even when numerous other records repeat a favorable claim."
- F1 L79–84: counts describe the graph, "not its evidential strength. Copying a statement into a fresh atom can increase incidence without adding a warrant; splitting one source into several identifiers can increase source span without making the arguments independent."
  - Bears directly on Rubicon v1's "19 measurements, p<1e-5, 9.3 sigma". Measurements that share a premise (for example the same H0 = 67.4 base, or the same 11/15 base) are not independent evidence.
- F1 L45–46: "different pages alone do not prove independence."
- F1 L218–220: "Guesses, observed identities, verified ranges, and theorems must not be made to look equivalent. Matching many terms is evidence, not proof."
- F1 L541: "Computational agreement is allowed to impersonate proof" (deadens).
- F1 L247–249: "Only digits stable across a stated confidence interval belong in an uncertain numerical expansion. Precision provenance must accompany numerically derived digits." This applies to the "irrational base 0.73336" in Rubicon v1.
- F1 L525–527: Superseeker "suggestions may be approximations and require independent verification before becoming Formula".
- F1 L88–98: "deciding existence, exhibiting one witness, selecting an extremal witness and returning every compatible witness are different jobs"; "An aesthetic keyword, short formula or accepted neighbor does not adjudicate the current claim."

### (h) 142857, cyclotomic, radix
- F1 L111–120: "The 142857/999999 relation is used here as a normalization discipline, not as a numerical scoring gimmick". Each atom is entered once. The same atom can be read from several localities "without being duplicated". Opposing readings "remain attached as a signed contrast". Closure happens only when every root, branch, exception and conflict is accounted for.
- F1 L227–237: "declared invariant: ... decimal, ordered-edge, binary quotient, cyclotomic, divisor, or programmatic views"; "rational independence does not prove an integer generating family is saturated, and compatibility modulo a prime need not lift integrally"; "doubled-generator counterexample and modular lift obstruction"; "**Source-native geometries need their own transports; an affine-only canary is not geometry neutrality.**"
  - Aha (a, j): geometry neutrality has to be *shown* for each source-native geometry. Passing one affine test does not establish it. This bears on the "topographically neutral except in lensing" thesis: neutrality is a claim that needs a transport for each geometry.
- F1 L256–259: "test whether decimality is the object, a coordinate chart, or one readout of a radix-independent construction." Also L139, HOWSOEVER: radix portability.
  - For Rubicon/Cosmic: 137 = 4·31+13 and 142857 are radix-10 readouts, so their radix status has to be declared.

### (a) Geometry / metric / placement / order
- F1 L282–289: "Also retain any clock correspondence and intermediate state"; "SP57's font ordering needs its metric and tie rule plus a finite-predecessor argument; a common unit change does not replace these data."
- F1 L275–281: "Reconstruction includes the intended operations and retained addresses, not just values"; "SP59's A163357 distinguishes traversal from serialization and grid adjacency"; "An inverse without an available, usable operation does not establish a shorter reader task."
- F1 L301–307: "Familiar mathematical vocabulary is not a defect by occurrence. Actual OEIS entries use manifolds (A005026) and information entropy (A234468) as precise objects." A lexical screen does not certify clarity. `language_lint.py` reports REVIEW_REQUIRED, NO_MATCHES or INCOMPLETE.
- F1 L497–498: an ordered-edge/array structure "needs a declared flattening and an inverse row/cell reconstruction".

### (b) Lens / placement
- F1 L131: WHERE = "placement": "In which OEIS field or supporting file can a reader find it?" Editorial placement, not optical.
- F1 L140: WHATEVER: "What is preserved or lost at every representation change?" This has the same logical form as the lens-retention requirement.

### (c) Physics
- F1 L366–367: "A valid fiber theorem, a supplied source encoding and a physical measurement return remain different warrants."
- F1 L640–642: "the collaborator's Greek/physical MUSE leads. The MUSE rows are retained as `EXPLORATORY`; the exact logic, coding, encoding, language, and OEIS roles retain their own sourced namespaces."
- F1 L172: the code decomposition is "not evidence for L01's physical or security claims."

### (i) Prohibitions / open items
- F1 L482–491: AI use: "AI-generated pink-box responses, AI-as-author, unverified AI code, and bulk AI submissions are explicitly disallowed." The packet is "a review instrument, not as text to paste wholesale"; "the author must decide, verify, and own".
- F1 L349–354: "a caller's PROVED label and nonempty proof record are declarations, not proof verification"; "Review credit follows actual execution and manual work, never the name of the stage".
- F1 L357–362: "A source hash does not mean every statement in that source was tested. The V41 minimal-reader checker parses only matrix (38)".
- F1 L451–458: "'PASS' without a claim-to-check map is not review evidence"; "Do not silently repair an example and report the source as having passed."
- F1 L625: "It does not mean that the OEIS submission has passed review." L650–651: "does not predict acceptance."
- F1 L14–15: second perimeter "does not execute its prose contracts or predict acceptance."
- F1 L333–341: complexity/acquisition: "SP43's AND/OR formula complexity changes when XOR is available; reader count is not computation cost"; "Inclusion-minimal need not mean minimum cardinality"; "Query identity and conditioning cannot carry uncharged source information."
- F1 L553–577: conflict register with 9 tensions kept on purpose. L575–577: "Novel object / editor familiarity: do not dilute novelty, but provide a first-principles verification path".
- F1 L478–480: "Novelty raises the burden of orientation, claim typing, and independent reconstruction."

### (j) Repair implications from F1
- Separate claim types: theorem, conjecture, checked range, and fit (L218, L541).
- Declare the invariant across representations (L227).
- Keep the source/scope/dependencies of each claim, and do not count shared-premise repeats as independent evidence (L79–84). This rules out "9.3 sigma" when the evidences share a premise.
- "Short public path, complete reconstruction path" (L271).
- Separate the proposed/new composition from standard ingredients (L432–435). For Rubicon: Hamming [7,4,3], Fano and PSL(2,7) are standard ingredients. The labelling and physics mapping are the new composition, and they need separate warrant.

