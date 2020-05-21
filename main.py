#bubble sort

def bubble_sort(nums):
    if nums is None:
      return None
    for n in range(len(nums)-1):
      for n in range(len(nums)-1):
        if nums[n] > nums[n+1]:
          nums[n], nums[n+1] = nums[n+1], nums[n]
    return nums



def insertion_sort(nums):
    if nums is None:
      return None
    for i in range(1, len(nums)):
      key = nums[i]
      j = i-1
      while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
      nums[j+1] = key
    return nums
      





def selection_sort(nums):
    if nums is None:
      return None
    for i in range(len(nums)):
      min_index = i
      for j in range(i+1, len(nums)):
        if nums[min_index] > nums[j]:
          min_index = j
      nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
    
        
def merge_sort(nums): 
    if nums is None:
      return None
    
    if len(nums) > 1:
      mid = len(nums)//2
      left = nums[:mid]
      right = nums[mid:]
      #split list into two half with recursion
      merge_sort(left)
      merge_sort(right)
      # merge left and right half
      i = j = k = 0
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          nums[k] = left[i]
          i += 1
        else:
          nums[k] = right[j]
          j += 1
        k += 1
      # check and add the remaining number in the left or right list
      while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
      while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return

    





def quick_sort(nums,low,high):
    if nums is None:
      return None
    if low < high:
      i = low - 1
      pivot = nums[high]
      for j in range(low, high):
        if nums[j] < pivot:
           i += 1
           nums[i], nums[j] = nums[j], nums[i]
      nums[i+1], nums[high] = nums[high], nums[i+1]
      n = i+1
      quick_sort(nums,low,n-1)
      quick_sort(nums,n+1,high)
    return




nums = [9,8,7,5,4,3,6,2,1]
# low = 0
# high = len(nums)-1
merge_sort(nums)

print (nums)
t=[3,4,5]


    





