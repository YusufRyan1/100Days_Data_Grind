# 1.Convert a list → set.
nums = [1,2,3,4,5,4]
nums=set(nums)

# 2.Add an element.
nums.add(6)
print(nums)

# 3.Remove an element.
nums.remove(4)
print(nums)

# 4.Check membership.
print(2 in nums)

# 5.Union of two sets.
chars={'a','b','c'}
merged=nums.union(chars)
print(merged)

# 6.Intersection of two sets.
nums2={1,3,5,7,9}
print(nums.intersection(nums2))

# 7.Difference of two sets.
print(nums.difference(nums2))

# 8.Symmetric difference.
print(nums.symmetric_difference(nums2))

# 9.Find unique words in a sentence.
sentence="Hi Today i went to school , Hi Today i went to hospital"
words=set(sentence.split())
print(words)

# 10.Check if two sets are disjoint.
nums3={7,9}
set3=nums.intersection(nums3)
if len(set3)==0:
    print("disJoint")
else:
    print("Joint")
