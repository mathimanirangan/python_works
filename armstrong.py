def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n=int(input())
    for i in range(1,n+1):
        if isarm(i):
            print(i)

    return 0
def isarm(n):
    total=0
    orig=n
    l=len(str(n))
    while n!=0:
        d=n%10
        n//=10
        total=total+d**l
    return(orig==total)

if __name__ == '__main__':
    main()
