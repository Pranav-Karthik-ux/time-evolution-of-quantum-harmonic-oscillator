[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)
[![NumPy • SciPy • Matplotlib](https://img.shields.io/badge/Uses-NumPy%20•%20SciPy%20•%20Matplotlib-0a7b8c)]

# Quantum Harmonic Oscillator – Exact Time Evolution & Revivals

![Animation preview](quantum_harmonic_oscillator.gif)


![The theory is given here](theory/quantum_harmonic_oscillator_time_evolution.pdf).


**A single-file, zero-dependency (beyond standard libraries) demonstration of exact quantum time evolution in the harmonic oscillator.**

Watch any superposition of energy eigenstates evolve analytically — no numerical integration, no approximations.  
Thanks to equally spaced energy levels, the wave function exhibits **perfect periodic revivals** every **T = 2π/ω**.

### What you’ll see
- Splitting, breathing, interference, and perfect reconstruction of the initial state
- Exact analytic solution using Hermite polynomials
- real + imaginary parts plotted in real time
- Automatically saves a  GIF

## Default initial state (feel free to change!)
```python

ψ(0) ∝ |0⟩ + 3|2⟩ + 7|3⟩
