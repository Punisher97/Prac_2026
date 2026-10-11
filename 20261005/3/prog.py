from math import *

def Calc(s, t, u):

    def S(x):
        return eval(s)
    
    def T(x):
        return eval(t)

    def U(x, y):
        return eval(u)
    
    def res(x):
        return U(S(x), T(x))

    return res

s, t, u = eval(input())
x = eval(input())

print(Calc(s, t, u)(x))