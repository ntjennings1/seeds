""" Gathers number list from user.

@return nums : The numbers
@rtype nums : list
"""
def get_nums():

    i = 0
    nums = []
    size = 9

    while i < size:
        nums.append(int(input('Enter a single number: ')))
        i += 1

    return nums

""" Organizes similar numbers in groups.

@returns null
"""
def alikes():

    nums = get_nums()

    i = 0
    c = 0
    group = []
    groups = []

    while i < len(nums):
        
        found = False
                        
        while c < len(groups):
            if groups[c][0] == nums[i]:
                groups[c].append(nums[i])
                found = True
                exit
            c += 1
        c = 0
        
        if not found:
            group.append(nums[i])
            groups.append(group)
        
        group=[]
        i += 1

    print("The groups are: ", groups)
        
""" Runs the alikes function. """
alikes()