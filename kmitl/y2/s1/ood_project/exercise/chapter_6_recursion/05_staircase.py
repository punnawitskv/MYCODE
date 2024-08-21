def staircase(n, current=1):
    if n == 0:
        print('Not Draw!')
        return

    if current > abs(n):
        return
    else:
        if n > 0:
            print('_' * (n - current) + '#' * current)
        else:
            print('_' * (current - 1) + '#' * (abs(n) - current + 1))
            
        staircase(n, current + 1)

staircase(int(input("Enter Input : ")))