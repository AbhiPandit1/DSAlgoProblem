

def kadaneAlgo(arr):
    sum=0
    maxSum=-2
    i=0
    for i in range(len(arr)-1):
        sum=sum+arr[i]
        if sum<0:
            sum=0
        else:
            maxSum=sum

    return maxSum
            
            


if __name__=='__main__':
    arr=[-1,-2,-3,4,5,-2,-3]
    kadaneAlgo(arr)

