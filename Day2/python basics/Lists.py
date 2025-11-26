# 1.Create a list of 5 numbers and print the sum.
nums=[2,3,4,1,5]
print(sum(nums))

# 2.Remove duplicates from a list.
nums=[2,3,4,4,5]
duplicates_removed_nums=set(nums)
print(duplicates_removed_nums)

# 3.Reverse a list without using .reverse() (try slicing).
nums=[1,2,3,4,5]
i=len(nums)-1
reversed_nums=[]
while(i>=0):
    reversed_nums.append(nums.pop(i))
    i-=1
print(reversed_nums)

# 4.Count how many times a value appears.
nums=[1,3,2,4,4]
print(nums.count(4))

# 5.Find the max and min manually (no built-in functions).
nums=[1,2,3,4,5]
max=0
minimum=10
for num in nums:
    if num>max:
        max=num
    if num<minimum:
        minimum=num
print(max,minimum)

# 6.Append, insert, delete values.
nums=[1,2,3]
nums.append(4)
print(nums)
nums.insert(1,5)
print(nums)
nums.remove(2)
print(nums)

# 7.Slice the first 3 items.
nums=[1,2,3,4,5]
print(nums[0:3])

# 8.Loop through the list and print even numbers.
nums=[1,2,3,4,5]
for num in nums:
    if num%2==0:
        print(num)

# 9.Combine two lists into one.
nums =[1,2,3]
nums2=[4,5]
nums.extend(nums2)
print(nums)

# 10.Sort a list (ascending + descending).
nums=[5,3,4,8,7]
nums.sort(reverse=False)
print(nums)
nums.sort(reverse=True)
print(nums)
