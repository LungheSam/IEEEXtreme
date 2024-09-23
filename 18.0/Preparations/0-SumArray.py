
# n=int(input().strip())
# array=list(map(int,input().strip().split(" ")))
# initArray=array.copy()
# # print(array)
# index=-1
# for i in range(len(array)):
#     array[i]=array[i]*(-1)
#     # print(array[i])
#     s=sum(array)
#     # print(f"Sum={s}")
#     if s==0:
#         index=i+1
#         break
#     else:
#         array=initArray
#         # print(array)
# if index==-1:
#     print(-1)
# else:
#     print(index)
        
def find_index(arr):
    """Finds the smallest index of an element in an array such that if you multiply it by -1, the sum of the whole array becomes 0.

    Args:
        arr: The input array.

    Returns:
        The smallest index of the element, or -1 if there is no solution.
    """

    n = len(arr)
    total_sum = sum(arr)

    for i in range(n):
        if total_sum - 2 * arr[i] == 0:
            return i+1

    return -1


N = int(input())
arr = list(map(int, input().split()))

index = find_index(arr)
print(index)