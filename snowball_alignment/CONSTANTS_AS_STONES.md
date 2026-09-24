# Constants as stones, measurements as flows: tracing the buttress

The constants are the stones in the riverbed. The measurements are the flows that pass around them. A measurement does not touch a constant directly: it **compares two physical processes**, and the constant is what the comparison routes around. To see where the stones hold the flow, where the buttress is, every flow must first be put in **one metric and one unit**.

Everything below is computed by `checks/constants_network.py` → `NETWORK_RESULTS.json`. Values tagged `[recall]` in the script must be confirmed at the primary source; the structure does not depend on their last digits.

---

## 1. The normalization: C e M

| Letter | Role | Why |
|---|---|---|
| **C** | c turns every mass into an energy (E = mc²). With h (E = hν, E = ħω) and k_B (E = kT) it puts every constant on one energy line. | same unit |
| **e** = 2.718… | positions are natural logarithms. Products become sums, rates add (a rate is an e-folding), and one e-fold is one unit of distance. | same metric |
| **M** | a reference mass-energy mc² is the origin. The electron is used here. | the single anchor |

- **The origin is the one anchor.** Moving it (to m_p, say) shifts every stone equally and changes no gap. This is the same "one anchor per component" that re-inverts the transition map (TI3, OG1).
- **Only gaps are physical.** Every physical statement is a gap between stones, and each gap is an integer combination of the four independent dimensionless stones of this chart:

  | Stone | Value | Meaning |
  |---|---|---|
  | α | 1/137.036 | |
  | μ = m_p/m_e | 1836.15 | |
  | G_CEM | 2.40×10⁻⁴³ | the ratio of gravity to electrostatics between two electrons |
  | H0_CEM | 2.05×10⁻⁴¹ | the Hubble rate in electron-radius units |

  These four generate the whole integer lattice of dimensionless combinations. Lattice index 1 is certified by the gcd of 4×4 minors.
- **Units are sections.** SI, CEM (c = e = m_e = k_e = 1), Planck and atomic units are four sections of the same dimension map. They display different numbers, but every dimensionless coordinate and every loop holonomy agrees to machine precision. That is the snowball's HR2: changing the section changes what is displayed, never the return.
- **In CEM, the quantum of action shows up as 1/α.** With c = e = m_e = k_e = 1, ħ = 137.036. The single measured electromagnetic stone appears as the size of the quantum itself.

## 2. The riverbed: where the stones are (e-folds from the electron's rest energy)

| e-folds | gap | stone | what it is in the physical world | how flows reach it |
|---:|---:|---|---|---|
| −88.77 | — | ħH₀ | one e-fold of cosmic expansion per Hubble time, as an energy (1.4×10⁻³³ eV) | CMB via ΛCDM; distance ladders |
| −23.32 | 65.45 | hν_Cs | the SI second: one Cs-133 hyperfine flip | exact by definition |
| −21.50 | 1.82 | kT_CMB | thermal energy of the relic radiation today | FIRAS blackbody |
| −19.25 | 2.26 | ρ_Λ^¼ | the vacuum-energy scale | *derived* from H₀, Ω_Λ, G |
| −10.53 | 8.71 | Rydberg | binding energy of hydrogen | 1S–2S two-photon, counter-propagating |
| −9.84 | 0.693 | Hartree | atomic energy unit (= 2 Rydberg: the gap is ln 2) | identity |
| −4.92 | 4.92 | α·m_ec² | one α-step below the electron | identity |
| 0 | 4.92 | m_ec² | the electron's rest energy (origin) | Penning trap, bound-electron g |
| 4.92 | 4.92 | m_ec²/α | one α-step above | identity |
| 5.33 | 0.41 | m_μc² | muon rest energy | |
| 7.52 | 2.18 | m_pc² | proton rest energy (= ln μ) | Penning ratios, HD⁺ spectroscopy |
| 8.15 | 0.64 | m_τc² | tau rest energy | |
| 11.97–13.09 | | W, Z, H, v | the electroweak cluster: four stones within 1.1 e-folds | colliders; muon lifetime |
| 51.53 | 38.44 | E_Planck | where a quantum's own gravity matches its scale | G measurements |

What the riverbed shows:

- **The electromagnetic stones form an exact ladder**, one α-step (4.920 e-folds) apart. This is an identity (Rydberg = 2 ln α − ln 2, and so on), not a finding.
- **Hubble → Planck spans 140.29 e-folds.** The dark-energy stone sits 0.63 e-folds from the exact midpoint *by construction*: ρ_Λ^¼ = (3Ω_Λ/8π)^¼ · √(ħH₀·E_P). It is a derived stone, placed by H₀ and G, not a separate stone.
- **Large gaps:** electroweak → Planck is 38.4 e-folds (the hierarchy problem), and Cs second → Hubble is 65.4.
- **Retained as fibers, with no map declared:** the muon lies 0.41 e-folds from the α-step above the electron, and kT_CMB lies within 2.3 e-folds of the vacuum scale (the "why now" coincidence).

## 3. The flows: what each measurement actually compares

| Direction class | What is compared | What the symmetry cancels | Examples |
|---|---|---|---|
| **Dual-direction** | the same process run both ways (±k photon kicks, counter-propagating beams, source masses near/far) | the J-odd part: first-order Doppler, linear drifts, position-odd systematics. The reading is the J-even part (u + Ju)/2 (snowball NR14). | Rb and Cs recoil; H 1S–2S; time-of-swing G; atom-interferometer G |
| **Direct ratio of one system** | two frequencies of the same particle in the same trap | common fields and calibrations | electron g−2 (anomaly vs cyclotron); ion cyclotron mass ratios |
| **Theory transport** | a measured quantity carried to the stone through a model | nothing: the model is part of the flow | α from g−2 through QED; H₀ from the acoustic scale through ΛCDM |
| **Calibration chain** | rung-by-rung placed comparisons (flux vs distance) | nothing: each rung is a placed lens | Cepheid ladder; TRGB ladder |

## 4. The buttress: where the flows close and where they pile up

Two independent flows to one stone form a loop. The loop's total in e-folds (its holonomy) is **unit-free**, the same in every section, and it is located on the transports the two flows do **not** share. Shared transports cancel around the loop (the snowball's RR-INCIDENCE-RETURN).

**The α stone** (3 flows, 2 loops, Birge ratio 3.94)

| Loop | holonomy (e-folds) | z | exposed (not shared) | cancelled (shared) |
|---|---:|---:|---|---|
| Rb recoil ↔ Cs recoil | 1.17×10⁻⁹ | 5.5 | Rb h/m, Cs h/m, m_Rb/m_e, m_Cs/m_e | R∞, m_e |
| g−2 ↔ Cs recoil | 8.8×10⁻¹⁰ | 3.9 | QED, a_e hadronic, R∞, Cs h/m, m_Cs/m_e, m_e | — |
| g−2 ↔ Rb recoil | −2.9×10⁻¹⁰ | −2.2 | the Rb counterparts | — |

The flow piles up between the two recoil routes, *after* R∞ and m_e have cancelled. The tension is therefore located in the atom-specific legs (h/m of each atom, and its Penning mass ratio), not in hydrogen spectroscopy and not in QED. The g−2 flow lies between the two, closer to Rb.

**The Hubble stone** (3 flows, Birge ratio 3.57)

| Loop | holonomy | z | exposed | cancelled |
|---|---:|---:|---|---|
| CMB ↔ Cepheid ladder | −0.0804 | −5.0 | ΛCDM history, sound horizon, parallax zero point, Cepheid P–L, SN Ia, local flow | — |
| Cepheid ↔ TRGB | 0.045 | 1.6 | Cepheid P–L, TRGB zero point, parallax | SN Ia standardization, local flow |
| CMB ↔ TRGB | −0.035 | −1.4 | … | — |

The largest pile-up shares no transport at all: it runs through a model on one side and a ladder on the other. Between the two ladders, where SN Ia and local flow cancel, the loop nearly closes (1.6σ). So the flow splits at the ladder/model fork, not inside the SN leg.

**The Planck (G) stone** (7 flows, 6 independent loops, Birge ratio 4.45)

The strongest loops are BIPM ↔ JILA (z = 9.9), HUST time-of-swing ↔ BIPM (−7.6), HUST angular-acceleration ↔ JILA (7.2) and UWash ↔ BIPM (−7.0). The only shared transport is the SI mass/length realization, which cancels in every loop. So every pile-up is located on the individual **apparatus**. This stone is the one the flows buttress least coherently: many flows, turbulent, with the disagreement carried by the instruments rather than by any shared theory. CODATA's expansion of the G uncertainty is a common widening applied to all loops at once. The snowball's joint-calibration rule would instead keep each apparatus's leg and project them jointly.

**Stones whose flows close** at this depth: the Rydberg, electron and proton stones. Their loops close to parts in 10¹¹–10¹², and their primary flows are yet to be entered (see §7).

## 5. What the pattern says

1. **Holonomy sits at the forks, not uniformly.** Where two flows share their long legs and differ in a short one, the loop exposes that short leg: the atom-specific recoil legs for α; the apparatus for G; the model-vs-ladder fork for H₀. There is no single lens common to all measurements. A common lens would cancel from every loop, so it can only be calibrated (snowball RR-PHYSICAL-CALIBRATION).
2. **Dual-direction flows reach deepest.** The flows that close to the smallest holonomy (the recoil and 1S–2S legs) are the ones where the comparison is run both ways, so the J-odd terms cancel. The one-way calibration chain (the Cepheid ladder) carries the largest pile-up.
3. **Some stones are derived, and their positions are set by others.** The dark-energy scale is placed by H₀ and G. The Hartree, Rydberg and α-steps are placed by α. The independent stones of this chart are exactly four.

## 6. How this re-reads the earlier drafts

- **The Rubicon was reading flows, and that was the right instinct.** Most of its "19 measurements" are flow quantities, not stones: uncertainties, the H₀ tension (73.0/67.4 − 1 = 0.0831, which is the CMB ↔ ladder loop; in e-folds, ln(73.04/67.4) = 0.080), the G expansion factor (a Birge-type widening). The corrected form is the loop holonomy in e-folds, with the transports it exposes named. It is not base^n.
- **The Cosmic Pattern's "each path through its own lens" is the admissible idea.** The correct form is per-loop exposed transports, not one universal L^w.

## 7. The same shape in the code mathematics

- In GF(2ʳ) the elements fixed by Frobenius are exactly {0, 1}, the **field of constants** (✔ TI12). The transition phase z ↦ z² + 1 is Frobenius followed by translation by the constant 1. It leaves the stone set in place, exchanges its two members (the 0 ↔ 9 wall), and every other state flows around them. At even r (hex, byte) the flow gains two more fixed stones: the cube roots of unity, which are the thirds (0x5, 0xA).
- The 168 linear symmetries all fix the origin stone. The order-6 decimal flow passes through the stones by translation, i.e. through the eighth coordinate (✔ TI9). The riverbed does not contain the flow; it shapes it.

## 8. Obligations to finish the trace

1. Confirm every `[recall]` value, and add the full covariance where the flows share inputs (CODATA correlation matrices).
2. Enter the primary flows for the closing stones: R∞ (H/D spectroscopy, including the proton-radius loop, historically a ~7σ pile-up that later measurements have largely closed), μ (Penning vs HD⁺), m_e (bound-electron g). Their loops are the calibration of "closes".
3. Add the remaining H₀ flows (lensing time delays, masers, gravitational-wave sirens) and the remaining CODATA G inputs. Then compute the full cycle space rather than pairwise loops.
4. For each loop with nonzero holonomy, list the physical legs that would have to move to close it, and by how much in e-folds. That list is the concrete, testable form of "where the buttress is".
