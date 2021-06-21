N = 10
arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
sum = 14
Output: 
1

Solution:
  
def sumExists(arr, N, sum):
    #Your code here
    dict = {}
    
    for k,v in enumerate(arr):
        if (sum - v) in dict:
            return 1
        
        dict[v] = k
    return 0
