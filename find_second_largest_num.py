n = int(input())
arr=[]
for i in range(n):
    x = list( map(int, input().split())) 
    arr.append(x)
   
print (arr)
larger= max(num for num in arr if num!=max(arr))
print (larger)
