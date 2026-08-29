# Código de Simulación y Modelado

Este directorio contiene el código numérico y de simulación correspondiente a los modelos y ejercicios desarrollados en las **Notas de Matemáticas Biológicas: Sistemas Dinámicos No Lineales**.

## Índice de modelos

| Capítulo | Archivo | Descripción | Enlace |
| :--- | :--- | :--- | :--- |
| **Cap. 18: Lotka–Volterra y ciclos límites** | `lotka_volterra.py` | Integración numérica del modelo presa–depredador con Euler explícito. | [lotka_volterra.py](https://github.com/uncrayon/notas-biomate/blob/main/code/ch18-lotka-volterra/lotka_volterra.py) |
| **Cap. 18: Lotka–Volterra y ciclos límites** | `lotka_volterra_netlogo.nlogo` | Modelo basado en agentes (ABM) en NetLogo (presas y depredadores). | [lotka_volterra_netlogo.nlogo](https://github.com/uncrayon/notas-biomate/blob/main/code/ch18-lotka-volterra/lotka_volterra_netlogo.nlogo) |
| **Cap. 20: Estudio de caso (Eritropoyesis)** | `eritropoyesis.py` | Modelo 2D reducido de regulación eritrocito–EPO ante hemorragia aguda. | [eritropoyesis.py](https://github.com/uncrayon/notas-biomate/blob/main/code/ch20-eritropoyesis/eritropoyesis.py) |

## Requisitos de ejecución

- **Python 3**: requiere `numpy` (y opcionalmente `matplotlib` para visualizaciones).
- **NetLogo**: versión 6.x o superior (compatible también con NetLogo Web).
