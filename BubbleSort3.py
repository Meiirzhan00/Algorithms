def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        auysu = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                auysu = True
        if auysu == False: 
            break
arr = [64, 34, 25, 12, 22, 11, 90]  
bubbleSort(arr)
    
for i in range(len(arr)): 
    print(arr[i],end=" ") 

import time
start_time = time.time()
bubbleSort(arr)
print(f"--- {(time.time() - start_time)} seconds ---" )
