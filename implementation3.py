data = input()

column= int(ord(data[0]))-int(ord('a'))+1
row=int(data[1])

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

count =0

for step in steps:
  next_row = row+step[0]
  next_column = column+step[1]

  if next_row >=1 and next_row<=8 and next_column>=1 and next_column<=8:
    count +=1

print(count)

''''
data = input()

column = int(ord(data[0])-ord('a')+1)
row = int(data[1])


steps = [(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]

count =0
for step in steps:
  next_column = column + step[1]
  next_row = row +step[0]

  if next_column>=1 and next_column<=8 and next_row>=1 and next_row<=8:
    count+=1

print(count)
'''