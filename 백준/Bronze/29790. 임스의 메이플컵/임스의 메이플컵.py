n, u, l = map(int, input().split())

cond_baek = 1000 <= n
cond_maple = (8000 <= u) or (260 <= l)

if cond_baek and cond_maple:
    print('Very Good')
elif cond_baek and (cond_maple == False):
    print('Good')
elif cond_baek == False:
    print('Bad')