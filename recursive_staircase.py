import random

def num_ways(n, choices):
    ways = 0
    def helper(n, choices, current):
        nonlocal  ways
        if n == 0:
            ways += 1
            # print(current)
        else:
            for i in choices:
                if i <= n:
                    current.append(i)
                    helper(n-i, choices, current)
                    current.pop()


    current = []
    helper(n, choices, current)
    return ways


def num_ways_1(n, x):
    def helper_memo(n, x, memo):
        if not isinstance(x, list):
           x = list(x)
        if memo[n] is not None:
            return memo[n]

        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return 0
        else:
            if memo[n-x[0]] is not None:
                sum = memo[n-x[0]]
            else:
                sum = num_ways_1(n - x[0], x)
                memo[n - x[0]] = sum

            for i in range(1,len(x)):
                if memo[n-x[i]] is not None:
                    sum += memo[n-x[i]]
                else:
                    temp = num_ways_1(n - x[i], x)
                    memo[n - x[i]] = temp
                    sum += temp

            memo[n] = sum
            return sum

    memo = (n+1) * [None]
    return helper_memo(n,x, memo)



x = {1, 2}
ways = num_ways(35, x)
print('total ways:', ways)
# rs = num_ways_1(, x)
# print(rs)