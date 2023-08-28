# clean
# readability
# predictablity
# DRY
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

fill = '*'
empty = ' '
for row in picture:
    for element in row:
        if element:
            print(fill, end='')
        else:
            print(empty, end='')
    print('')
