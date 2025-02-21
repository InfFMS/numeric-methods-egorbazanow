import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return np.cos(x)
def arc_length(f, a, b, n=1000):
  x = np.linspace(a, b, n+1)
  y = [f(val) for val in x]
  arc_len = 0.0
  for i in range(1, n+1):
    ds = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    arc_len += ds
  return arc_len
a = 0
b = np.pi
length = arc_length(f, a, b)
print(f"Длина горки от {a} до {b}: {length:.4f}")
x = np.linspace(a, b, 400)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="Горка: cos(x)")
ax.set_xlabel("x")
ax.set_ylabel("y = cos(x)")
ax.set_title("Профиль горки")
ax.grid(True)
ax.legend()
plt.show()

def f(x):
  return np.cos(x) + 0.1 * x**2
def arc_length(f, a, b, n=1000):
  x = np.linspace(a, b, n+1)
  y = [f(val) for val in x]
  arc_len = 0.0
  for i in range(1, n+1):
    ds = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    arc_len += ds
  return arc_len
a = 0
b = np.pi
length = arc_length(f, a, b)
print(f"Длина горки от {a} до {b}: {length:.4f}")
x = np.linspace(a, b, 400)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="Горка: cos(x) + 0.1*x**2")
ax.set_xlabel("x")
ax.set_ylabel("y = cos(x) + 0.1*x**2")
ax.set_title("Профиль горки")
ax.grid(True)
ax.legend()
plt.show()

def f(x):
  """Функция, описывающая профиль горки"""
  return -np.tanh(x - np.pi/2)

def arc_length(f, a, b, n=1000):
  x = np.linspace(a, b, n+1)
  y = [f(val) for val in x]
  arc_len = 0.0
  for i in range(1, n+1):
    ds = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    arc_len += ds
  return arc_len
a = 0
b = np.pi
length = arc_length(f, a, b)
print(f"Длина горки от {a} до {b}: {length:.4f}")
x = np.linspace(a, b, 400)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="Горка: -tanh(x - π/2)")
ax.set_xlabel("x")
ax.set_ylabel("y = -tanh(x - π/2)")
ax.set_title("Профиль горки")
ax.grid(True)
ax.legend()
plt.show()
def f(x):
  return -0.2*(x - np.pi)**3 + 0.5*(x - np.pi)**2 + 1
def arc_length(f, a, b, n=1000):
  x = np.linspace(a, b, n+1)
  y = [f(val) for val in x]
  arc_len = 0.0
  for i in range(1, n+1):
    ds = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    arc_len += ds
  return arc_len
a = 0
b = np.pi
length = arc_length(f, a, b)
print(f"Длина горки от {a} до {b}: {length:.4f}")
x = np.linspace(a, b, 400)
y = [f(val) for val in x]
fig, ax = plt.subplots()
ax.plot(x, y, label="Горка: -0.2*(x-π)**3 + 0.5*(x-π)**2 + 1")
ax.set_xlabel("x")
ax.set_ylabel("y = -0.2*(x-π)**3 + 0.5*(x-π)**2 + 1")
ax.set_title("Профиль горки")
ax.grid(True)
ax.legend()
plt.show()