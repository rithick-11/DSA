arr = list(map(int, input("Enter a number :").strip(" ").split(" ")))

def binary_search(arr, low, high, target):
    if low > high :
        return -1
    
    mid = (low + high) // 2

    if target == arr[mid]:
        return mid
    
    if target > arr[mid]:
        return binary_search(arr, mid+1, high, target)
    
    return binary_search(arr, low, mid-1, target)



def binary(arr, target):
    low = 0
    high = len(arr) - 1

    # while(low <= high):
    #     mid = (low + high) // 2
    #     if(target == arr[mid]):
    #         return mid
    #     elif target > arr[mid]:
    #         low = mid + 1
    #     else:
    #         high = mid - 1

    return binary_search(arr, low, high, target)


print(binary(arr, 16))