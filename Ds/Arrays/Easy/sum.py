def twosum(arr,target):
    s={}

    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in s:

            print(arr[i],complement)
           
        else:
            s[arr[i]]=i
        
        
if __name__=='__main__':
    arr=[1,2,3,4,5,3,6]

    twosum(arr,9)

