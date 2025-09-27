import numpy as np

# Создаем случайный массив
arr = np.random.rand(100)
print("Исходный массив:")
print(f"Min: {arr.min():.4f}, Max: {arr.max():.4f}")
print(f"Первые 10 элементов: {arr[:10]}")

# Min-max нормализация
arr_normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("\nПосле нормализации:")
print(f"Min: {arr_normalized.min():.4f}, Max: {arr_normalized.max():.4f}")
print(f"Первые 10 элементов: {arr_normalized[:10]}")