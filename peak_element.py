"""
The idea is based on the technique of Binary Search to check if the middle element is the peak element
or not. If the middle element is not the peak element, then check if the element on the right side is
greater than the middle element then there is always a peak element on the right side. If the element 
on the left side is greater than the middle element then there is always a peak element on the left side.
"""


def peakElement(arr, n):
    # Code here
    l, r = 0, n-1
        
    while(l<=r):
        mid = (l+r)//2

        #Checking if mid has reached extreme ends of the array or satisfy the given condition.
        if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == (n-1) or arr[mid] >= arr[mid+1]):
            return mid
        
        #Checking if mid is lessar than the left element. In this case we have to move to the left side of array.
        elif (arr[mid] < arr[mid-1] and mid > 0):
            r = mid - 1
        
        else:
            l = mid + 1


#Driver Code
if __name__ == "__main__":
    arr = [14, 14, 10, 4, 13, 8, 17]
    n = len(arr)
    print(peakElement(arr, n)) 