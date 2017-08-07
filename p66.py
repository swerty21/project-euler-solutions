def continued_frac(n):
    a0 = int(n**0.5)
    a,m,d = a0,0,1
    while True :
        yield a
        m = a*d - m
        d = (n - m*m)//d
        a = (a0 + m)//d

def pell_sol(n):
    h_1, h_2 = 1, 0
    k_1, k_2 = 0, 1
    a = continued_frac(n)
    i = 0
    for i, a_i in enumerate(a):
        h = a_i*h_1 + h_2
        k = a_i*k_1 + k_2
        if h*h - n*k*k == 1: return h,k
        h_1, h_2 = h, h_1
        k_1, k_2 = k, k_1
    return None 

res = []
for x in range(1,1000+1):
    x_sqrt = int(x**0.5)
    if x_sqrt*x_sqrt == x: continue
    res.append( (pell_sol(x)[0],x) )

print(max(res))
