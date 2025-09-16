#Back-end complete function Template for Python 3

class Solution:
    def numberOfSubsequences(self,S,W):
        
        S=list(S)
        W=list(W)
    
        ans=0
    
        while True:  #  Untill no such subsequence exist
    
            i=0
            j=0
            flag=0
    
            while i<len(S):
    
                if S[i]==W[j]:
    
                    j+=1
                    S[i]='*'
    
                    if j==len(W):
    
                        ans+=1   # A subsequence found
                        flag=1
                        break
    
    
                i+=1
    
            if flag==0:   # No subsequence found in this iteration
                break
    
    
        return ans
print(Solution().numberOfSubsequences('GeeksforGeeks','Gks'))                                                                                               