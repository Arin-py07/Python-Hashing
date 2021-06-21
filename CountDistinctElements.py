#Without using set:

def cDistinctFinder(l):
    res = 1
    
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res = res+1
    
    return res
  
l = [10,20,10,30,30,20]
print(cDistinctFinder(l))


#using Set:---------------------------------------------------------------------------------------------------------------------------------------------------------

def cDistinctFinder2(l):
  return len(set(l))    #Internally using Hashing technique that's why it is more efficient solution.

l = [10,20,10,30,30,20]
print(cDistinctFinder2(l))
  
