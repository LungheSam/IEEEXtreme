def count_3_divisible_pairs(N, arr):
    # Counters for numbers based on their modulo 3 value
    mod_0 = mod_1 = mod_2 = 0
    
    # Count how many numbers fall into each mod group (0, 1, 2)
    for num in arr:
        if num % 3 == 0:
            mod_0 += 1
        elif num % 3 == 1:
            mod_1 += 1
        else:
            mod_2 += 1
    
    # Calculate the number of valid pairs:
    
    # 1. Pairs within mod_0 (choose 2 from mod_0)
    pairs_mod_0 = mod_0 * (mod_0 - 1) // 2
    
    # 2. Pairs between mod_1 and mod_2
    pairs_mod_1_2 = mod_1 * mod_2
    
    # Total pairs
    total_pairs = pairs_mod_0 + pairs_mod_1_2
    
    return total_pairs

# Input reading
N = int(input())  # Number of elements
arr = list(map(int, input().split()))  # Array of elements

# Output the result
print(count_3_divisible_pairs(N, arr))

