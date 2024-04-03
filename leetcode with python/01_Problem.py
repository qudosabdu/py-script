def sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        if target -nums[i] in seen:
            return [seen[target-nums[i]], i]
        seen[nums[i]] = i
        print(seen)
    return []


# print(sum([2,7,11,15], 9)) # [0, 1]
print(sum([3,2,4], 6)) # [1, 2]