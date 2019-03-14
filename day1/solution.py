# where we fist start out
starting_point = [0, 0, 0, 0]
# the steps we will go
direction = 0
# how to get the turns (R3/ L1) from the file
with open('input.txt') as f:
    directions = f.read()
# how to split the file and remove the , and space after every turn
turns = directions.split(', ')
# to calculate each block
for turn in turns:
    letter = turn[0]
    number = int(turn[1:])
    if letter == 'L':
        direction -= 1
    else:
        direction += 1
    # to make sure to not be out of bounds
    direction %= len(starting_point)
    # to take all the numbers and add it to the individual directions
    starting_point[direction] += number
# takes the total amount of blocks start_point[0] and starting_point[2] are the north and south while starting_point[1] and starting_point[3] are east and west.
print(abs(starting_point[0] - starting_point[2]) + abs(starting_point[1] - starting_point[3]))

