# CCC J4 2013
# Maximum number of chores

# input
minutes = int(input())
total_chores = int(input())
duration = []
for i in range(total_chores):
    current = int(input())
    duration.append(current)
# END OF INPUT #

# Processing
# How to maximize the number of chores completed within
# given time frame???





# brute force -> create longest addition combination of total 
# minutes spent on doing chores

# greedy -> lets choose the easiest tasks and do many of them as possible
duration.sort() # python .sort() is O(nlogn)
chore_counter = 0
i = 0 # helps us index duration list

while time > 0:
    if duration[i] > time:
        break
    else:
        time -= duration[i]
        chore_counter += 1
        i += 1
print(chore_counter)