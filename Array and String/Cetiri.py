nums = list(map(int, input().split()))
nums.sort()

if (nums[2] - nums[1] == nums[1] - nums[0]):
    print(nums[2] + (nums[2] - nums[1]))
elif (nums[2] - nums[1] > nums[1] - nums[0]):
    diff = nums[1] - nums[0]
    print(nums[1] + diff)
#1 6 8
elif (nums[2] - nums[1] < nums[1] - nums[0]):
    diff = nums[2] - nums[1]
    print(nums[0] + diff)
