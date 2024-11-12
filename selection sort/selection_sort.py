arr = list(map(int, input("Enter a list of numbers with space :").strip(" ").split(" ")))

def selection_sort(arr):
    #return a array if length is leass than one
    if(len(arr) <= 1):
        return arr
    
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_index]):
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    
    return arr

print(arr)  
print(selection_sort(arr))