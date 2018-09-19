from math import factorial

def main():
    n = int(input('enter the no of rows:'))
    for i in range(n):
        j,space = 0,0
        while space < n-i:
            print(' ',end='')
            space += 1
            
        while j <= i:
            res = factorial(i) //( factorial(j)*factorial(i-j))
            print(str(res) + ' ',end='')
            j += 1
        print()


if __name__ == '__main__':
    main()