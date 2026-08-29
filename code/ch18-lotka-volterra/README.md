# Capítulo 18: Lotka–Volterra y Ciclos Límites

Este directorio contiene las implementaciones computacionales del modelo presa–depredador de Lotka–Volterra descritas en la Sección 18.2 de las notas.

## Archivos

### 1. `lotka_volterra.py`
Implementa la integración numérica directa del sistema continuo de ecuaciones diferenciales ordinarias:
$$\begin{aligned}
\frac{dx}{dt} &= \alpha x - \beta x y \\
\frac{dy}{dt} &= -\gamma y + \delta x y
\end{aligned}$$
utilizando el método de Euler explícito con parámetros $\alpha=\beta=\gamma=\delta=1$, condición inicial $(x_0, y_0) = (1.2, 0.6)$, paso $\Delta t = 0.01$ y horizonte $T=20.0$.

- **Cómo ejecutar**:
  ```bash
  python3 lotka_volterra.py
  ```
- **Salida esperada**:
  ```text
  estado final: x = 1.562, y = 0.741
  ```

### 2. `lotka_volterra_netlogo.nlogo`
Modelo basado en agentes (ABM) en NetLogo donde presas (verdes) y depredadores (rojos) interactúan en un espacio discreto 2D con reglas individuales de movimiento, consumo de energía y persecución de presas cercanas.

- **Cómo ejecutar**:
  Abrir el archivo `lotka_volterra_netlogo.nlogo` en [NetLogo Desktop](https://ccl.northwestern.edu/netlogo/) o cargarlo en [NetLogo Web](https://www.netlogoweb.org/). Presionar el botón `setup` para inicializar el mundo y `go` para iniciar la simulación continua.
