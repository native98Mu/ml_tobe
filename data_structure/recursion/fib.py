"""斐波那契数列第n个数"""
#经典递归
def fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
# for i in range(10):
#     print("Fib  " + str(i) +":   "+ str(fib(i)))
#带备忘录的递归，即就是每个f(n-1)和f(n-2)只算一次
def mem_fib(n):
    if n == 0: 
        return 0
    memo = (n+1)*[0]
    return helper(memo,n)
def helper(memo,n):
    if n <= 2:
        return 1
    if memo[n] != 0: 
        return memo[n]
    memo[n] = helper(memo,n-1)+helper(memo,n-2)
    return memo[n]
# for i in range(10):
#     print("Fib  " + str(i) +":   "+ str(mem_fib(i)))
#dp数组
def dp_fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    #创建动态表
    dp = (n+1)*[0]
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
# for i in range(10):
#     print("Fib  " + str(i) +":   "+ str(dp_fib(i)))

#带压缩dp
def dp_compression_fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    #创建动态表
    pre = 1
    curr  = 1
    sum = 0
    for i in range(3,n+1):
        sum = pre + curr
        pre = curr
        curr = sum
    return curr
for i in range(10):
    print("Fib  " + str(i) +":   "+ str(dp_compression_fib(i)))




