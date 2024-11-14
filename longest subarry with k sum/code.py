arr = list(map(int, input("Enter a number separated br space :").strip(" ").split(" ")))
k = int(input("Enter a k value :"))
n = len(arr)
i , j = 0, 0

lenght = 0
sum = arr[0]

while(j < n):
    if(sum == k):
        if(lenght < (j-i)+1):
            lenght +=1
        j+=1
        sum += arr[j]
    elif sum < k:
        j+=1
        sum += arr[j]
    else:
        sum -= arr[i]   
        i +=1    

print(i, j, lenght)