import numpy as np
from scipy.linalg import lu
from scipy import stats
from collections import Counter

def print2DArray(arr):
    if type(arr) == int:
        print("Нет матрицы")
        return
    for i in range(len(arr)):
        print(" ")
        for j in range(len(arr[0])):
            print(np.round(arr[i][j], 2), end=" ")
print("1: ")
M1 = np.array([[2., 0., -1., 25.],
               [-6., 28., -7.4, 0.],
               [1., -5., 13., 2.8],
               [0., 4., 3., 1.7]])
print2DArray(M1)

print("\n2: ")
P, L, U = lu(M1)
print("Пермутационная матрица P:")
print2DArray(P)

print("\nНижняя треугольная матрица L:")
print2DArray(L)

print("\nВерхняя треугольная матрица U:")
print2DArray(U)

print("\n3: ")
det_P = np.linalg.det(P)

det_L = np.prod(np.diag(L))

det_U = np.prod(np.diag(U))

det_A = det_P * det_L * det_U

# Выводим результаты
print(f"Определитель P: {det_P}")
print(f"Определитель L: {det_L}")
print(f"Определитель U: {det_U}")
print(f"Определитель A: {det_A}")

print("\n4: ")
# Установка генератора случайных чисел для воспроизводимости
np.random.seed(42)

# Генерация выборки с равномерным распределением
uniform_sample = np.random.randint(1, 101, size=100)

# Генерация выборки с нормальным распределением
# Генерируем числа между 1 и 100 с нормальным распределением
mean = 50
std_dev = 15
normal_sample = np.random.normal(loc=mean, scale=std_dev, size=100)

# Округляем значения и ограничиваем их в диапазоне [1, 100]
normal_sample = np.clip(np.round(normal_sample), 1, 100).astype(int)

# Выводим результаты
print("Выборка с равномерным распределением:")
print(uniform_sample)

print("\nВыборка с нормальным распределением:")
print(normal_sample)

print("\n5: ")
# Определение функции для вычисления характеристик выборки
def compute_statistics(sample):
    stats_dict = {
        "mean": np.mean(sample),
        "mode": stats.mode(sample)[0],  # Извлечение моды
        "median": np.median(sample),
        "min": np.min(sample),
        "max": np.max(sample),
        "std_dev": np.std(sample, ddof=0)  # Для выборки используем поправку ddof=0
    }
    return stats_dict

# Вычисляем статистики для обеих выборок
uniform_stats = compute_statistics(uniform_sample)
normal_stats = compute_statistics(normal_sample)

# Выводим результаты
print("Статистические характеристики для выборки с равномерным распределением:")
for stat, value in uniform_stats.items():
    print(f"{stat.capitalize()}: {value}")

print("\nСтатистические характеристики для выборки с нормальным распределением:")
for stat, value in normal_stats.items():
    print(f"{stat.capitalize()}: {value}")

print("\n6: ")
# Установка генератора случайных чисел для воспроизводимости
np.random.seed(42)

# Генерация выборки с равномерным распределением
uniform_sample = np.random.randint(1, 101, size=100)

# Генерация выборки с нормальным распределением
mean = 50
std_dev = 15
normal_sample = np.random.normal(loc=mean, scale=std_dev, size=100)
normal_sample = np.clip(np.round(normal_sample), 1, 100).astype(int)

# Функция для вычисления p-value с помощью теста хи-квадрат
def chi_square_test(sample):
    # Фактические частоты
    observed = Counter(sample)
    observed_freq = [observed.get(i, 0) for i in range(1, 101)]
    
    # Ожидаемые частоты
    expected_freq = [100 / 100] * 100  # Нормируем на общее количество элементов
    
    # Выполнение теста хи-квадрат
    chi2_stat, p_value = stats.chisquare(observed_freq, expected_freq)
    return chi2_stat, p_value

# Вычисляем p-value для обеих выборок
uniform_chi2, uniform_p = chi_square_test(uniform_sample)
normal_chi2, normal_p = chi_square_test(normal_sample)

# Выводим результаты
print(f"p-value для выборки с равномерным распределением: {uniform_p:.6f}")
print(f"p-value для выборки с нормальным распределением: {normal_p:.6f}")