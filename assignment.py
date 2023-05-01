# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition(a, b):
    sum = a + b 
    return sum

# Write a Python function that takes a string as input and returns 
# the string reversed.
def reversal(input_string):
    for x in reversed(input_string):
        return (x)

# Write a Python function that takes a list of integers as
# input and returns the sum of all the integers in the list.   
def adding(numbers):
    return sum(numbers) 

numerals = [1, 2, 3, 4, 5, 6, 7, 8]
do_add = (numerals)
print(do_add) 

# Write a Python function that takes a list of integers as input and returns a new list with 
# all the even numbers removed. 
def no_even(nums):
    for i in nums:
        if i % 2 != 0:
            return(i)
        
nums = [1,2,3,4,5,6,7,8,9]
nums1 = no_even(nums)
print(nums1)

# Write a Python function that takes a list of integers as input and returns 
# the highest value in the list.
def highest(num2):
    return max(num2)

the_list = [3,4,5,6,7,8,9,2,1]
highest_value = highest(the_list)
print(highest_value)