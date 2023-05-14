
""""
def twoSum(nums, target):
        
        n=len(nums)
        for i in range(0,n):
            
            for j in (i+1,n):
                sum== nums[i]+nums[j]
                if sum==target:
                    return[i,j]
        
"""

def oSoln(arr,target):
    d={}

    for i in arr:
        complement=target - i
        if complement in d:
            print(d[complement],i)
        else:
            d[i]=1
       
        

if __name__ =='__main__':
    arr=[2,3,4,5,6]

    oSoln(arr,5)