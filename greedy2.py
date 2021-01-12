n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    result+=first
    m-=1
    if m==0:
     break
  result+=second
  m-=1
  if m==0:
     break
     
print(result)

'''
내풀이
n,m,k=map(int,input().split())
array=list(map(int,input().split()))
array.sort()
mok = (m//(k+1))*(array[n-1]*k + array[n-2])
namuji=m%(k+1)*array[n-2]
result = mok +namuji
print(result)
'''