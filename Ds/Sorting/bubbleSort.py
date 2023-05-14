#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Sorting algorithm

#Bubble sort



def bubbleSort(arr):
    n=len(arr)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range (0,n):
            if arr[i]>arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
                
    
    return arr        
arr=[2,17,4,1,4,7,9]
bubbleSort(arr);

for i in range(len(arr)):
    print(arr[i], end=" ")








    
    
    
    