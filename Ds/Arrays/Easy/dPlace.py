

"""
def dic(arr):
    d={}
    for i in range(len(arr)-1):
        d[arr[i]]=i
        print(d.keys())
    return d

"""
def dleft(arr,d):
    for p in range(d):
        n=len(arr)-1
        temp=arr[n]
   
        for i in range(n,0,-1):
            arr[i]=arr[i-1]
            print(arr)
       
        arr[0]=temp
    print(arr)

    
    
  

    
    
    
        

if __name__=='__main__':
    arr=[1,2,3,4,5]
    #[3,4,5,1,2]
    dleft(arr,6)




   