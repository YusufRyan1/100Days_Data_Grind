# 1.Create a tuple of 5 items.
nums=(1,2,3,4,5)

# 2.Access index 2.
print(nums[2])

# 3.Try modifying an element (expect error).
nums[2]=4

# 4.Convert tuple → list → tuple.
print(type(nums))
nums=list(nums)
print(type(nums))
nums=tuple(nums)
print(type(nums))

# 5.Tuple unpacking:
first,second,third,fourth,fifth=nums
print(first,second,third,fourth,fifth)

# 6.Loop through a tuple.
for num in nums :
    print(num)

# 7.Check if an element exists.
print(2 in nums)

# 8.Use a tuple as a dictionary key.
locations = {
    (30.0444, 31.2357): "Cairo",
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris"
}