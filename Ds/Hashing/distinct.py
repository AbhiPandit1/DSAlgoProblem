arr=[1,1,2,3,4,5,2,3,1]
freq={}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
print(freq)
print(len(freq.keys()))