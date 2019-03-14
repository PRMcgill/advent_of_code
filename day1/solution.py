starting_point = [0, 0, 0, 0]
direction = 0
with open('input.txt') as f:
    directions = f.read()

turns = directions.split(', ')

for turn in turns:
    letter = turn[0]
    number = int(turn[1:])
    if letter == 'L':
        direction -= 1
    else:
        direction += 1
    direction %= len(starting_point)
    starting_point[direction] += number

print(abs(starting_point[0] - starting_point[2]) + abs(starting_point[1] - starting_point[3]))

