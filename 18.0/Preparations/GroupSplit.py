# N=int(input())
# count=0
# for x in range(1,N):
#     y=N-x
#     if y%x==0:
#         count+=1
# print(count)
import math

def count_group_splits(N):
    count = 0
    
    # Loop through all divisors of N
    for x in range(1, int(math.sqrt(N)) + 1):
        if N % x == 0:
            # If x is a divisor of N, check if it's a valid group size (x < N)
            if x < N:
                count += 1
            # Check if (N // x) is also a valid group size, as long as it's distinct from x
            if N // x != x and N // x < N:
                count += 1
    
    return count

# Input
N = int(input())

# Output the result
print(count_group_splits(N))
