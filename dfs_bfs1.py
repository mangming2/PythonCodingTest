#by bfs
from collections import deque

n,m = map(int,input().split())

array=[]
for i in range(n):
  array.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if array[nx][ny]==1:
        continue
      if array[nx][ny]==0:
          array[nx][ny]=1
          queue.append((nx,ny))
      
count =0
for i in range(n):
  for j in range(m):
    if array[i][j]==0:
      bfs(i,j)
      count+=1
      
              
print(count) 
print(array[0][1])   


''''
복습
from collections import deque
n, m = map(int,input().split())
array=[]
for i in range(n):
  array.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if array[nx][ny]==1:
        continue
      if array[nx][ny]==0:
        array[nx][ny]=1
        queue.append((nx,ny))
count =0
for i in range(n):
  for j in range(m):
    if array[i][j]==0:
      count+=1
      bfs(i,j)
print(count)      
'''