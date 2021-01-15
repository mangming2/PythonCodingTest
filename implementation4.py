n,m = map(int,input().split())
x,y,direction =map(int,input().split())

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))

array[x][y] = 1

dx =[-1,0,1,0]
dy= [0,1,0,-1]

def turn():
  global direction
  direction-=1
  if direction==-1:
    direction=3

count =1
turn_time =0

while True:
  turn()
  nx = x+dx[direction]
  ny = y+dy[direction]

  if array[nx][ny]==0:
    array[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time=0
  else:
    turn_time+=1

  if turn_time==4:
    break

  print(count)
    
