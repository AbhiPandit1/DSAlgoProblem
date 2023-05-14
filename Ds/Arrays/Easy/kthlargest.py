
def findKthLargest(nums, k):
        sort(nums)
        nums[k-1]
        
    

def sort(arr):
    i=0
    j=len(arr)-1
    while i<len(arr) and i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr


if __name__=='__main__':
    arr=[3,4,3,2,5,6,7,8,4,9,8,7,2]
    print(findKthLargest(arr,2))



