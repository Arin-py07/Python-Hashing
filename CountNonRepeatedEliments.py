Input:
10
1 1 2 2 3 3 4 5 6 7
Output: 
4

Solution:
  
class Solution:
    
    def countNonRepeated(self,arr,n):
        
        #Hash-map
        ht = {}
        count = 0
        
        for i in range (n):
          
            if arr[i] not in ht:
                ht[arr[i]] = 0
            ht[arr[i]] += 1
            
        for x in ht:
            if ht[x]==1:
                count +=1
                
        return count
