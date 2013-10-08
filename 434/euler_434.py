from functools import lru_cache
 
@lru_cache(maxsize=None)
def R(i, j, m):
    res = pof2[i*j]
    for a in range(1,i+1):
        for b in range(0, j+1):
            if a == i and b == j:
                continue
            res = (res - nCr[i-1][a-1]*nCr[j][b]*\
                    pof2[(i-a)*(j-b)]*R(a, b, m)) % m
    return res
 
def precompute(N, m):
    # precompute 2^(i*j) for i*j <= N*N
    global pof2
    pof2 = [0 for i in range((N+1)*(N+1))]
    pof2[0] = 1
    for i in range(1,(N+1)*(N+1)):
        pof2[i] = (pof2[i-1]*2) % m
 
    # precompute n choose r for n,r < N
    global nCr
    nCr = [[0 for r in range(N+1)] for n in range(N+1)]
    for i in range(N+1):
        nCr[i][0] = 1
    for n in range(1, N+1):
        for r in range(1, N+1):
            nCr[n][r] = (nCr[n-1][r-1] + nCr[n-1][r]) % m
 
def S(N, m):
    # sum up all R (use R_ij = R_ji)
    res = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            f = 1 if i == j else 2
            res += f*R(i, j, m) % m
    return res % m
 
if __name__=="__main__":
    m = 1000000033
    N = 100
 
    from datetime import datetime
    startTime = datetime.now()
    precompute(N,m)
    print(S(N,m))    
    print("runtime: {0}".format( datetime.now()-startTime) )
