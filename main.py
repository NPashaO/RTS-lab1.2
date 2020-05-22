import matplotlib.pyplot as plt
from algs import signal, get_m, get_D, get_R, get_R_by_gen, r_tau

# option values
n = 10
omega = 1100
N = 256

range_min = 0
range_max = 1

x_gen = signal(n, omega, N, range_min, range_max)
y_gen = signal(n, omega, N, range_min, range_max)

x = [x_gen(i) for i in range(N)]
y = [y_gen(i) for i in range(N)]

plt.plot(range(N), x, label='x')
plt.plot(range(N), y, label='y')
plt.legend()
plt.show()
m = get_m(x)
D = get_D(x, m)

print(f'm: {m}\nD: {D}')

r_tau_X = [r_tau(x_gen, y_gen, N, tau) for tau in range(N//2)]
r_tau_Y = [r_tau(x_gen, x_gen, N, tau) for tau in range(N//2)]
plt.plot(range(N//2), r_tau_X, label='Rxx_tauX')
plt.plot(range(N//2), r_tau_Y, label='Rxx_tauY')
plt.legend()
plt.show()

