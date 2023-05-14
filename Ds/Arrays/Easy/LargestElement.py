



def largestElementN(arr):
    arr.sort()
    return arr[len(arr)-1]
    
    
def largestElementO(arr1):


    largest=arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

if __name__=='__main__':
    arr=[3,4,3,2,5,6,7,8,4,9,8,7,2]
    print(largestElementO(arr))

