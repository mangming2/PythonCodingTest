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
