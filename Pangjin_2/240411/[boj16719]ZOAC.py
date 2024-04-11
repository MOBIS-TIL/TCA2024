import sys
from collections import deque
sys.stdin = open("input.txt", "r")

i = input()
q = deque()
dic = [deque() for _ in range(36)]
ans = [0]*(len(i)+1)

print(ans)
cnt = 0

for x in i :
    cnt += 1
    dic[ord(x)-55].append([x, cnt])

print(dic)

for x in range(len(dic)):
    if dic[x] :
        while dic[x] :
            word, y = dic[x].popleft()
            y = int(y)
            ans[y] = ord(word) - 55
            for i in ans:
                if i > 0 :
                    print(chr(i+55), end = "")
            print("")