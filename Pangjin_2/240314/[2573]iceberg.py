import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]
minus_Map = [[0]*M for _ in range(N)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
year = 0

while(1) : 

    for y in range(N):
        for x in range(M):
            if Map[y][x] > 0 : #무언가 있으면
                temp = 0 # 여기다가 저장
                for dir in range(4) : #네 방향 조사
                    yy = y + dy[dir]
                    xx = x + dx[dir]
                    if N > yy >= 0 and M > xx >= 0 and Map[yy][xx] == 0 : # 바다(0)이면
                        temp += 1

                minus_Map[y][x] = -temp

    for y in range(N):
        for x in range(M):
            Map[y][x] += minus_Map[y][x]
            if Map[y][x] < 0 : # 0보다 작으면
                Map[y][x] = 0 # 0으로 저장

    minus_Map = [[0]*M for _ in range(N)] # minus_Map 초기화

    visit_Map = [[0]*M for _ in range(N)] # 비짓맵
    cnt = 0 # 덩어리 몇개인지 count

    for y in range(N): # 두 덩어리인지 조사
        for x in range(M):
            if Map[y][x] > 0 and visit_Map[y][x] == 0: # 바다가 아니고, 방문하지 않았다면
                stack = []
                cnt += 1
                stack.append((y, x))
                while stack:
                    yy, xx = stack.pop()
                    visit_Map[yy][xx] = 1
                    for dir in range(4) : #네 방향 조사
                        yyy = yy + dy[dir]
                        xxx = xx + dx[dir]
                        if N > yyy >= 0 and M > xxx >= 0 and Map[yyy][xxx] > 0 and visit_Map[yyy][xxx] == 0 :
                            stack.append((yyy, xxx))

    visit_Map = [[0]*M for _ in range(N)] # 비짓맵

    year += 1
    if cnt > 1 :
        print(year)
        break
    
    Sum = 0
    for y in range(N): # 두 덩어리인지 조사
        for x in range(M):
            Sum += Map[y][x]

    if Sum == 0 :
        print(0)
        break





