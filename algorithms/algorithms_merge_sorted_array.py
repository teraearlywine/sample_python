"""
Merge sorted arrays using a two pointer approach 
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
"""

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]


arr1 = zip(arr1, arr2)             # Zip returns tuples, and handles the m constraint
arr1 = list(map(list, arr1))       # Convert tuples into a list of lists using map
arr1 = sum(arr1, [])               # Stack overflow solution: sum nested list -> [1,2] + [3,4] just joins it
arr1 = sorted(arr1)
print(arr1)
