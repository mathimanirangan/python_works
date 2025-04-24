picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]



def tree():
    r=0
    while r<len(picture):
        # print(r)
        c=0
        while c<len(picture[r]):
            # print(r,c,picture[r][c])
            print('*' if picture[r][c]==1 else ' ',end='')
            c=c+1
        print('')
        r=r+1

tree()
tree()
tree()