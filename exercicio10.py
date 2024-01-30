#CREATE TWO ARRAYS WITH NUMBERS FROM 1 TO 10
#AND ANOTHER ARRAY FROM NUMBERS FROM 10 TO 15
#CAN WE MAKE THESE ARRAYS INSIDE ANOTHER 2D ARRAY? 
#ANSWER: NO

#WHAT IF WE MAKE THESE ARRAYS TRANSFORM TO LISTS, AND MAKE  
#A 2D LIST, CAN WE? 
#ANSWER:YES

nums_10_list = []
nums_15_list = []

nums_10 = range(11)
nums_15 = range(10, 16)

#CONVERT TO LIST IF NUMPY:
# lista1 = nums_10.tolist()


for nums in nums_10:
    nums_10_list.append(nums)

for nums in nums_15:
    nums_15_list.append(nums)

print(nums_10_list)
print(nums_15_list)
    
list2D = [nums_10_list, nums_15_list]

print(list2D)

