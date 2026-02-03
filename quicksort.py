def quicksort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)
        quicksort(arr, low, pindex - 1)
        quicksort(arr, pindex + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
  
