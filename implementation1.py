n=int(input())
x,y=1,1
plans=list(input().split)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx=x+dx[i]
      ny=y+dy[i]

  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  x,y=nx,ny
print(x,y)

''''
내풀이
n=int(input())

move = list(input().split())

move_types = ['L','R','U','D']
x,y=1,1
dx=[0,0,-1,+1]
dy=[-1,+1,0,0]

for i in range(len(move)):
  for j in range(len(move_types)):
   if move[i] == move_types[j]:
    x+=dx[j]
    y+=dy[j]
    if x>n or x<1 or y>n or y<1:
      x-=dx[j]
      y-=dy[j]


print(x,y)
'''