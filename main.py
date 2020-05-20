#bubble sort

def bubble_sort(num):
    if num is None:
      return None
  
    for n in range(len(num)-1):
      for n in range(len(num)-1):
        if num[n] > num[n+1]:
          num[n], num[n+1] = num[n+1], num[n]
    return num



def insertion_sort(num):
    if num is None:
      return None
    for n in range(1, len(num)):
      key = num[n]
      m = n-1
      while m >=0 and key < num[m]:
        num[m+1] = num[m]
        m -= 1
      num[m+1] = key
    return num



def selection_sort(num):
    if num is None:
      return None
    for n in range(len(num)):
      min_key = n
      for m in range(n+1, len(num)):
        if num[min_key] > num[m]:
          min_key = m
      num[n], num[min_key] = num[min_key], num[n]
    return num
        
def merge_sort(num): 
    if num is None:
      return None
    if len(num) > 1:
      mid = len(num)//2
      left = num[:mid]
      right = num[mid:]
      # split list first
      merge_sort(left)
      merge_sort(right)
      # then merge
      i = j = k = 0
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          num[k] = left[i]
          i += 1
        else:
          num[k] = right[j]
          j += 1
        k += 1
      while i < len(left):
        num[k] = left[i]
        i += 1
        k += 1
      while j < len(right):
        num[k] = right[j]
        j += 1
        k += 1 
    return num




def quick_sort(num,low,high):
    if num is None:
      return None
    i = (low-1)
    pivot = num(high)
    for j in range(low, high):
      if num[j] < pivot:
        i += 1
        num[i], num[j] = num[j], num[i]
    num[i+1],num[j] = num[j], num[n+1]
    pivot_index = i+1

    quick_sort(num,low, pivot_index-1)
    quick_sort(num, pivot_index+1, high)
    return num



num = [9,8,7,5,4,3,6,2,1]
y = merge_sort(num)
print (y)
t=[3,4,5]


    





