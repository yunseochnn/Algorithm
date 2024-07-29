n,m = map(int,input().split())
board = []
result = []
for _ in range(n):
    board.append(input())
for i in range(n-7):
    for j in range(m-7):
        t1 = 0 #B로시작
        t2 = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2 == 0:
                    if board[x][y] != 'B':
                        t1 += 1
                    if board[x][y] != 'W':
                        t2 += 1
                else:
                    if board[x][y] != 'W':
                        t1 += 1
                    if board[x][y] != 'B':
                        t2 += 1
        result.append(t1)
        result.append(t2)
print(min(result))