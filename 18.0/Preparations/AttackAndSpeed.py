# InitAttack,InitSpeed,KDollars,XIncreseAttack,YIncreaseSpeed=list(map(int,input().split(" ")))
# # print(XIncreseAttack)

# for k in range(KDollars):
#     # print(f"K={k}")
#     Attack=InitAttack+k*XIncreseAttack
#     Speed=InitSpeed+(KDollars-k)*YIncreaseSpeed
#     # print(f"\nAttack={Attack}\nSpeed={Speed}")
    
#     if Attack==Speed:
#         print(k)
#         break
#     k+=1
# else:
#     print(-1)

def balance_attributes(A, S, K, X, Y):
    # We need to solve: A + i*X = S + (K-i)*Y
    # Rearranging: i*(X+Y) = S - A + K*Y
    # So: i = (S - A + K*Y) / (X+Y)
    
    numerator = S - A + K*Y
    denominator = X + Y
    
    # Check if there's an integer solution
    if numerator % denominator != 0:
        return -1
    
    i = numerator // denominator
    
    # Check if the solution is valid (0 <= i <= K)
    if 0 <= i <= K:
        return i
    else:
        return -1

# Read input
A, S, K, X, Y = map(int, input().split())

# Calculate and print the result
result = balance_attributes(A, S, K, X, Y)
print(result)
