def lengthOfLongestSubstring(s):
        longest = 0
        indexes = {}
        offset = 0
        for i in range(len(s)):
            char = s[i]
            index = indexes.get(char)
            print("index outside if",indexes,index,char,i)
            if index is not None and index >= offset:
                length = i - offset
                offset = index + 1
                if length > longest:
                    longest = length
            # print(indexes)
            indexes[char] = i
            print(indexes,f"longest={longest}", f"offset={offset}")
        return max(longest, (len(s) - offset))


print(lengthOfLongestSubstring("MRRRMAB"))