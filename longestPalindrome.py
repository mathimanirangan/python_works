def longestPalindrome(s):
    op = ''
    max = 0
    j=0
    if s == s[::-1]:
        return(s)
    for i in range(len(s)):
        j=j+i
        while j <= len(s) and i <= j:
            if s[i:j] == s[i:j][::-1]:
                # print(s[i:j],'palindrome')
                if max < len(s[i:j]):
                    max=len(s[i:j])
                    op = s[i:j]
            # print(s[i:j],s[i:j][::-1])
            j+=1
        j=0
    return op


print(longestPalindrome('bb'))

# for i in range(5):
#     print(i)