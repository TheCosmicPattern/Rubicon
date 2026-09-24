#!/usr/bin/env python3
"""
Constants as stones, measurements as flows: the unit-free measurement network.

Picture (author's): the constants are the stones in the riverbed; measurements are
the flows that pass around them. What a measurement "tangibly indicates" is a
COMPARISON between two physical processes. Some comparisons run in both directions
(counter-propagating beams, swapped ions, near/far source-mass configurations), some
are direct ratios of two frequencies of one system, and some reach the stone only
through a theory transport (QED, LambdaCDM) or a calibration chain (distance ladder).
To trace the buttress, every flow has to be put in one metric and one unit.

Mathematics (RELATION.md, used as stated there):
 * Dimensional analysis is an integer observation: D : Z^constants -> Z^(M,L,T,I).
   Its integer kernel (RR-INTEGER-ATTAINMENT IA1-IA2) is the lattice of dimensionless
   combinations: the only unit-free content. A unit system (SI, CEM, Planck) is a
   SECTION of D; changing it changes displayed values, never the kernel coordinates
   (RR-H-RETURN HR2: "changing the section changes the displayed residual while
   leaving the whole source return unchanged").
 * Several independent routes to one stone form closed loops. Reconstruction of a
   common value is possible exactly when every loop has zero signed total
   (RR-INCIDENCE-RETURN). A nonzero loop total (holonomy) is where the flow piles up
   against a stone: it is unit-free and it is located on the transports the loop does
   NOT share (shared transports cancel around the loop).
 * A dual-direction comparison records the J-even part (u + Ju)/2 of the doubled
   reading (RR-NONRADIAL-DOUBLE NR14): odd terms (first-order Doppler, linear drift,
   position-odd systematics) cancel; even terms remain and must be modelled.

PROVENANCE: [exact] = SI defining constant; [OEIS] = copied from an OEIS record;
[recall] = entered from memory of CODATA/PDG/primary papers and MUST be confirmed at
the primary source before any external use.  Nothing is fitted.

Run: python3 constants_network.py > ../NETWORK_RESULTS.json
"""
import json, math, sys
from fractions import Fraction as Q

# ------------------------------------------------------------------ 1. stones and dimensions
DIM = ("M", "L", "T", "I")
CONST = {  # symbol: (dimension exponents M,L,T,I ; SI value ; rel. std. uncertainty ; provenance)
    "c":    ((0, 1, -1, 0),  299792458.0,          0.0,      "[exact] SI"),
    "h":    ((1, 2, -1, 0),  6.62607015e-34,       0.0,      "[exact] SI"),
    "e":    ((0, 0, 1, 1),   1.602176634e-19,      0.0,      "[exact] SI"),
    "eps0": ((-1, -3, 4, 2), 8.8541878128e-12,     1.5e-10,  "[recall] CODATA 2018"),
    "m_e":  ((1, 0, 0, 0),   9.1093837015e-31,     3.0e-10,  "[recall] CODATA 2018"),
    "m_p":  ((1, 0, 0, 0),   1.67262192369e-27,    3.1e-10,  "[recall] CODATA 2018"),
    "G":    ((-1, 3, -2, 0), 6.67430e-11,          2.2e-5,   "[OEIS] A070058 / CODATA 2018"),
    "H0":   ((0, 0, -1, 0),  67.4e3 / 3.0856775814913673e22, 7.4e-3, "[recall] Planck 2018 (km/s/Mpc -> 1/s)"),
}
NAMES = list(CONST)

def dimvec(sym): return CONST[sym][0]

# integer kernel basis (named), each a dict symbol->integer exponent; the pure-number
# factors (2, 4pi) belong to the named quantity and are carried separately.
KERNEL = {
    "alpha":       ({"e": 2, "eps0": -1, "h": -1, "c": -1}, Q(1, 2), 0),       # e^2/(2 eps0 h c)
    "mu":          ({"m_p": 1, "m_e": -1}, Q(1), 0),                            # m_p/m_e
    "G_CEM":       ({"G": 1, "m_e": 2, "eps0": 1, "e": -2}, Q(4), 1),           # 4 pi eps0 G m_e^2 / e^2
    "H0_CEM":      ({"H0": 1, "e": 2, "eps0": -1, "m_e": -1, "c": -3}, Q(1, 4), -1),  # H0 r_e / c
}
# (dict, rational factor, power of pi)

def kernel_ok():
    out = {}
    for k, (vec, _, _) in KERNEL.items():
        tot = [sum(n * dimvec(s)[i] for s, n in vec.items()) for i in range(4)]
        out[k] = tot == [0, 0, 0, 0]
    return out

def lattice_index():
    """Index of the named basis in the full integer kernel (1 = it generates every
    integer dimensionless combination).  Kernel rank = #constants - rank D = 8-4 = 4.
    Index = gcd of maximal minors of the basis matrix divided by that of a true
    kernel basis; computed via Smith-form gcd of 4x4 minors."""
    from itertools import combinations
    B = [[KERNEL[k][0].get(s, 0) for s in NAMES] for k in KERNEL]
    def det(M):
        M = [row[:] for row in M]; n = len(M); d = Q(1)
        M = [[Q(x) for x in r] for r in M]
        for i in range(n):
            p = next((r for r in range(i, n) if M[r][i] != 0), None)
            if p is None: return 0
            if p != i: M[i], M[p] = M[p], M[i]; d = -d
            d *= M[i][i]
            for r in range(i + 1, n):
                f = M[r][i] / M[i][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
        return int(d)
    g = 0
    for cols in combinations(range(len(NAMES)), 4):
        g = math.gcd(g, det([[row[c] for c in cols] for row in B]))
    # the dimension matrix has rank 4 with gcd of its 4x4 minors:
    D = [[dimvec(s)[i] for s in NAMES] for i in range(4)]
    gd = 0
    for cols in combinations(range(len(NAMES)), 4):
        gd = math.gcd(gd, det([[D[i][c] for c in cols] for i in range(4)]))
    return g, gd

def kvalue(k, logv):
    vec, fac, pipow = KERNEL[k]
    return math.exp(sum(n * logv[s] for s, n in vec.items())) * float(fac) * math.pi ** pipow

# ------------------------------------------------------------------ 2. sections (unit systems)
def solve4(A, b):
    n = 4; M = [list(map(float, A[i])) + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]; M[r] = [a - f * c for a, c in zip(M[r], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]

SECTIONS = {
    "SI":     None,
    "CEM":    {"c": 1.0, "e": 1.0, "m_e": 1.0, "eps0": 1 / (4 * math.pi)},   # k_e = 1
    "Planck": {"c": 1.0, "h": 2 * math.pi, "G": 1.0, "eps0": 1 / (4 * math.pi)},  # hbar = k_e = 1
    "atomic": {"h": 2 * math.pi, "e": 1.0, "m_e": 1.0, "eps0": 1 / (4 * math.pi)},  # hbar = e = m_e = k_e = 1
}

def section_values(name):
    si = {s: math.log(CONST[s][1]) for s in NAMES}
    fix = SECTIONS[name]
    if fix is None: return si
    syms = list(fix)
    A = [dimvec(s) for s in syms]
    b = [si[s] - math.log(fix[s]) for s in syms]
    lam = solve4(A, b)            # log unit rescalings for M, L, T, I
    return {s: si[s] - sum(d * l for d, l in zip(dimvec(s), lam)) for s in NAMES}

# ------------------------------------------------------------------ 3. flows (routes to stones)
ROUTES = [
  # node, label, value, sigma, comparison actually made, direction class, transports
  ("alpha_inv", "a_e (Fan 2023)", 137.035999166, 0.000000015,
   "spin-flip (anomaly) frequency vs cyclotron frequency of ONE electron in a Penning trap",
   "direct frequency ratio of one system", {"QED series for a_e", "hadronic+weak a_e terms"}, "[recall]"),
  ("alpha_inv", "Rb recoil (Morel 2020)", 137.035999206, 0.000000011,
   "photon momentum hbar*k vs Rb atom velocity, Bloch/Raman kicks up and down",
   "dual-direction (+k/-k)", {"R_inf (H spectroscopy + QED)", "m_Rb/m_e (Penning)", "m_e (bound-e g, QED)", "Rb h/m apparatus"}, "[OEIS]"),
  ("alpha_inv", "Cs recoil (Parker 2018)", 137.035999046, 0.000000027,
   "photon momentum hbar*k vs Cs atom velocity, symmetric atom interferometer",
   "dual-direction (+k/-k)", {"R_inf (H spectroscopy + QED)", "m_Cs/m_e (Penning)", "m_e (bound-e g, QED)", "Cs h/m apparatus"}, "[recall]"),
  ("H0_kms_Mpc", "CMB (Planck 2018)", 67.4, 0.5,
   "angular size of the acoustic scale on the sky (sound horizon / angular distance)",
   "theory transport", {"LambdaCDM expansion history", "sound-horizon physics"}, "[recall]"),
  ("H0_kms_Mpc", "Cepheid ladder (SH0ES 2022)", 73.04, 1.04,
   "flux vs distance: parallax -> Cepheid period-luminosity -> SN Ia, rung by rung",
   "calibration chain (placed lenses)", {"parallax zero point", "Cepheid P-L", "SN Ia standardization", "local flow"}, "[recall]"),
  ("H0_kms_Mpc", "TRGB ladder (Freedman 2021)", 69.8, 1.7,
   "flux vs distance: red-giant-branch tip -> SN Ia",
   "calibration chain (placed lenses)", {"TRGB zero point", "SN Ia standardization", "local flow"}, "[recall]"),
  ("G_1e-11", "HUST-18 time-of-swing", 6.674184, 0.000078,
   "torsion period with source masses near vs far", "dual-configuration (near/far)", {"HUST TOS apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "HUST-18 angular-accel. feedback", 6.674484, 0.000078,
   "turntable angular acceleration needed to cancel gravitational torque", "direct balance", {"HUST AAF apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "UWash-00 AAF", 6.674255, 0.000092,
   "angular acceleration feedback torsion balance", "direct balance", {"UWash apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "BIPM-14 servo/Cavendish", 6.67554, 0.00016,
   "electrostatic servo torque vs gravitational torque", "direct balance", {"BIPM apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "UCI-14 time-of-swing", 6.67435, 0.00013,
   "cryogenic torsion period near vs far", "dual-configuration (near/far)", {"UCI apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "JILA-18 pendulum", 6.67260, 0.00025,
   "pendulum-cavity spacing with source masses moved", "dual-configuration", {"JILA apparatus", "SI mass/length"}, "[recall]"),
  ("G_1e-11", "LENS-14 atom interferometry", 6.67191, 0.00099,
   "gravity-gradient phase on Rb matter waves, source masses moved", "dual-direction (+k/-k)", {"LENS apparatus", "SI mass/length", "Rb h/m"}, "[recall]"),
]

def node_analysis():
    out = {}
    for node in dict.fromkeys(r[0] for r in ROUTES):
        rs = [r for r in ROUTES if r[0] == node]
        # log-space (unit-free) coordinates: ln(value); holonomy of a two-route loop
        # is ln(v1/v2), identical in every unit section because both routes read the
        # same stone with the same dimension vector.
        w = [1 / (r[3] / r[2]) ** 2 for r in rs]
        lnm = sum(wi * math.log(r[2]) for wi, r in zip(w, rs)) / sum(w)
        chi2 = sum(wi * (math.log(r[2]) - lnm) ** 2 for wi, r in zip(w, rs))
        n = len(rs)
        loops = []
        for i in range(n):
            for j in range(i + 1, n):
                a, b = rs[i], rs[j]
                hol = math.log(a[2] / b[2])
                sig = math.hypot(a[3] / a[2], b[3] / b[2])
                exposed = sorted(a[6] ^ b[6]); shared = sorted(a[6] & b[6])
                loops.append({"loop": f"{a[1]} -> stone -> {b[1]}", "holonomy_ln": hol,
                              "z": hol / sig, "exposed_transports": exposed, "cancelled_shared": shared})
        loops.sort(key=lambda d: -abs(d["z"]))
        out[node] = {
            "routes": [{"route": r[1], "value": r[2], "sigma": r[3], "compares": r[4], "direction": r[5],
                        "transports": sorted(r[6]), "provenance": r[7]} for r in rs],
            "independent_loops": n - 1,
            "weighted_mean": math.exp(lnm),
            "birge_ratio": math.sqrt(chi2 / (n - 1)) if n > 1 else None,
            "loops_by_tension": loops,
        }
    return out

def section_invariance():
    """Holonomy of the H0 loop and the G loops computed after converting each route to
    each unit section: identical (the section shift cancels around the loop)."""
    res = {}
    mpc = 3.0856775814913673e22
    for sec in SECTIONS:
        lv = section_values(sec); si = {s: math.log(CONST[s][1]) for s in NAMES}
        shiftH = lv["H0"] - si["H0"]; shiftG = lv["G"] - si["G"]
        h_planck = math.log(67.4e3 / mpc) + shiftH; h_shoes = math.log(73.04e3 / mpc) + shiftH
        g1 = math.log(6.674484e-11) + shiftG; g2 = math.log(6.67260e-11) + shiftG
        res[sec] = {"H0_loop_holonomy": h_shoes - h_planck, "G_loop_HUST_AAF_vs_JILA": g1 - g2,
                    "H0_value_in_section": math.exp(h_planck), "G_value_in_section": math.exp(lv["G"])}
    return res

# ------------------------------------------------------------------ 4. the riverbed: C e M
# c turns every mass into an energy (E = m c^2), h turns every rate/frequency into an
# energy (E = hbar*omega, E = h*nu), k_B turns every temperature into one (E = k T).
# e (= 2.718...) supplies the metric: positions are natural logarithms, so products
# become sums, rates add, and one e-fold is one unit of distance.  M: the reference
# mass-energy m c^2 sets the origin.  The choice of m is the single anchor (TI3/OG1);
# every physical statement is a GAP between stones, and gaps are independent of it.
EV = 1.602176634e-19                     # [exact] J per eV
KB = 1.380649e-23                        # [exact]
HBAR = CONST["h"][1] / (2 * math.pi)

def stones():
    c = CONST["c"][1]; me = CONST["m_e"][1]; mp = CONST["m_p"][1]; G = CONST["G"][1]
    H0 = CONST["H0"][1]
    a = kvalue("alpha", {s: math.log(CONST[s][1]) for s in NAMES})
    Ee = me * c * c
    OmL, Tcmb = 0.6847, 2.72548           # [recall] Planck 2018; Fixsen 2009
    rhoL = OmL * 3 * H0 ** 2 * c ** 2 / (8 * math.pi * G)          # J/m^3
    ELam = (rhoL * (HBAR * c) ** 3) ** 0.25
    GeV = 1e9 * EV
    S = [  # name, energy (J), what it is physically, how it is reached
        ("Hubble rate  hbar*H0", HBAR * H0, "one e-fold of cosmic expansion per Hubble time, as an energy", "CMB via LambdaCDM / distance ladder"),
        ("dark-energy scale rho_L^(1/4)", ELam, "fourth root of the vacuum energy density", "H0, Omega_L, G combined"),
        ("Cs hyperfine h*nu_Cs", CONST["h"][1] * 9192631770, "the SI second: one Cs-133 ground-state flip", "[exact] SI definition"),
        ("CMB photon k*T_CMB", KB * Tcmb, "thermal energy of the relic radiation today", "FIRAS blackbody spectrum"),
        ("Rydberg  R_inf*h*c", a * a * Ee / 2, "binding energy of hydrogen (infinite nuclear mass)", "1S-2S two-photon, counter-propagating"),
        ("Hartree  alpha^2 m_e c^2", a * a * Ee, "atomic unit of energy", "= 2 Rydberg exactly"),
        ("alpha * m_e c^2", a * Ee, "Coulomb energy at the reduced Compton wavelength", "one alpha-step below m_e c^2"),
        ("electron  m_e c^2", Ee, "rest energy of the electron (ORIGIN of this chart)", "Penning trap / bound-electron g"),
        ("m_e c^2 / alpha", Ee / a, "electron rest energy one alpha-step up", "one alpha-step above m_e c^2"),
        ("muon  m_mu c^2", 105.6583755e6 * EV, "muon rest energy", "[recall] PDG"),
        ("proton  m_p c^2", mp * c * c, "proton rest energy", "Penning trap mass ratios; HD+ spectroscopy"),
        ("tau  m_tau c^2", 1776.86e6 * EV, "tau rest energy", "[recall] PDG"),
        ("W  m_W c^2", 80.377 * GeV, "W boson rest energy", "[recall] PDG 2022"),
        ("Z  m_Z c^2", 91.1876 * GeV, "Z boson rest energy", "[recall] PDG 2022"),
        ("Higgs  m_H c^2", 125.25 * GeV, "Higgs boson rest energy", "[recall] PDG 2022"),
        ("electroweak v", 246.22 * GeV, "Higgs vacuum expectation value (from G_F)", "[recall] muon lifetime"),
        ("Planck  sqrt(hbar c^5/G)", math.sqrt(HBAR * c ** 5 / G), "energy at which gravity of a quantum equals its own scale", "torsion balances etc. (G)"),
    ]
    rows = [{"stone": n, "energy_eV": E / EV, "efolds_from_electron": math.log(E / Ee),
             "is": what, "reached_by": how} for n, E, what, how in S]
    rows.sort(key=lambda r: r["efolds_from_electron"])
    for i in range(1, len(rows)):
        rows[i]["gap_efolds_from_previous"] = rows[i]["efolds_from_electron"] - rows[i - 1]["efolds_from_electron"]
    # exact gap identities (integer combinations of the kernel stones + pure numbers)
    la = math.log(a); lGc = math.log(kvalue("G_CEM", {s: math.log(CONST[s][1]) for s in NAMES}))
    lH = math.log(kvalue("H0_CEM", {s: math.log(CONST[s][1]) for s in NAMES}))
    pos = {r["stone"]: r["efolds_from_electron"] for r in rows}
    ident = {
        "Rydberg = 2 ln(alpha) - ln 2": abs(pos["Rydberg  R_inf*h*c"] - (2 * la - math.log(2))) < 1e-12,
        "alpha-steps equally spaced": abs((pos["electron  m_e c^2"] - pos["alpha * m_e c^2"]) - (pos["m_e c^2 / alpha"] - pos["electron  m_e c^2"])) < 1e-12,
        "Planck = -(1/2) ln(alpha * G_CEM)": abs(pos["Planck  sqrt(hbar c^5/G)"] + 0.5 * (la + lGc)) < 1e-9,
        "Hubble = ln(H0_CEM) - ln(alpha)": abs(pos["Hubble rate  hbar*H0"] - (lH - la)) < 1e-9,
        "proton = ln(mu)": abs(pos["proton  m_p c^2"] - math.log(1836.15267343)) < 1e-6,
    }
    return {"alpha_step_efolds": -la, "stones": rows, "gap_identities": ident,
            "span_efolds_hubble_to_planck": pos["Planck  sqrt(hbar c^5/G)"] - pos["Hubble rate  hbar*H0"]}

def main():
    logv = {s: math.log(CONST[s][1]) for s in NAMES}
    g, gd = lattice_index()
    kern = {k: kvalue(k, logv) for k in KERNEL}
    sections = {}
    for sec in SECTIONS:
        lv = section_values(sec)
        sections[sec] = {"constants": {s: math.exp(lv[s]) for s in NAMES},
                         "kernel_coordinates": {k: kvalue(k, lv) for k in KERNEL}}
    inv = all(abs(sections[s]["kernel_coordinates"][k] / kern[k] - 1) < 1e-9 for s in SECTIONS for k in KERNEL)
    cem = sections["CEM"]["constants"]
    out = {
        "kernel_members_dimensionless": kernel_ok(),
        "kernel_lattice_index": {"gcd_4x4_minors_basis": g, "gcd_4x4_minors_dimension_matrix": gd,
                                 "reading": "basis generates the full integer kernel iff these agree up to sign"},
        "kernel_values": kern,
        "sections": sections,
        "kernel_coordinates_section_invariant": inv,
        "CEM_reading": {
            "hbar_in_CEM": cem["h"] / (2 * math.pi), "1/alpha": 1 / kern["alpha"],
            "statement": "with c = e = m_e = k_e = 1 the action quantum hbar equals 1/alpha: the one measured electromagnetic stone surfaces as the size of the quantum",
            "G_in_CEM": cem["G"], "G_meaning": "ratio of gravitational to electrostatic force between two electrons",
            "H0_in_CEM": cem["H0"], "H0_meaning": "H0 * r_e / c (classical electron radius over Hubble length)",
            "large_number_fiber": {"1/G_CEM": 1 / cem["G"], "1/H0_CEM": 1 / cem["H0"],
                                   "status": "numeral coincidence class (Dirac); retained as evaluation fiber, no map declared"}},
        "riverbed_CeM": stones(),
        "network": node_analysis(),
        "section_invariance_of_loops": section_invariance(),
    }
    json.dump(out, sys.stdout, indent=1, default=str); print()

if __name__ == "__main__":
    main()
