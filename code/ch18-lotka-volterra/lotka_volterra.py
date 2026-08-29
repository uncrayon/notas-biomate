#!/usr/bin/env python3
"""
Simulación de Lotka-Volterra mediante integración numérica de Euler explícito.

Referencia:
    Capítulo 18: Modelo de Lotka-Volterra y ciclos límites (Sección 18.2)
    Notas de Matemáticas Biológicas - Sistemas Dinámicos No Lineales.
"""

import numpy as np

alpha, beta, gamma, delta = 1.0, 1.0, 1.0, 1.0

def lv(u, t):
    """Campo vectorial de Lotka-Volterra."""
    x, y = u
    return np.array([alpha*x - beta*x*y,
                     -gamma*y + delta*x*y])

dt, T = 0.01, 20.0        # paso temporal y horizonte
u = np.array([1.2, 0.6])  # condición inicial
for t in np.arange(0, T, dt):
    u = u + dt * lv(u, t)
print(f"estado final: x = {u[0]:.3f}, y = {u[1]:.3f}")

if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt

        # Visualización opcional de la serie temporal
        ts = np.arange(0, T, dt)
        trajectory = []
        u_sim = np.array([1.2, 0.6])
        for t in ts:
            trajectory.append(u_sim.copy())
            u_sim = u_sim + dt * lv(u_sim, t)
        traj_arr = np.array(trajectory)

        plt.figure(figsize=(8, 4))
        plt.plot(ts, traj_arr[:, 0], label="Presas (x)", color="green")
        plt.plot(ts, traj_arr[:, 1], label="Depredadores (y)", color="red")
        plt.xlabel("Tiempo t")
        plt.ylabel("Población")
        plt.title("Modelo de Lotka-Volterra (Euler explícito)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception:
        pass
