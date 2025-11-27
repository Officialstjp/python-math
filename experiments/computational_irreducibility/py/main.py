import zlib

def rule30_step(current_row):
    """
    Generates the next row based on Rule 30.
    Row is a list of integers (0 or 1).
    Assumes infinite 0s on boundaries, so we pad the current row.
    """
    # Pad the row with 0s on either side for the calculation
    padded = [0, 0] + current_row + [0, 0]
    next_row = []
    
    # Iterate through the padded row to generate the next state
    for i in range(1, len(padded) - 1):
        # Get the triplet: Left, Center, Right
        left = padded[i-1]
        center = padded[i]
        right = padded[i+1]
        
        # Apply Rule 30 logic
        idx = (left << 2) | (center << 1) | right
        val = (30 >> idx) & 1
        next_row.append(val)
        
    return next_row

def run_simulation(steps):

    # Step 0: A single black cell (1) in a sea of white (0)
    row = [1]
    center_column = [1]
    
    print(f"Step 0: {row} (Center: 1)")
    
    xy_size = steps * 2 + 1  # Enough to hold the growth
    
    for t in range(1, steps + 1):
        grid_offset = steps - t  # offset from edge of grid to current steps row start
        row = rule30_step(row)
        
        # Extract center element
        # The row grows by 2 elements each step (1 left, 1 right)
        center_index = len(row) // 2
        center_val = row[center_index]
        center_column.append(center_val)
        
        # Formatting for visualization
        display_row = " " * grid_offset + "".join(["\u25A0" if x else " " for x in row])
        print(f"Step {t}: {display_row} (Center: {center_val})")
        
    return center_column

def fast_rule30_simulation(steps):
    """
    Runs Rule 30 for a large number of steps and collects the center column.
    Optimized to not store every full row in history, only the current one.
    """
    # Start: Single black cell
    current_row = [1]
    center_column = [1]
    
    for t in range(steps):
        # Pad: 0 0 [ROW] 0 0
        # We only need to read; we construct the next_row fresh.
        padded = [0, 0] + current_row + [0, 0]
        next_row = []
        
        # Rule 30 Bitwise Logic:
        # (Left, Center, Right) -> New Center
        # 000->0, 001->1, 010->1, 011->1, 100->1, 101->0, 110->0, 111->0
        # Lookup table for speed: index = 4*L + 2*C + 1*R
        # [0, 1, 1, 1, 1, 0, 0, 0]
        rule_map = [0, 1, 1, 1, 1, 0, 0, 0]
        
        length = len(padded)
        for i in range(1, length - 1):
            l = padded[i-1]
            c = padded[i]
            r = padded[i+1]
            idx = (l << 2) | (c << 1) | r
            next_row.append(rule_map[idx])
            
        current_row = next_row
        
        # Capture Center
        center_val = current_row[len(current_row) // 2]
        center_column.append(center_val)
        
        # Progress marker for user sanity
        if t % 10000 == 0 and t > 0:
            print(f"Processed {t} steps...")

    return center_column

# 1. GENERATE DATA
print("Running simulation for 32937 steps...")
data = fast_rule30_simulation(32937)
print("Simulation complete.")

# 2. ANALYZE DATA

# A. Bias Test
total = len(data)
ones = sum(data)
zeros = total - ones
ratio = ones / total

print(f"\n--- TEST 1: BIAS CHECK ---")
print(f"Total Steps: {total}")
print(f"Black Cells (1): {ones}")
print(f"White Cells (0): {zeros}")
print(f"Ratio of 1s: {ratio:.5f} (Target for random: 0.5)")

print(f"\n--- TEST 2: COMPRESSION MOVED! ---")

# C. Streak Test
max_streak_1 = 0
max_streak_0 = 0
current_streak = 0
current_val = -1

for val in data:
    if val == current_val:
        current_streak += 1
    else:
        # Check if the streak that just ended was a record
        if current_val == 1:
            max_streak_1 = max(max_streak_1, current_streak)
        else:
            max_streak_0 = max(max_streak_0, current_streak)
        
        current_streak = 1
        current_val = val

print(f"\n--- TEST 3: STREAK CHECK ---")
print(f"Longest run of consecutive 1s: {max_streak_1}")
print(f"Longest run of consecutive 0s: {max_streak_0}")
