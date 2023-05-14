#intersection of arr

def intersection(arr1,arr2):
    arr=arr1+arr2
    d={}
    for i in range(len(arr)):
        d[arr[i]]=1
    print(len(d.keys()))


if __name__=="__main__":
    arr1=[10,10,11]
    arr2=[10,10,10]

    intersection(arr1,arr2)

