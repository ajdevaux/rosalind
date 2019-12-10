from functools import lru_cache
"""
This greatly speeds up the code by caching previous answers
"""

def fibd(n, m):
    """
    n is number of generations in months, m is lifespan of rabbits in months
    """
    @lru_cache(maxsize=1000)
    def babies(n,m):
        if n == 1:
            return 1
        else:
            return adults(n-1) + mature(n-1,m)
    @lru_cache(maxsize=1000)
    def adults(n):
        if n == 1:
            return 0
        else:
            return babies(n-1,m)
    @lru_cache(maxsize=1000)
    def mature(n,m):
        if n == 1:
            return 0
        else:
            return adults(n-1) + mature(n-1,m) - deaths(n,m)

    @lru_cache(maxsize=1000)
    def deaths(n,m):
        if n <= m:
            return 0
        else:
            return babies(n-m,m)

    if (m < 3) & (n >= 3):
        return 0
    else:
        return sum((mature(n,m),adults(n),babies(n,m)))


n=10
m=3
print(fibd(n,m),deaths(n,m))


12 2

258314806822396236 721911415500
