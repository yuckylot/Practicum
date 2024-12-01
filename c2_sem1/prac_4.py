import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.sqrt(2 * x**3)

print("\n1:")
x = np.linspace(2, 4, 100)
for i in x:
    print(f"{i:.2f}", end=" ")
print("\n")
for i in x:
    print( f"f({i:.3f}):" , f(i))
print()

print("\n2:")
plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label="sqrt(2 * x**3)")
plt.title("График функции sqrt(2 * x**3)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("ln(x)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
print()

print("\n3:")
plt.figure(figsize=(8, 5))
plt.scatter(x, f(x), color=(0.5, 0.8, 0.2), label="Точки", marker="o")
plt.title("Точечный график функции sqrt(2 * x**3)", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("sqrt(2 * x**3)", fontsize=12)
plt.legend()
plt.grid(color=(0.1, 0.1, 0.1), linestyle="--", linewidth=0.5, alpha=1)
plt.show()
print()

print("\n4:")
uniform_sample = np.random.uniform(1, 101, size=100)
uniform_sample = np.round(uniform_sample).astype(int)

sample = np.random.normal(loc=50, scale=15, size=100)
normal_sample = np.clip(sample, 1, 101)
normal_sample = np.round(normal_sample).astype(int)

plt.figure(figsize=(12, 6))

plt.hist(
    uniform_sample,
    bins=15,
    color="skyblue",
    alpha=0.7,
    label="Равномерное распределение",
)
plt.hist(
    normal_sample,
    bins=30,
    color="salmon",
    alpha=0.7,
    label="Нормальное распределение"
)

plt.title("Гистограммы распределений", fontsize=16)
plt.xlabel("Значение", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.legend()
plt.show()
print()

print("\n5:")
sample = np.random.randint(1, 5, 50)
counts = np.bincount(sample)[1:]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(
    counts,
    labels=[str(i) for i in range(1, 5)],
    autopct="%1.1f%%",
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
plt.title("Круговая диаграмма распределения чисел")

plt.subplot(1, 2, 2)
plt.bar(range(1, 5), counts, color=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"])
plt.title("Столбчатая диаграмма распределения чисел")
plt.xlabel("Число")
plt.ylabel("Частота")

plt.tight_layout()
plt.show()
print()


# 6.
print("\n6:")
x_3d = np.linspace(2, 4, 100)
y_3d = np.linspace(2, 4, 100)
X, Y = np.meshgrid(x_3d, y_3d)
Z = np.log(X + Y) / np.log(np.e)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, color="cyan")
ax.set_title("3D График функции ln(x + y)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("ln(X + Y)")
plt.show()
print()


# 7.
print("\n7:")
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].plot(x, y, label="ln(x)", color="blue")
axs[0, 0].set_title("График функции ln(x)")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("ln(x)")
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].scatter(x, y, color=(0.5, 0.8, 0.2), label="Точки", marker="o")
axs[0, 1].set_title("Точечный график функции ln(x)")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("ln(x)")
axs[0, 1].legend()
axs[0, 1].set_facecolor("red")
axs[0, 1].grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)

axs[1, 0].pie(
    counts,
    labels=[str(i) for i in range(1, 5)],
    autopct="%1.1f%%",
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
axs[1, 0].set_title("Круговая диаграмма")

ax = fig.add_subplot(224, projection="3d")
ax.plot_surface(X, Y, Z, color="cyan")
ax.set_title("3D График функции ln(x + y)")

plt.suptitle("Сетка графиков", fontsize=18)
plt.show()
print()

# 8.
print("\n8:")
styles = ["ggplot", "classic", "dark_background"]
for style in styles:
    plt.style.use(style)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    axs[0, 0].plot(x, f(x), label="ln(x)", color="blue")
    axs[0, 1].scatter(x, f(x), color=(0.5, 0.8, 0.2), label="Точки", marker="o")
    axs[1, 0].pie(
        counts,
        labels=[str(i) for i in range(1, 5)],
        autopct="%1.1f%%",
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
    )
    axs[1, 1] = fig.add_subplot(224, projection="3d")
    axs[1, 1].plot_surface(X, Y, Z, color="cyan")

    plt.suptitle(f"Сетка графиков - Стиль: {style}", fontsize=18)
    plt.show()