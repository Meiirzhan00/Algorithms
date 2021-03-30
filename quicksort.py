def quicksort(arr):

  if len(arr) < 2:
    return arr

  else:
    ozek = arr[0]
    az = [i for i in arr[1:] if i < ozek]

    ulken = [i for i in arr[1:] if i > ozek]

    return quicksort(az) + [ozek] + quicksort(ulken)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [91,15,4,74,31,3,45,7,9,11]
    print("Бастапқы массив :   ", end='')
    printList(arr)

    p = quicksort(arr)
    print("Сортталған массив : ", end='')
    printList(p)
