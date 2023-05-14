
def selection(arr):
    n=len(arr)
    

    for i in range(0,n-1):


        min_index=i  

        for j in range(i,n): 
            if arr[j]<arr[min_index]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index],arr[i]
        
    return arr
       


if __name__ =='__main__':
    a=[9,98,93,94,108,109]

    selection(a)
    print(a)