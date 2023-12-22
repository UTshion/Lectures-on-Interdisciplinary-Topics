import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

INTERVAL = 0.05  # [s] インターバル
FRAME_INTERVAL = 1000 * INTERVAL  # [msec] フレーム間のインターバル
FPS = 1000 / FRAME_INTERVAL  # FPSの設定

Nt = 10000
N = 40
L = 80
c = 2.0
a = 1.3
dx = L / N

tmin = 0.0
tmax = 500.0

t0 = 0
dt = (tmax - tmin) / Nt

t = np.linspace(0, tmax, Nt)
x0 = np.empty(N * 2)

# 新しい変数 road_condition をランダムに初期化
road_condition = np.random.rand(N)

# 新しい変数の影響を調整する係数
damping_coefficient = 0.1

# 弧度法を用いて環状道路を100区間に分割するため、thetaを設定
theta = np.linspace(0, 2 * np.pi, 100)


def Velocity(x):
    return np.tanh(x - 2) + np.tanh(2)


p = 0
for i in range(N):
    x0[i] = p
    x0[N + i] = Velocity(p)
    p += dx
    p += 0.01 * (np.random.uniform(0, 1) - 0.5)

sol = np.empty((Nt, N * 2))
sol[0] = x0


def ov_model(t, x, road_condition):
    f = np.zeros(N * 2)

    for i in range(N):
        f[i] = x[N + i]
        if i < N - 1:
            d = x[i + 1] - x[i]
        else:
            d = x[0] - x[i]

        if d > L:
            d -= L

        if d < 0:
            d += L

        # 新しい変数 road_condition を用いて damping term を設定
        damping_term = damping_coefficient * road_condition[i]

        f[N + i] = a * (Velocity(d) - x[N + i]) - damping_term

        # damping_term を0から1の範囲に制約
        damping_term = np.clip(damping_term, 0, 1)

    return f, damping_term


solver = ode(ov_model)
solver.set_integrator("dop853")
solver.set_initial_value(x0, t0)

# ode オブジェクトに road_condition 属性を追加
solver.set_f_params(road_condition)

k = 1
while solver.successful() and solver.t < tmax:
    # ループ内で damping_term を計算する前に制約をかける
    road_condition_clipped = np.clip(road_condition, 0, 1)
    solver.set_f_params(road_condition_clipped)

    solver.integrate(t[k])

    sol[k] = solver.y
    for i in range(N):
        if sol[k, i] > L:
            sol[k, i] -= L
    k += 1


def update(i):
    plt.cla()
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)
    plt.plot(np.cos(theta), np.sin(theta), c="Black", alpha=0.2)

    # 各点をプロット
    traj_x = np.cos(2 * np.pi * sol[i, 0:N] / L)
    traj_y = np.sin(2 * np.pi * sol[i, 0:N] / L)
    scatter = plt.scatter(traj_x, traj_y, c="Red")

    # 各点がなす軌跡をプロット
    for j in range(N - 1):
        plt.plot(
            [traj_x[j], traj_x[j + 1]], [traj_y[j], traj_y[j + 1]], c="blue", alpha=0.5
        )

    # 始点と終点を結んで軌跡をつなぐ
    plt.plot([traj_x[-1], traj_x[0]], [traj_y[-1], traj_y[0]], c="blue", alpha=0.5)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("OV model with Randomized Road Condition")

    # 下部に damping_term の値を表示
    _, damping_term = ov_model(0, sol[i], road_condition)
    plt.text(
        0,
        -1.3,
        f"Damping Term: {damping_term:.3f}",
        horizontalalignment="center",
        verticalalignment="center",
    )

    return (scatter,)


# プロット
fig = plt.figure(figsize=(8, 8))
ani = FuncAnimation(
    fig, update, frames=range(0, Nt, 15), interval=FRAME_INTERVAL, blit=True
)
plt.show()
