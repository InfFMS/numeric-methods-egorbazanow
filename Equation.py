import numpy as np
import matplotlib.pyplot as plt
def solve_ddd(f, a, b, eps=0.01):
    if f(a) * f(b) > 0:
        print("Функция не меняет знак на заданном отрезке. Корень может отсутствовать или быть четным.")
        return None
    while (b - a) / 2 >= eps:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c
def f(x):
    return x**3 - x + 1
x_min = -3
x_max = 3
x = np.linspace(x_min, x_max, 1000)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = x^3 - x + 1")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("График функции f(x) = x^3 - x + 1")
ax.grid(True)
a = -2
b = 0
eps = 1e-7
root = solve_ddd(f, a, b, eps)
if root is not None:
    ax.plot(root, f(root), 'ro', label=f"Корень: x ≈ {root:.5f}")
    print(f"Приближенное значение корня: {root}")
ax.legend()
plt.show()
def f(x):
    return x**3 - x**2 - 9*x - 9
x_min = -5
x_max = 5
x = np.linspace(x_min, x_max, 1000)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = x^3 - x^2 - 9x - 9")
ax.axhline(0, color='black', linewidth=0.5) # Ось x
ax.axvline(0, color='black', linewidth=0.5) # Ось y
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("График функции f(x) = x^3 - x^2 - 9x - 9")
ax.grid(True)
a = 2
b = 4
eps = 1e-7
root = solve_ddd(f, a, b, eps)
if root is not None:
    ax.plot(root, f(root), 'ro', label=f"Корень: x ≈ {root:.5f}")
    print(f"Приближенное значение корня: {root}")
ax.legend()
plt.show()
def f(x):
    return x**2 - np.exp(x)
x_min = -2
x_max = 4
x = np.linspace(x_min, x_max, 1000)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = x^2 - e^x")
ax.axhline(0, color='black', linewidth=0.5) # Ось x
ax.axvline(0, color='black', linewidth=0.5) # Ось y
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("График функции f(x) = x^2 - e^x")
ax.grid(True)
a1 = -1
b1 = 0
eps = 1e-7
root = solve_ddd(f, a1, b1, eps)
if root is not None:
    ax.plot(root, f(root), 'ro', label=f"Корень: x ≈ {root:.5f}")
    print(f"Приближенное значение корня: {root}")
ax.legend()
plt.show()
def solve_ddd(f, a, b, eps=0.01):
    """
    Решает уравнение f(x) = 0 методом дихотомии на отрезке [a, b].
    Требует, чтобы функция f(x) меняла знак на этом отрезке и была непрерывной.
    """
    if f(a) * f(b) > 0:
        print(f"Функция не меняет знак на отрезке [{a}, {b}]. Корень может отсутствовать или быть четным.")
        return None

    while (b - a) / 2 >= eps:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c
def f(x):
    if x <= 0:
        return float('inf')
    return 5*x - 6*np.log(x) - 7
x_min = 0.1
x_max = 5
x = np.linspace(x_min, x_max, 400)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = 5x - 6ln(x) - 7")
ax.axhline(0, color='black', linewidth=0.5) # Ось x
ax.axvline(0, color='black', linewidth=0.5) # Ось y
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("График функции f(x) = 5x - 6ln(x) - 7")
ax.grid(True)
ax.set_ylim(-10, 10)
eps = 1e-7
roots = []
intervals = [(0.1, 1.5), (2, 3)]
colors = ['ro', 'go']

for i, (a, b) in enumerate(intervals):
    root = solve_ddd(f, a, b, eps)
    if root is not None:
        roots.append(root)
        ax.plot(root, f(root), colors[i], linestyle='None', label=f"Корень: x ≈ {root:.5f}")
        print(f"Приближенное значение корня: {root}")
    else:
        print(f"Корень не найден на интервале [{a}, {b}].")
ax.legend()
plt.show()
def f(x):
    return np.cos(x) + 2*x - 3
x_min = -2
x_max = 5
x = np.linspace(x_min, x_max, 1000)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="f(x) = cos(x) + 2x - 3")
ax.axhline(0, color='black', linewidth=0.5) # Ось x
ax.axvline(0, color='black', linewidth=0.5) # Ось y
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("График функции f(x) = cos(x) + 2x - 3")
ax.grid(True)
ax.set_ylim(-5, 5)
eps = 1e-7
a = 1
b = 2
root = solve_ddd(f, a, b, eps)
if root is not None:
    ax.plot(root, f(root), 'ro', linestyle='None', label=f"Корень: x ≈ {root:.5f}")
    print(f"Приближенное значение корня: {root}")
else:
    print(f"Корень не найден на интервале [{a}, {b}].")
ax.legend()
plt.show()


