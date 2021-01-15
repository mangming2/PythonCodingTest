n,m = map(int,input().split())
x,y,direction =  map(int,input().split())
array=[]

for i in range(n):
  array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
array[x][y]=1
def turn():
  global direction
  direction+=1
  if direction==4:
    direction=0
result=1
turn_count=0
while True:
  turn()
  
  nx= x+dx[direction]
  ny = y+dy[direction]

  if array[nx][ny]==0:
    array[nx][ny]=1
    result+=1
    x=nx
    y=ny
    turn_count=0
    continue
  else:
    turn_count+=1

  if turn_count==4:
    break

print(result)

