arr=[1,2,2,3,4,5]
"""
n=len(arr)
a=[]

def sum(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)+1):
        a=arr[i:j]
        x=sum(a)
        res=0
        if x==5:
            print(x)
            
            
        res=res+1
        print(res)
            
    """      
    

        
            
            

        

        
        

        