x=int(input())
count=0
arr=list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i]>x:
        count+=1
print(count)

