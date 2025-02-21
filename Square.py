import numpy as np
import matplotlib.pyplot as plt
def integrate(f, a, b, n=1000):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral
def plot_blob(y1_func, y2_func, x_start, x_end, title):
  x = np.linspace(x_start, x_end, 400)
  y1 = [y1_func(val) for val in x]
  y2 = [y2_func(val) for val in x]
  plt.fill_between(x, y1, y2, color='skyblue')  # Цвет кляксы
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title(title)
  plt.grid(True)
  def area_func(x):
    return y1_func(x) - y2_func(x)
  area = integrate(area_func, x_start, x_end)
  plt.text(x_start + (x_end - x_start) * 0.1, min(y2) + (max(y1) - min(y2)) * 0.9, f"Площадь: {area:.4f}")  # Вывод площади на графике
  print(f"{title}: Площадь = {area:.4f}")
  plt.show()
def y1_1(x):
  return np.sin(2*x) + 1
def y2_1(x):
  return -0.2*x**2 + 0.5
def y1_2(x):
  return np.cos(x) + 1.2
def y2_2(x):
  return -0.5*x**2 + 0.7
def y1_3(x):
  return np.exp(-x**2) + 1
def y2_3(x):
  return -0.3*x**3 + 0.5
def y1_4(x):
  return np.exp(-x**2)
def y2_4(x):
    return 0.2*np.sin(3*x) - 0.5
def y1_5(x):
  return np.exp(-(x+1)**2) + np.exp(-(x-1)**2) + 0.5
def y2_5(x):
  return -0.3*x**2
plot_blob(y1_1, y2_1, 0, np.pi, "Клякса 1")
plot_blob(y1_2, y2_2, -np.pi/2, np.pi/2, "Клякса 2")
plot_blob(y1_3, y2_3, -2, 2, "Клякса 3")
plot_blob(y1_4, y2_4, -2, 2, "Клякса 4")
plot_blob(y1_5, y2_5, -2, 2, "Клякса 5")
