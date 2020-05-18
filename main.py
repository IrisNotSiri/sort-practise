#bubble sort

def bubble_sort(num):
  if num is None:
    return None
  else:
    for n in range(len(num)-1):
      for n in range(len(num)-1):
        if num[n] > num[n+1]:
          y = num[n]
          num[n] = num[n+1]
          num[n+1] = y
    return num


def insertion_sort(num):
  if num is None:
    return None
  else:
    for i in range(1, len(num)):
      key = num[i]
      j = i-1
      while j >= 0 and key < num[j]:
        num[j+1] = num[j]
        j = j-1
      num[j+1] = key
  return num

def selection_sort(num):
  if num is None:
    return None
  else:
    for i in range(len(num)):
      ind_min = i
      for j in range((i+1),len(num)):
        if num[i] > num[j]:
          ind_min = j
      num[i], num[ind_min] = num[ind_min],num[i]
  return num
  



num = [9,8,7,6,5,4,3,2,1]
y = selection_sort(num)
print (y)


    





