"""
def frequencyNaive(arr):
    n=len(arr)
    for i in range (n):#2,3,4,5,2,4,5,5
        flag=False
        
        
        for j in range (i):
            if arr[i]==arr[j]:
                print(arr[i],arr[j])
                flag=True
                break
        if flag==True:
           continue
        
        
        freq=1
       

        for j in range(i+1,n):
            if arr[i]==arr[j]:
                print(arr[i],freq)
                freq+=1
"""


def frequencyOptimise(arr):
    n=len(arr)
    d=dict()
    for i in range(n):
        if arr[i] in d.keys():
           
           d[arr[i]]+=1
        else:
           
            d[arr[i]]=1
   
    print(d)


if __name__=='__main__':

    arr=[2,3,4,5,2,4,5,5]#[2:2],[3:1],[4:2],[5:3]

    frequencyOptimise(arr)

