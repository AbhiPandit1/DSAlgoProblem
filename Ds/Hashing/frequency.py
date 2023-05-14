arr=[1,1,2,2,3,4,5,6,7,8,9,9,8,6,9,10,11,12,14,14]

"""
for i in range(len(arr)):
    flag=False
    for j in range(i):
        if arr[i]==arr[j]:#checkin till 0 to i if any no is repested
            flag=True # if repeated mark true
            break
    if flag==True:# if flag true get out of the loop
        continue
    freq=1
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            freq+=1
    print(arr[i],freq)
"""

#Optimise soln
d={}
for i in range(len(arr)):
    if arr[i] in d.keys():
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
print(d.keys())
print(d)


        
           

