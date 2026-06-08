#Fibonacci Using Memoization (Top-Down DP)
def fibonacci(n, memo={}):

    # Check if already calculated
    if n in memo:
        return memo[n]

    # Base cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Store result in memo
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


n = 7

print("Fibonacci Number:", fibonacci(n))


#Climbing Stairs Using DP Memoization
def climb_stairs(n, memo={}):

    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    if n < 0:
        return 0

    memo[n] = (
        climb_stairs(n - 1, memo)
        + climb_stairs(n - 2, memo)
    )

    return memo[n]


n = 4

print("Number of ways:", climb_stairs(n))


#Fibonacci Using Tabulation (Bottom-Up DP)
def fibonacci_tabulation(n):

    if n == 0:
        return 0

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 7

print("Fibonacci Number:", fibonacci_tabulation(n))