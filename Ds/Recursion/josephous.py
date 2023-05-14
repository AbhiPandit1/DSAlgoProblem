#josephous Problem



def josh(n,k):
    if n==1:
        return 0
    return josh(n-1,(k-1)%n)


n=[1,2,3,4,5]
josh(n,2)



