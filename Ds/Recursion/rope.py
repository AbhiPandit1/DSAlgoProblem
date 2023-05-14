#Ther is a proble of length of rope is given and three no is given a ,b,c in which parts rope can be divided now we have to find no of ways in which rope can be cut
# l=23 a=11,b=12,c=5
#in this there is two ways in which rope can be cut 11,12 or 12,11 there is not other way so we have to return 2
#if not possible print -1


#Idea
#idea is like this we make the first cut a =11 now n=12 now we can do it for other value


def rope(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    res=max(rope(n-a,a,b,b),rope(n-b,a,b,c),rope(n-c,a,b,c))
    if res==0 :
        return 1

    
    if res==-1:
        return -1
    return res+1
n=35
a=11
b=12
c=5
print(rope(n,a,b,c))

 





        