import matplotlib.pyplot as plt
import numpy as np

# --- 1. GENERATOR ---
def rule30_step(current_row):
    padded = [0, 0] + current_row + [0, 0]
    next_row = []
    rule_map = [0, 1, 1, 1, 1, 0, 0, 0]
    for i in range(1, len(padded) - 1):
        idx = (padded[i-1] << 2) | (padded[i] << 1) | padded[i+1]
        next_row.append(rule_map[idx])
    return next_row

def get_center_sequence(steps):
    row = [1]
    center_seq = [1]
    for _ in range(steps):
        row = rule30_step(row)
        center_seq.append(row[len(row) // 2])
    return center_seq

# --- 2. ALGEBRAIC PROBE (Berlekamp-Massey) ---
def berlekamp_massey(sequence):
    """
    Calculates the linear complexity of a binary sequence.
    Returns the length of the shortest LFSR that can generate the sequence.
    """
    N = len(sequence)
    b = [1]  # Copy of last C
    c = [1]  # Connection polynomial
    L = 0    # Linear complexity
    m = -1   # Last position where L changed
    
    for n in range(N):
        # Calculate discrepancy
        d = 0
        for i in range(L + 1):
            d ^= c[i] & sequence[n - i]
        
        if d == 1:
            t = [0] * (n - m) + b
            # c(x) = c(x) + x^(n-m) * b(x)
            # XOR addition of polynomials
            temp_c = c[:] # copy
            if len(t) > len(c):
                c += [0] * (len(t) - len(c))
            for i in range(len(t)):
                c[i] ^= t[i]
                
            if L <= n / 2:
                L = n + 1 - L
                m = n
                b = temp_c
                
    return L

# --- EXECUTION ---
print("1. Generating 40,000 steps for Visual Inspection...")
# We generate enough to make a nice 200x200 square image (40,000 bits)
full_seq = get_center_sequence(40000)

print("2. Running Berlekamp-Massey (Algebraic Attack) on first 2,000 steps...")
# BM is O(N^2), so we use a smaller sample for the script to run fast
sample_size = 2000
sample_seq = full_seq[:sample_size]
l_complexity = berlekamp_massey(sample_seq)

print(f"\n--- ALGEBRAIC RESULTS ---")
print(f"Sequence Length: {sample_size}")
print(f"Linear Complexity (L): {l_complexity}")
print(f"Verdict: {'Pattern Found!' if l_complexity < sample_size/2 - 10 else 'Indistinguishable from Random'}")
print("(Note: For a truly random sequence, L should be close to N/2)")

# --- 3. VISUALIZATION ---
# Reshape into a 200x200 grid
grid_size = 200
# Ensure we have exactly grid_size^2 elements
visual_data = np.array(full_seq[:grid_size**2]).reshape((grid_size, grid_size))

plt.figure(figsize=(10, 10))
plt.imshow(visual_data, cmap='binary', interpolation='nearest')
plt.title("Visual Artifact Scan: Rule 30 Center Column (200x200 Grid)")
plt.axis('off')
plt.savefig('rule30_visual_scan.png', dpi=150, bbox_inches='tight')