class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target: 
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def first_occurrence(self, arr, target):
        low = 0
        high = len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1  # Keep searching on the left side
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def last_occurrence(self, arr, target):
        low = 0
        high = len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1  
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def search_range(self, arr, target):
        first = self.first_occurrence(arr, target)
        if first == -1:
            return [-1, -1]
        last = self.last_occurrence(arr, target)
        return [first, last]
    def count_occurrences(self, arr, target):
        first = self.first_occurrence(arr, target)
        if first == -1:
            return 0
        last = self.last_occurrence(arr, target)
        return last - first + 1
s = Solution()
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(s.count_occurrences(arr, target)) 