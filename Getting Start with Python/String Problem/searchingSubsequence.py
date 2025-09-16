class solution:
    def numberOfSubsequence(self, S,W):
        S = list(S)
        W = list(W)
        print(S, W)
        ans = 0
        while True:
            i = 0
            j = 0
            flag = 0
            while (i < len(S)):
                if(S[i]==W[j]):
                    j += 1
                    S[i] = '*'
                    print(S)
                    if(j == len(W)):
                        ans += 1
                        flag = 1
                        break
                i += 1
            if(flag == 0):
                break
        return ans
        
print(solution().numberOfSubsequence('GeeksforGeeks','Gks'))