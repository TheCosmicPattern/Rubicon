#!/usr/bin/env python3
"""
THE RUBICON — ISW Prediction Calculator

Computes the specific, falsifiable ISW (Integrated Sachs-Wolfe) signal
modification predicted by the OGSI metric relative to ΛCDM.

This is the prediction that ΛCDM does not make.
If confirmed: the physical interpretation moves from BIN 3 to BIN 2.
If falsified: the OGSI mechanism is ruled out at this λ value.

Run: python3 isw_prediction.py

No dependencies beyond standard Python.
"""

import math
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experiment_results")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===================================================================
# OGSI METRIC
# ===================================================================
# ds² = -A²(σ)c²dt² + a²(t)dx²
# A(σ) = 1 + λσ
# λ ≈ 0.03 (from Pantheon+SH0ES mass step, 3.4σ detection)
# σ = sSFR × m* / ρ_CMB (entropy production density)

LAMBDA_OGSI = 0.03  # From Γ = -0.033 ± 0.010 mag

# Cosmological parameters (Pantheon+ best fit)
OMEGA_M = 0.32
OMEGA_L = 0.68
H0_PLANCK = 67.4   # km/s/Mpc
H0_SHOES = 73.0    # km/s/Mpc

# ===================================================================
# COSMIC STAR FORMATION RATE DENSITY
# ===================================================================
# Madau & Dickinson (2014) parametric fit
# ψ(z) = 0.015 × (1+z)^2.7 / (1 + ((1+z)/2.9)^5.6)
# Units: M_sun / yr / Mpc³

def sfrd(z):
    """Cosmic star formation rate density (Madau & Dickinson 2014)."""
    return 0.015 * (1 + z)**2.7 / (1 + ((1 + z) / 2.9)**5.6)

# σ(z) ∝ SFRD(z) / ρ_CMB(z)
# ρ_CMB ∝ (1+z)^4
# Normalized to σ(z=0) = 1

def sigma_relative(z):
    """Relative entropy production density."""
    return sfrd(z) / (1 + z)**4

SIGMA_0 = sigma_relative(0)

def sigma_normalized(z):
    """σ(z) normalized to today's value."""
    return sigma_relative(z) / SIGMA_0

def A_ogsi(z):
    """OGSI metric lapse function A(σ) = 1 + λσ."""
    return 1 + LAMBDA_OGSI * sigma_normalized(z)

# ===================================================================
# ΛCDM BACKGROUND COSMOLOGY
# ===================================================================

def H_ratio_squared(z):
    """H²(z) / H²(0) in flat ΛCDM."""
    return OMEGA_M * (1 + z)**3 + OMEGA_L

def H(z):
    """Hubble parameter H(z) in km/s/Mpc (using Planck H0)."""
    return H0_PLANCK * math.sqrt(H_ratio_squared(z))

def Omega_Lambda_z(z):
    """Dark energy density fraction at redshift z."""
    return OMEGA_L / H_ratio_squared(z)

def Omega_matter_z(z):
    """Matter density fraction at redshift z."""
    return OMEGA_M * (1 + z)**3 / H_ratio_squared(z)

# ===================================================================
# GROWTH FACTOR (linear perturbation theory)
# ===================================================================
# D(a) ∝ H(a) × ∫₀ᵃ da' / (a'H(a'))³
# Simplified: using the approximation D(z) ≈ Ω_m(z)^0.55 / (1+z)

def growth_factor(z):
    """Linear growth factor D(z), normalized to D(0)=1."""
    # Carroll, Press & Turner (1992) approximation
    om = Omega_matter_z(z)
    ol = Omega_Lambda_z(z)
    D = (5/2) * om / (om**(4/7) - ol + (1 + om/2) * (1 + ol/70))
    D0_om = Omega_matter_z(0)
    D0_ol = Omega_Lambda_z(0)
    D0 = (5/2) * D0_om / (D0_om**(4/7) - D0_ol + (1 + D0_om/2) * (1 + D0_ol/70))
    return D / D0 / (1 + z)

# ===================================================================
# ISW KERNEL
# ===================================================================
# The ISW effect arises from time-varying gravitational potentials:
#   ΔT/T_ISW = -2 ∫ (∂Φ/∂t) / c² dt
#
# In ΛCDM:
#   Φ ∝ D(z) / (1+z) × δ_m
#   The ISW signal ∝ d/dt[D(z)/(1+z)] which is driven by dark energy
#
# In OGSI:
#   Φ_eff = A(σ(z)) × Φ_ΛCDM
#   The ISW signal gets an additional term from dA/dt

def isw_kernel_lcdm(z):
    """
    ΛCDM ISW kernel (unnormalized).
    Proportional to the rate of change of the gravitational potential.
    """
    # dΦ/dt ∝ f(Ω_Λ) × H(z)
    # The ISW effect is strongest during matter→DE transition
    om = Omega_matter_z(z)
    ol = Omega_Lambda_z(z)
    # ISW kernel ∝ (1 - f) × H where f ≈ Ω_m^0.55 is the growth rate
    f_growth = om**0.55
    return (1 - f_growth) * math.sqrt(H_ratio_squared(z)) * growth_factor(z)

def isw_kernel_ogsi(z):
    """
    OGSI ISW kernel with perspective-flipped refractivity.

    The local OGSI modification is A(σ(z)).
    The observer at z=0 reads this through the inverted refractive base
    (looking outward = inverted base = 15/11 per unit z).
    This AMPLIFIES distant signals.
    """
    lcdm_kernel = isw_kernel_lcdm(z)

    # Local enhancement at redshift z
    local_enhancement = A_ogsi(z) - 1  # = λ × σ(z)/σ(0)

    # Perspective-flipped refractivity for outward observation
    # Base: 11/15 (R=4 info-side), inverted for outward: (15/11)^z
    outward_base = 15/11
    refraction_amplification = outward_base ** z

    # The observed enhancement is the local enhancement × amplification
    observed_enhancement = local_enhancement * refraction_amplification

    return lcdm_kernel * (1 + observed_enhancement)

# ===================================================================
# COMPUTE THE PREDICTION
# ===================================================================

def compute_isw_prediction():
    print("=" * 70)
    print("  THE RUBICON — ISW PREDICTION")
    print("  Specific, falsifiable, computed from OGSI metric")
    print("=" * 70)

    # --- σ(z) profile ---
    print("\n--- Cosmic Star Formation & Entropy Production ---\n")
    print(f"{'z':>6} {'SFRD':>10} {'σ(z)/σ(0)':>10} {'A(σ)':>10}")
    print("-" * 40)

    z_values = [0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]
    for z in z_values:
        print(f"{z:>6.1f} {sfrd(z):>10.4f} {sigma_normalized(z):>10.4f} {A_ogsi(z):>10.6f}")

    # --- ISW signal by redshift ---
    print("\n--- ISW Signal: OGSI vs ΛCDM ---\n")
    print(f"{'z':>6} {'ISW_ΛCDM':>10} {'ISW_OGSI':>10} {'Ratio':>10} {'Δ(%)':>8}")
    print("-" * 48)

    for z in [0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 2.5, 3.0]:
        il = isw_kernel_lcdm(z)
        io = isw_kernel_ogsi(z)
        ratio = io / il if il > 0 else 0
        delta = (ratio - 1) * 100
        print(f"{z:>6.1f} {il:>10.6f} {io:>10.6f} {ratio:>10.6f} {delta:>7.2f}%")

    # --- Integrated ISW by redshift bin ---
    print("\n--- Integrated ISW by Redshift Bin ---\n")

    bins = [
        (0.1, 0.5, "Low-z (nearby)"),
        (0.5, 1.0, "Intermediate"),
        (1.0, 1.5, "Pre-cosmic-noon"),
        (1.5, 2.0, "Cosmic noon"),
        (2.0, 3.0, "High-z"),
    ]

    dz = 0.005
    bin_results = []

    print(f"{'Bin':>20} {'ΛCDM':>10} {'OGSI':>10} {'OGSI/ΛCDM':>10} {'Δ(%)':>8}")
    print("-" * 62)

    for z_lo, z_hi, label in bins:
        int_lcdm = 0
        int_ogsi = 0
        z = z_lo
        while z < z_hi:
            int_lcdm += isw_kernel_lcdm(z) * dz
            int_ogsi += isw_kernel_ogsi(z) * dz
            z += dz
        ratio = int_ogsi / int_lcdm if int_lcdm > 0 else 0
        delta = (ratio - 1) * 100
        bin_results.append({
            'z_lo': z_lo, 'z_hi': z_hi, 'label': label,
            'lcdm': int_lcdm, 'ogsi': int_ogsi,
            'ratio': ratio, 'enhancement_pct': delta,
        })
        print(f"  z={z_lo:.1f}-{z_hi:.1f} {label:>12} {int_lcdm:>10.6f} {int_ogsi:>10.6f} {ratio:>10.6f} {delta:>7.2f}%")

    # Total
    total_lcdm = sum(b['lcdm'] for b in bin_results)
    total_ogsi = sum(b['ogsi'] for b in bin_results)
    total_ratio = total_ogsi / total_lcdm if total_lcdm > 0 else 0
    total_delta = (total_ratio - 1) * 100
    print(f"  {'TOTAL':>20} {total_lcdm:>10.6f} {total_ogsi:>10.6f} {total_ratio:>10.6f} {total_delta:>7.2f}%")

    # --- THE PREDICTION ---
    print("\n" + "=" * 70)
    print("  THE SPECIFIC PREDICTION")
    print("=" * 70)

    print(f"""
OGSI predicts the ISW signal is enhanced by {total_delta:.1f}% relative to ΛCDM.

The enhancement profile follows σ(z):
  - Strongest at LOW redshift (z < 0.5): +{bin_results[0]['enhancement_pct']:.2f}%
  - Intermediate (z = 0.5-1.0):          +{bin_results[1]['enhancement_pct']:.2f}%
  - Weakening toward cosmic noon (z > 1): +{bin_results[2]['enhancement_pct']:.2f}%
  - Minimal at high redshift (z > 2):     +{bin_results[4]['enhancement_pct']:.2f}%

ΛCDM predicts NONE of this enhancement.

The QUALITATIVE difference:
  ΛCDM:  ISW kernel peaks at z ≈ 0.5, declines smoothly
  OGSI:  ISW kernel has the same shape PLUS an enhancement that
         DECREASES with redshift (following declining σ(z))

This creates a REDSHIFT-DEPENDENT EXCESS:
  If you measure ISW-galaxy cross-correlation in tomographic bins
  (as current surveys can do), the LOW-z bins should show MORE
  ISW signal than ΛCDM predicts, while HIGH-z bins should agree
  with ΛCDM.

HOW TO TEST:
  1. Use Planck CMB temperature maps
  2. Cross-correlate with galaxy survey catalogs (DESI, SDSS, DES)
  3. Measure ISW amplitude in the 5 redshift bins above
  4. Compare to ΛCDM prediction (no enhancement)
  5. Compare to OGSI prediction (enhancement declining with z)

The data exists. The computation is straightforward.
The prediction is specific: +{bin_results[0]['enhancement_pct']:.1f}% at z < 0.5,
declining to +{bin_results[4]['enhancement_pct']:.1f}% at z > 2.

If confirmed: OGSI moves from BIN 3 (proposed) to BIN 2 (measured).
If falsified: OGSI mechanism is ruled out at λ = {LAMBDA_OGSI}.
""")

    # --- Connection to the refractivity model ---
    print("--- Connection to the Rubicon Structure ---\n")
    print(f"  λ = {LAMBDA_OGSI} = the mass step Γ")
    print(f"  (11/15)^11 = {(11/15)**11:.6f} ≈ Γ = 0.033 (0.05% off)")
    print(f"  The ISW enhancement IS the refractivity made visible:")
    print(f"  At each redshift, A(σ) - 1 = λ × σ(z)/σ(0) is the")
    print(f"  structural refraction at that depth.")
    print()
    print(f"  The prediction is that the RESIDUAL between measured ISW")
    print(f"  and ΛCDM ISW follows the cosmic star formation history")
    print(f"  scaled by λ ≈ 0.03 = (11/15)^11.")
    print()
    print(f"  This connects the mass step (cosmological), the ISW")
    print(f"  (CMB × large-scale structure), and the refractivity model")
    print(f"  (the structure) through a single parameter derived from")
    print(f"  the Pantheon+SH0ES dataset.")

    # Save results
    results = {
        'lambda_ogsi': LAMBDA_OGSI,
        'omega_m': OMEGA_M,
        'omega_l': OMEGA_L,
        'total_enhancement_pct': total_delta,
        'bins': bin_results,
        'prediction': f"ISW enhanced by {total_delta:.1f}% over ΛCDM, declining with z",
        'test_method': "ISW-galaxy cross-correlation tomography (Planck × DESI/SDSS)",
        'falsification': f"If ISW matches ΛCDM within 1% across all bins, OGSI at λ={LAMBDA_OGSI} is falsified",
    }

    with open(os.path.join(OUTPUT_DIR, "isw_prediction.json"), 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {OUTPUT_DIR}/isw_prediction.json")
    return results


if __name__ == "__main__":
    compute_isw_prediction()
