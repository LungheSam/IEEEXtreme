from collections import defaultdict

def max_shoe_pairs(N, shoes):
    # Use defaultdict to automatically initialize counts to 0
    shoe_counts = defaultdict(lambda: {'L': 0, 'R': 0})
    
    # Count the number of left and right shoes for each size
    for size, side in shoes:
        shoe_counts[size][side] += 1
    
    # Calculate the total number of pairs
    total_pairs = sum(min(counts['L'], counts['R']) for counts in shoe_counts.values())
    
    return total_pairs

# Read input
N = int(input())
shoes = []
for _ in range(N):
    size, side = input().split()
    shoes.append((int(size), side))

# Calculate and print the result
result = max_shoe_pairs(N, shoes)
print(result)