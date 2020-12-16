m = int(input())
table = [[x for x in list(input())] for _ in range(m)]
symbol = '-'
for i in range(0, m):
    for j in range(0, m - 2):
        if table[i][j] == table[i][j+1] == table[i][j+2] == 'x':
            symbol = 'x'
        if table[i][j] == table[i][j+1] == table[i][j+2] == 'o':
            symbol = 'o'
for i in range(0, m-2):
    for j in range(0, m):
        if table[i+1][j] == table[i+2][j] == table[i][j] == 'x':
            symbol = 'x'
        if table[i + 1][j] == table[i + 2][j] == table[i][j] == 'o':
            symbol = 'o'
print(symbol)