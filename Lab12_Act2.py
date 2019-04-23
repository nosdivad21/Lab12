from math import *
#Number of elements
N = 10
#upper and lower bounds
a = float(input('Enter the lower bound:'))
b = float(input('Enter the upper bound:'))
# for later use
x = 1
y = 0
def Integration(N, a, b):
    def f(x):
        return x**2
    value = 0
    value2 = 2
    for n in range(1,N+1):
        value += f(a+((n-(1/2))*((b-a)/N)))
    value2 = ((b-a)/N)*value
    return value2
TOL = 10**-6
while abs(x-y) > TOL:
    x = Integration(N, a, b)
    N = N * 10
    y = Integration(N, a, b)
print(Integration(N, a, b))