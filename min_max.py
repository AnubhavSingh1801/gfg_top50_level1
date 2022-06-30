"""
Time Complexity - O(N)
Space Complexity- O(1)
"""

import sys
def getMinMax( a, n):
    min_num, max_num = sys.maxsize, -sys.maxsize
    
    for i in a:
        if i > max_num:
            max_num = i
        
        if i < min_num:
            min_num = i
        
    return min_num, max_num

#Driver code

if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    n = len(a)
    print(getMinMax(a,n))