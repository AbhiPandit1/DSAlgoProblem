
"""
def nonZeroNaive(arr):
    c=0
    c1=0
    temp=[]
    temp2=[]

    for i in range(len(arr)):

        if arr[i]<1:
            c+=1
            temp2.append(arr[i])
            print(temp2)

        else:
            c1+=1
            temp.append(arr[i])
           
    print(c1,c)
     
    temp1=temp+temp2
    print(temp1)



"""
def nonZeroOptimal(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            j=i
            break
    print(j)
    
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j=j+1
            print(arr)
        
    print(arr)



  

if __name__=='__main__':


    arr=[2,0,3,4,0,5,4,0,4,3,0,3,0,2,3,0]
    nonZeroOptimal(arr)
