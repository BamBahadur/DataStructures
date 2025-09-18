class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        total_length = len(s)
        last_len = 0

        for i in range(total_length,0,-1):
            if s[i-1] == " ":
                if last_len>0:
                    break
            else:
                last_len+=1
            
            
        return last_len