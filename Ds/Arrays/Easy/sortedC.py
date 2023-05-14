
def checkSorted(arr):

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:  
            return False   
        
    
   
    return True





if __name__=='__main__':
    arr=[3,4,3,2,5,6,7,8,-4,9,8,7,2]
    arr2=[1,1,3,4,5,6,7,8]
    arr3=[-1,0,1,2,3,4,5,6,7]
    arr4=[3,4,5,1,2]

    print(checkSorted(arr))
    print(checkSorted(arr2))
    print(checkSorted(arr3))
    print(checkSorted(arr4))
