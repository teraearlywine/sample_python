"""
Remove elements in the 'nums' list equal to val
"""
val = 3
nums = [3,2,2,3]


pos = 0                     # Initialize the while loop base case
while pos < len(nums):      # Set up iteration (check each element in the list)
    if nums[pos] == val:    # If the nums element position equals value
        nums.pop(pos)       # Pop / remove from list
        continue            # Then continue
    pos += 1                # Iterate on to the next element
