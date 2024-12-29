""" Organizes numbers in groups of three.

@returns null
"""
def grouping(nums):

    i = 0
    count = 3
    group = []
    groups = []

    while i < len(nums):      
        group.append(nums[i])
        if ((i+1) % count == 0):
            groups.append(group)
            group = []
        i += 1
    if len(group) > 0:
        groups.append(group)

    print("The groups are: ", groups)
        
""" Runs the grouping function. """
grouping([1,2,3,4,1,2,4])