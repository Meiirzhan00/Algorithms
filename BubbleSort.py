from typing import List
class SortingAlgorithm:
  def BubbleSort(self, arr: List[int]):
    n=len(arr)
    for i in range(n):
      for j in range(n-i-1):
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[74,56,15,75,81,94,6,7]
print(arr)
p=SortingAlgorithm()
print(p.BubbleSort(arr))
