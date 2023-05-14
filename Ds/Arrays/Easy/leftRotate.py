

def leftRotate(arr,d):
    arr1=arr[:d]
    print(arr1)
    arr2=arr[d:]
    arr=arr2+arr1

    print(arr)











if __name__=='__main__':
    arr=[2,3,4,5,6,4,3]
    leftRotate(arr,3)
