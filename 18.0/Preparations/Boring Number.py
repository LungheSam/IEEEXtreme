"""
Boring Number
Time limit: 1000 ms
Memory limit: 128 MB

You are given an array 
A
A of 
N
N integers. Find the index 
i
i of an element such that the absolute difference between 
A
i
A 
i
​
  and the arithmetic mean of all the 
N
N integers is minimum. If the solution is not unique, find the smallest index 
i
i.

Standard input
The first line contains a single integer 
N
N.

The second line contains the 
N
N elements of the array 
A
A.

Standard output
Print the answer on the first line.
"""

N=int(input())
array=list(map(int,input().strip().split(" ")))
mean_array=sum(array)/N
# print(f"Mean{mean_array}")
absolute_values=[]
minimum=mean_array
for i in range(len(array)):
    absolute=abs(array[i]-mean_array)
    # print(f"Element {array[i]}:absolute {absolute}")
    absolute_values.append(absolute)
    if min(absolute_values)< minimum:
        minimum=min(absolute_values)
        index=i

print(index+1)