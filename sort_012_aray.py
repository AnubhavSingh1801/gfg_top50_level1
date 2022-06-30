"""
Refer Dutch Flag Algorithm

Time Complexity - O(N)
Space Complexity- O(1)
"""

def sort012(arr,n):
    # code here
    low, mid, high = 0, 0, n-1
    
    while(mid<=high):
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

if __name__ == "__main__":
    arr = [0, 2, 1, 2, 0]
    n = len(arr)
    sort012(arr, n)
    print(arr)