arr=[3,2,8,15,-8]

for i in range(len(arr)-1):
    for j in range(i,len(arr)):
        if arr[i]+arr[j]==17:
            print(arr[i],arr[j])
d={}
for i in range(len(arr)):
    complement=17-arr[i]
    if complement in d:
        print(complement,d[arr[i]])
    else:
        d[arr[i]]=1
print(d)
            