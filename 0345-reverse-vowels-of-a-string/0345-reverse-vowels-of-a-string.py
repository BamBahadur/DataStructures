class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        Vowels = "AEIOUaeiou"

        last_index = len(s)-1
        first_index = 0

        while (first_index<last_index):
            if(s_list[first_index] in Vowels):
                if(s_list[last_index] in Vowels):
                    s_list[first_index],s_list[last_index] = s_list[last_index],s_list[first_index]
                    first_index+=1
                    last_index-=1
                else:
                    last_index-=1
            else:
                first_index+=1
        return "".join(s_list)