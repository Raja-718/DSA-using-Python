arr = [1,2,3,5]
n = len(arr) + 1
missing = n*(n+1)//2 - sum(arr)
print(missing)
