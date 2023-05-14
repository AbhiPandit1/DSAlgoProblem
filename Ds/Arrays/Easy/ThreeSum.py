
"""
def threeSum(arr,target):
    s=set()
    x=[]
    
    
    for i in range(0,len(arr)-1):
        
            for j in range(i+1,len(arr)-1):
                
                    for k in range(j+1,len(arr)-1):
                        if(arr[i]+arr[j]+arr[k]==target):
                            temp={arr[i],arr[j],arr[k]}
                            
                            

    s.update(temp) 
    print(s) 
    x=list[s]
    print(x)
"""
def betterSoln(arr):
    d=set()
    for i in range(len(arr)):
        d.clear()
       
        for j in range(i+1,len(arr)):
            if -(arr[i]+arr[j]) in d:
                
               
                temp1={arr[i],arr[j],-(arr[i]+arr[j])}
                
                print(temp1)
               
               
            else:
                temp=[arr[j]]
                temp.sort()
                d.update(temp)
                


                
                
        
        
                
                    
if __name__=='__main__':
    arr=[1,-2,3,4,5,6,7,8,9,4,0,2,3,4]
    betterSoln(arr)

