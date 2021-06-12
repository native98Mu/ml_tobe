"""凑零钱问题"""

#暴力解法
def coinChange(coins,n):
    #要凑出金额n，至少需要1+dp(n-1)枚硬币
    if n==0:
        return 0
    if n < 0:
        return -1
    res = float('INF')
    for coin in coins:
        subproblem = coinChange(coins,n-coin)
        if subproblem == -1: continue
        res = min(res,1+subproblem)
    return res if res != float("INF") else -1   
coins = [1,2,5]
# for i in range(10):
#     print(str(i)+" need: "+ str(coinChange(coins,i)) + "coins.")

#带备忘录

def mem_coinChange(coins,n):
    #要凑出金额n，至少需要1+dp(n-1)枚硬币
    if n==0:
        return 0
    
    return helper(memo,n)
def helper(memo):

coins = [1,2,5]
for i in range(10):
    print(str(i)+" need: "+ str(coinChange(coins,i)) + "coins.")

