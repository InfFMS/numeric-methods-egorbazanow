import numpy as np
import matplotlib.pyplot as plt
def snells_law(n1, n2, theta1):
  sin_theta2 = (n1 / n2) * np.sin(theta1)
  if abs(sin_theta2) > 1:
    return None  # Полное внутреннее отражение
  else:
    return np.asin(sin_theta2)
def optical_path_length(n1, n2, a, b, x, L, theta1):
  if snells_law(n1, n2, theta1) is None:
      return float('inf')
  theta2 = snells_law(n1, n2, theta1)
  path1 = np.sqrt((x - a)**2 + b**2)
  path2 = np.sqrt((L - x)**2 )
  return n1 * path1 + n2 * path2
def find_optimal_angle(n1, n2, a, b, L, num_angles=100):
    min_path_length = float('inf')
    optimal_theta1 = None
    best_x = None
    theta1_values = np.linspace(0, np.pi/2, num_angles)
    for theta1 in theta1_values:
        x = a + b/np.tan(theta1) if np.tan(theta1) !=0 else a
        if x < min(a,L) or x > max(a,L):
          continue
        path_length = optical_path_length(n1, n2, a, b, x, L, theta1)
        if path_length < min_path_length:
            min_path_length = path_length
            optimal_theta1 = theta1
            best_x = x
    return optimal_theta1, min_path_length, best_x
n1 = 1.0
n2 = 1.5
a = -2
b = 3
L = 2
optimal_theta1, min_path_length, best_x = find_optimal_angle(n1, n2, a, b, L)
if optimal_theta1 is not None:
    print(f"Оптимальный угол падения (theta1): {np.degrees(optimal_theta1):.2f} градусов")
    print(f"Минимальная оптическая длина пути: {min_path_length:.4f}")
    print(f"Точка преломления (x): {best_x:.4f}")
    x_points = [a, best_x, L]
    y_points = [b, 0, 0]
    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points, marker='o', linestyle='-', label="Луч")
    plt.axhline(0, color='black', linewidth=1, label="Граница раздела")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Минимизация оптической длины пути")
    plt.legend()
    plt.grid(True)
    plt.xlim(a - 1, L + 1)
    plt.ylim(-1, b + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
else:
    print("Не найдено решения: полное внутреннее отражение")
