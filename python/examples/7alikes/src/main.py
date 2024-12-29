""" Organizes similar numbers in groups.

@returns null
"""
def alikes(nums):

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
alikes([1,2,3,4,1,2,3,4,5,5,5])