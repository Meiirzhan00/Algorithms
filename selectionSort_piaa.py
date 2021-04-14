def kishiSandyTabu(arr):
   kishiSan=arr[0]
   kishiSan_index=0

   for i in range(1,len(arr)):
     if arr[i] < kishiSan:
       kishiSan=arr[i]
       kishiSan_index=i
   return kishiSan_index

def selectionSort(arr):
  newArr=[]

  for i in range(len(arr)):
    kishiSan = kishiSandyTabu(arr)
    newArr.append(arr.pop(kishiSan))

  return newArr

p=selectionSort([5,3,6,2,10])
print(f"\n\n\nБастапқы массив :  [5, 3, 6, 2, 10]")
print(f"Сортталған массив: {p}\n\n\n")
