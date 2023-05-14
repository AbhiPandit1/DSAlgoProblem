


def sLargest(arr):
    largest=arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]>largest:
            largest=arr[i]
        
    return largest

    

def secondLargest(arr):
    l=-9999999999999999999999

    for i in range(0,len(arr)-1):
        if arr[i]>l and arr[i]!=sLargest(arr):
           l=arr[i]
    return l

def optimalSoln(arr):
    largest=arr[0]
    sLargest=-1
    for i in range(1,len(arr)-1):
        if arr[i]>largest:
            sLargest=largest
            largest=arr[i]

    return sLargest
if __name__=='__main__':
    arr=[3,4,3,2,5,6,7,8,-4,9,8,7,2]
    print(sLargest(arr))
    print(secondLargest(arr))
    print(optimalSoln(arr))


            


