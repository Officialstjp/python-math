# Results of simple tests:

**The Bias Test:**
Is the ratio of black (1) to white (0) cells 50/50? If it's significantly skewed (e.g., 60% black), we can create a probabilistic shortcut.

**The Compression Test (Kolmogorov Complexity):**
Hypothesis: If the sequence shrinks significantly (e.g., by 50%), it means there is repeating logic.

Wolfram's claim: It should be incompressible (random).


**The Streak Test:**
What is the longest run of consecutive 1s or 0s? Real randomness rarely has massive streaks; simple patterns often do

## Environment
Python 3.11.9 venv, Windows 11 24h2

## Results:

Run 1: 

```
Running simulation for 50,000 steps...
Processed 10000 steps...
Processed 20000 steps...
Processed 30000 steps...
Processed 40000 steps...
Simulation complete.

--- TEST 1: BIAS CHECK ---
Total Steps: 50001
Black Cells (1): 25096
White Cells (0): 24905
Ratio of 1s: 0.50191 (Target for random: 0.5)

--- TEST 2: COMPRESSION CHECK ---
Original Size: 50001 bytes
Compressed Size: 8030 bytes
Compression Ratio: 0.1606
(Values > 1.0 mean 'uncompressable' overhead. Values < 1.0 mean pattern found.)

--- TEST 3: STREAK CHECK ---
Longest run of consecutive 1s: 21
Longest run of consecutive 0s: 19
```

Actual Run:

```
Generating Rule 30 for 50000 steps...
Generating Control Data (Random) for 50000 steps...

--- PACKING & COMPRESSION ANALYSIS ---

DATASET: Rule 30 Center
  Raw Bits:        50001
  Packed Size:     6251 bytes (True size)
  Compressed Size: 6262 bytes
  Compression Ratio: 1.0018
  -> VERDICT: Incompressible (High Entropy/Random-like)

DATASET: Control (Random)
  Raw Bits:        50001
  Packed Size:     6251 bytes (True size)
  Compressed Size: 6262 bytes
  Compression Ratio: 1.0018
  -> VERDICT: Incompressible (High Entropy/Random-like)
```

Incompressible per simple methods.



Cryptohraphic complexity and visual tests:
```
1. Generating 40,000 steps for Visual Inspection...
2. Running Berlekamp-Massey (Algebraic Attack) on first 2,000 steps...

--- ALGEBRAIC RESULTS ---
Sequence Length: 2000
Linear Complexity (L): 1000
Verdict: Indistinguishable from Random
(Note: For a truly random sequence, L should be close to N/2)
```

