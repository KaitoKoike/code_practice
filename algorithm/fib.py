done = []
memo = {}

#全探索
def fib_all(n):
    a = 0
    b = 1
    c = int()
    i = 1
    while(True):
        if c == 0:
            c = a + b
            i += 1
        else:
            tmp = c
            c = c + b
            b = tmp
            i += 1
        if i == n:
            break
    return c
#メモ化探索
def fib_memo(n):
    #やったかどうかをためる
    if n not in done:
        if n == 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1
        else:
            memo[n] = fib(n-1)+fib(n-2)
        done.append(n)
        return memo[n]
    else:
        return memo[n]

#動的計画法利用
Max_N = int(1e+2)
dp = [0 for n in range(Max_N+1)]

def fib_dp(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    number = fib_all(n)
    print(number)
