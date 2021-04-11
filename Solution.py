MOD = 1000000007

t = int(input())

def f(c0, c1):
    c1 -= 1
    res = 1
    for i in range(c0 + 1, c0 + c1 + 1):
        res = res * i // (i - c0)
    return res % MOD

for _ in range(t):
    c0, c1 = map(int, input().split())
    print(f(c0, c1))
