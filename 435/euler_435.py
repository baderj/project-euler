def mat_mult(A, B, m):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= m
    return C
 
def mat_pow(A, p, m):
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)
 
def fib(n, m):
    T = [[1,1], [1,0]]
    if n == 1:
        return 1
    T = mat_pow(T, n-1, m)
    return T[0][0]
 
def mpow(x, p, m):
    if p == 1:
        return x
    if p % 2:
        return x*mpow(x, p-1, m) % m
    r = mpow(x, p//2, m)
    return r*r % m
 
def F(n, x, m):    
    b = (x*x + x - 1)
    f_nn = fib(n+1, m*b)
    f_n = fib(n, m*b)
    a = (f_nn*mpow(x, n+1, m*b) + f_n*mpow(x, n+2, m*b) - x) % (m*b)
    return a/b
 
def calc(n,m,x_range):
    R = 0    
    for x in x_range:
        R += F(n, x, m) 
        R %= m    
    return R
 
if __name__ == "__main__":
    n = pow(10,15)
    m = 1307674368000
    x_range = range(0, 101)
    print(calc(n, m, x_range))