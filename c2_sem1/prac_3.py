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
    print(" ")
    
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

print(f"Определитель P: {det_P}")
print(f"Определитель L: {det_L}")
print(f"Определитель U: {det_U}")
print(f"Определитель A: {det_A}")


print("\n4: ")
uniform_sample = np.random.uniform(1, 101, size=100)
uniform_sample = np.round(uniform_sample).astype(int)

sample = np.random.normal(loc=50, scale=15, size=100)
normal_sample = np.clip(sample, 1, 101)
normal_sample = np.round(normal_sample).astype(int)

print("Выборка с равномерным распределением:")
print(*uniform_sample)
print("\nВыборка с нормальным распределением:")
print(*normal_sample)


print("\n5: ")
def compute_statistics(sample):
    stats_dict = {
        "Mean": np.mean(sample),
        "Mode": stats.mode(sample)[0],
        "Median": np.median(sample),
        "Min": np.min(sample),
        "Max": np.max(sample),
        "std_dev": np.std(sample, ddof=0)
    }
    return stats_dict

uniform_stats = compute_statistics(uniform_sample)
normal_stats = compute_statistics(normal_sample)

print("Статистические характеристики для выборки с равномерным распределением:")
for stat, value in uniform_stats.items():
    print(f"{stat}: {value}")

print("\nСтатистические характеристики для выборки с нормальным распределением:")
for stat, value in normal_stats.items():
    print(f"{stat}: {value}")


print("\n6: ")
np.random.seed(42)
uniform_sample = np.random.uniform(1, 101, size=100)

normal_sample = np.random.normal(loc=50, scale=15, size=100)
normal_sample = np.clip(np.round(normal_sample), 1, 100).astype(int)


def chi_square_test(sample):
    observed = Counter(sample)
    observed_freq = [observed.get(i, 0) for i in range(1, 101)]
    
    expected_freq = [100 / 100] * 100  
    
    chi2_stat, p_value = stats.chisquare(observed_freq, expected_freq)
    return chi2_stat, p_value

uniform_chi2, uniform_p = chi_square_test(uniform_sample)
normal_chi2, normal_p = chi_square_test(normal_sample)

print(f"p-value для выборки с равномерным распределением: {uniform_p:.6f}")
print(f"p-value для выборки с нормальным распределением: {normal_p:.6f}")