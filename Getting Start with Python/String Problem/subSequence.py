#User function Template for python3
class Solution:
    def numberOfSubsequences (self,S,W):
        # code here 
        # for i in range(len(S)):
        #User function Template for python3
        used = [False] * len(S)
        count = 0
        
        while True:
            pos = 0
            temp = []
            
            for i in range(len(S)):
                if not used[i] and S[i] == W[pos]:
                    temp.append(i)
                    pos += 1
                    if pos == len(W):
                        break
                    
            if pos == len(W):
                count += 1
                for p in temp:
                    used[p] = True
                    
            else:
                break
            
        return count
print(Solution().numberOfSubsequences('GeeksforGeeks','Gks'))