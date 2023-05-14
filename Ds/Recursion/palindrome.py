def Palindrome(arr,l,r):
    
    n=len(arr)
    if arr==" ":
        return True
    if arr[0]==arr[n-1]:
        return Palindrome(arr,l+1,r-1)
        
    else: False
if __name__=="__main__":
    arr="racecar"
    Palindrome(arr,0,len(arr)-1)