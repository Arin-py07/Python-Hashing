Input:
n = 13
Votes[] = {john,johnny,jackie,johnny,john,jackie,jamie,jamie,john,johnny,jamie,johnny,john}
Output: john 4

Explanation: john has 4 votes casted for 
him, but so does johny. john is 
lexicographically smaller, so we print 
john and the votes he received.

Solution:

from collections import Counter 
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        
        vote_count = Counter(arr)
        
        max_votes = max(vote_count.values())
        
        lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]
        
        return (sorted(lst)[0], max_votes)
