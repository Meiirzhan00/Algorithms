class SortAlgotithm:
  def BubbleSort(self):
    n=input("Enter are digits: ").split(' ')
    for i in range(len(n)-1):
      for j in range(len(n)-1):
        if n[j]>n[j+1]:
          n[j],n[j+1]=n[j+1],n[j]
    
    for s in n:
      print(s,end=' ')

p=SortAlgotithm()
p.BubbleSort()
