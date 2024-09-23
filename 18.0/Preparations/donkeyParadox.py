def count_starvation_cells(N, M, haystack1, haystack2):
    (x1, y1) = haystack1
    (x2, y2) = haystack2
    starvation_count = 0
    
    for i in range(N):
        for j in range(M):
            # Skip if the cell is one of the haystacks
            if ((i, j) == (x1, y1)) or ((i, j) == (x2, y2)):
                continue
            
            # Calculate distances to both haystacks
            dist1 = abs(i - x1) + abs(j - y1)
            dist2 = abs(i - x2) + abs(j - y2)
            
            # Check if distances are equal
            if dist1 == dist2:
                starvation_count += 1
    
    return starvation_count

# Input reading
N, M = map(int, input().strip().split())
haystack1 = tuple(map(int, input().strip().split()))
haystack2 = tuple(map(int, input().strip().split()))

# Output the result
print(count_starvation_cells(N, M, haystack1, haystack2))
