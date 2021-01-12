n,m=map(int,input().split())
result=0
for i in range(n):
 array=list(map(int,input().split()))
 min_result=min(array)
 result=max(min_result,result)

print(result)


