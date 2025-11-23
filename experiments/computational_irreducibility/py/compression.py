import zlib
import random

def rule30_step(current_row):
    # Optimized list-based Rule 30 step
    padded = [0, 0] + current_row + [0, 0]
    next_row = []
    rule_map = [0, 1, 1, 1, 1, 0, 0, 0] # 000->0 ... 111->0
    
    for i in range(1, len(padded) - 1):
        idx = (padded[i-1] << 2) | (padded[i] << 1) | padded[i+1]
        next_row.append(rule_map[idx])
    return next_row

def generate_rule30_center(steps):
    print(f"Generating Rule 30 for {steps} steps...")
    row = [1]
    center_column = [1]
    for _ in range(steps):
        row = rule30_step(row)
        center_column.append(row[len(row) // 2])
    return center_column

def pack_bits_to_bytes(bit_list):
    """
    Converts a list of 0s and 1s (integers) into actual packed bytes.
    [1, 1, 1, 1, 1, 1, 1, 1] -> b'\xff' (255)
    """
    # Convert list of bits to a single large integer
    num = 0
    for bit in bit_list:
        num = (num << 1) | bit
        
    # Convert that integer to bytes
    # (bit_length + 7) // 8 calculates the number of bytes needed
    num_bytes = (len(bit_list) + 7) // 8
    return num.to_bytes(num_bytes, byteorder='big')

def run_comparative_test(steps):
    # 1. Generate Rule 30 Data
    r30_data = generate_rule30_center(steps)
    
    # 2. Generate Control Data (Pure Random)
    print(f"Generating Control Data (Random) for {steps} steps...")
    control_data = [random.randint(0, 1) for _ in range(len(r30_data))]
    
    print("\n--- PACKING & COMPRESSION ANALYSIS ---")
    
    datasets = [
        ("Rule 30 Center", r30_data),
        ("Control (Random)", control_data)
    ]
    
    for name, data in datasets:
        # Pack the bits (The Correction)
        packed_bytes = pack_bits_to_bytes(data)
        
        # Compress
        compressed = zlib.compress(packed_bytes)
        
        # Metrics
        original_len = len(packed_bytes)
        compressed_len = len(compressed)
        ratio = compressed_len / original_len
        
        print(f"\nDATASET: {name}")
        print(f"  Raw Bits:        {len(data)}")
        print(f"  Packed Size:     {original_len} bytes (True size)")
        print(f"  Compressed Size: {compressed_len} bytes")
        print(f"  Compression Ratio: {ratio:.4f}")
        
        if ratio > 1.0:
            print("  -> VERDICT: Incompressible (High Entropy/Random-like)")
        else:
            print(f"  -> VERDICT: Compressible (Pattern Detected: {(1-ratio)*100:.1f}% smaller)")

# Let's run for a significant number of steps to ensure statistical significance
run_comparative_test(50000)