

def twoSum(arr,target):
    d={}
    for i in range(0,len(arr)):
        complement=target-arr[i]
        if complement in d:
            print(d)
            return complement,arr[i]
        else:
            d[arr[i]]=i
    
                    
       

if __name__=='__main__':
    arr=[1,2,3,4,5,6,7,8]

    print(twoSum(arr,15))