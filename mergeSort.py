def mergeSort(arr):
    if len(arr) > 1:
        ortasy = len(arr)//2
        L = arr[:ortasy]
        R = arr[ortasy:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
if __name__ == '__main__':
    arr = [7,18,59,4,20,45,3,14]
    print("Бастапқы массив :   ", end='')
    printList(arr)

    mergeSort(arr)
    print("Сортталған массив : ", end='')
    printList(arr)
 
import time
start_time = time.time()
mergeSort(arr)
print()
print(f"--- {(time.time() - start_time)} seconds ---" )
