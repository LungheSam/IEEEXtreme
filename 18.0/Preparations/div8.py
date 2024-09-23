import itertools
number=input()
number_list=list(number)
number=int(number)
permuations=list(itertools.permutations(number_list))
permuations=[int("".join(i)) for i in permuations if (int("".join(i))<number) and (int("".join(i))%8==0) and (i[0] !='0')]

if permuations==[]:
    if number%8==0:
        print(number)
    else:
        print(-1)
else:
    print(min(permuations))




    

    
