def lower_bound(arr, target):
    ans = len(arr)
    low = 0
    high = ans - 1
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] >= target):
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans

print("Lower bound in python")
arr = list(map(int, input("Enter a number :").strip(" ").split(" ")))
target = int(input("Enter the target value :"))

print(lower_bound(arr, target))
