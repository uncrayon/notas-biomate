#!/usr/bin/env python3
"""
Simulación del modelo reducido 2D de regulación eritrocito-eritropoyetina (EPO)
y respuesta dinámica ante una hemorragia aguda (Ejercicio 6).

Referencia:
    Capítulo 20: Estudio de caso: del modelo completo a la reducción (Ejercicio 6)
    Notas de Matemáticas Biológicas - Sistemas Dinámicos No Lineales.
"""

import numpy as np

# Parámetros adimensionales (Hstar absorbido; escalas típicas)
gC, gE, Hs, sE, D, dmax, Kd = 0.30, 0.45, 1.0, 3.6, 2.0, 1.0, 1.0

def f(C, E):
    """Campo vectorial para la dinámica conjunta de glóbulos rojos (C) y EPO (E)."""
    dC = Hs*dmax*E/(Kd+E) - gC*C
    dE = sE*np.exp(-C/D)   - gE*Hs*E
    return dC, dE

# Equilibrio aproximado por relajación libre
C, E = 1.7, 1.6
dt = 0.01
for _ in range(20000):
    dC, dE = f(C, E)
    C, E = C + dt*dC, E + dt*dE
Ceq = C
C = 0.7*Ceq            # Hemorragia: -30 % en t0
traj = []
for k in range(60000):
    dC, dE = f(C, E)
    C, E = C + dt*dC, E + dt*dE
    traj.append(C)
traj = np.array(traj)
print(f"C_eq={Ceq:.3f}  min={traj.min():.3f}  "
      f"max={traj.max():.3f}  overshoot={traj.max()>Ceq*1.001}")

if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt

        # Visualización opcional de la recuperación post-hemorragia
        ts = np.arange(len(traj)) * dt
        plt.figure(figsize=(8, 4))
        plt.plot(ts, traj, label="Concentración de eritrocitos C(t)", color="tab:red")
        plt.axhline(Ceq, color="black", linestyle="--", alpha=0.7, label=f"Equilibrio $C^*={Ceq:.3f}$")
        plt.xlabel("Tiempo adimensional t")
        plt.ylabel("Eritrocitos C")
        plt.title("Respuesta dinámica post-hemorragia (Eritropoyesis 2D)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception:
        pass
