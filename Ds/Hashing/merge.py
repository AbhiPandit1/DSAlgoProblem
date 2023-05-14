nums2=[1,2,3,4,1]
nums1=[1,2,3,4]

nums=[]
i=0
j=0
m=len(nums1)
n=len(nums2)
while i<m and j<n:
    if nums1[i]==nums2[j]:
        print(nums1[i],nums2[j])
        nums.append(nums1[i])
        i+=1
        j+=1
print(nums)
        

        
