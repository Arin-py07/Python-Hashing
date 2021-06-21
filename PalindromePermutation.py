Input : "geegsgeeks"
Output : True
  
Input : "abaaac"
Output : False
  
Solution:
  
from collection import Counter #Counter is a subclass of Dictionary.

def isPalPer(s):
  cnt = Counter(s)
  odd = 0
  
  for freq in cnt.values():
    
    if freq%2 != 0:
      odd += 1
      
      if odd > 1 :
        return False
      
  return True
        
  
