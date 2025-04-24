# def convert(s, numRows):
#     zig=(numRows*2)-2
#     zag=0
#     op=''
#     for i in range(numRows):
#         op+=s[i]
#         # print(i,zig,zag)
#         c=i
#         for j in range(len(s)):
#             c+=zig
#             if c<len(s) and zig > 0:
#                 op+=s[c]
#             c+=zag
#             if c<len(s) and zag >0:
#                 op+=s[c]
#         zig-=2
#         zag+=2
#         # print(i,zig,zag,op)
#     return op

def convert(s,numRows):
    if(numRows  < 2):
        return s
    arr = ['' for i in range(numRows)]
    direction = 'down'
    row = 0
    for i in s:
        arr[row] += i
        if row == numRows-1:
            direction = 'up'
        elif row == 0:
            direction = 'down'
        if(direction == 'down'):
            row += 1
        else:
            row -= 1
    print(arr)
    print(len(''.join(arr)))
    return(''.join(arr))
print(convert('MATHI',6))