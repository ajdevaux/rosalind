from functools import lru_cache
"""
This greatly speeds up the code by caching previous answers
"""
@lru_cache(maxsize=1000)
def fibo(n,k):
    """
    n is number of generations, k is number of pairs produced
    """
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibo(n-2,k)*k + fibo(n-1,k)

if __name__ == "__main__":
    n,k = input("Enter two numbers separated by a comma")
    fibo(n,k)
