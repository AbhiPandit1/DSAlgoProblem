

def pattern(arr):
    list=[]
    for i in range(0,arr):
      list.append("*"*  i)
    print("\n".join(list))
   


        
        

   
if __name__=='__main__':
    n=5
    pattern(n)



