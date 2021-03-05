from typing import List
class Algorithm:
  def Binary_search(self, list: List[int],item) -> int:
    low=0
    high=len(list)-1
    while low<=high:
      mid=(low+high)//2
      guess=list[mid]
      if guess==item:
        return mid
      elif guess>item:
        high=mid-1
      else:
        low=mid+1
    
    return None

my_list=[1,3,5,7,9]
p=Algorithm()
print(p.Binary_search(my_list,9))

import time
start_time = time.time()
p.Binary_search(my_list,3)
print(f"--- {(time.time() - start_time)} seconds ---" )
