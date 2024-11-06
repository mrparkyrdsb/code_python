# When Greedy Fails
# Problem = 2000 CCC S4 Golf

# When given a target distance to reach and number of clubs to use ... 
# What is the minimum number of strokes needed if the robot will always hit the exact distance 
# each club can offer
# For example:
# A distance of 10 with [3, 6, 1]; it would be possible to get to the target with 3 strokes using 6+3+1

def greedy(target, clubs):
    stroke = 0
    i = 0
    clubs.sort(reverse=True) # this allows greatest to least sorting

    while target > 0 and i < len(clubs):
        if clubs[i] > target:
            break
        else:
            target -= clubs[i]
            stroke += 1

            if clubs[i] > target:
                i += 1
    # end of while
    if target == 0:
        return stroke
    else:
        return -1
# end of greedy      

def dp_table(target, clubs):
    # table setup
    table = [0]
    for i in range(target):
        table.append(float("infinity"))
    # end of table setup #

    for distance, swings in enumerate(table):
        if swings != float("infinity"):
            for travel in clubs:
                new_location = distance + travel
                if new_location < len(table):
                    table[new_location] = min(table[new_location], swings + 1)
    
    if table[-1] != float("infinity"):
        return table[-1]
    else:
        return -1
# end of dp_table
    

test1 = (10, [3,6,1]) # Expects 3
test2 = (12, [7,4,2]) # Expects 3

target1 = test1[0]
club1 = test1[1]

target2 = test2[0]
club2 = test2[1]

test1_msg = f'''
For Test 1:
    Target Distance = {target1}
    Our Clubs = {club1}

    Greedy Solution Answer: {greedy(target1, club1)}
    dp_table Solution Answer: {dp_table(target1, club1)}
'''
print(test1_msg)

test2_msg = f'''
For Test 2:
    Target Distance = {target2}
    Our Clubs = {club2}

    Greedy Solution Answer: {greedy(target2, club2)}
    dp_table Solution Answer: {dp_table(target2, club2)}
'''
print(test2_msg)
