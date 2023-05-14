
def ispalindromic(a):
    i=0
    j=len(arr)-1

    if len(a)<=1 :
        print(True)
    
    else:
    

        while i<len(arr)-1 and i<j:
        
            if a[i]==a[j]:
               j=j-1
               i=i+1
               print(True)
               print(a)
            else:
              print(False)
              break
        print(a)
                
    

def subArray(arr):
    length=0

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            arr2=arr[i:j]
            print(arr2)
            if ispalindromic(arr2):
                print(arr2)
            else:
                break

           
           
            
          
   


if __name__=='__main__':
    arr=[1,1,2,1,1]
    ispalindromic(arr)
   
    
    
