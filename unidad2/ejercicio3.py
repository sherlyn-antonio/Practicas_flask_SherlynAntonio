matriz = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R'],
    ['S', 'T', 'U'],
    ['V', 'W', 'X'],
    ['Y', 'Z']
]

for i in range(0,9):
    for j in range(0,3):
        if i == 8 and j == 2:
            break
        print(f"posición[{i}][{j}] = {matriz[i][j]}")