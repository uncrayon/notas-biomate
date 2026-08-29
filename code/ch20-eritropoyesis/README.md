# Capítulo 20: Estudio de Caso — Regulación de Eritropoyesis

Este directorio contiene el código numérico correspondiente al Ejercicio 6 del Capítulo 20 de las notas (estudio de caso clínico sobre la dinámica acoplada de eritrocitos y eritropoyetina EPO).

## Archivos

### 1. `eritropoyesis.py`
Integra el sistema dinámico bidimensional reducido:
$$\begin{aligned}
\frac{dC}{dt} &= H^* d_{\max} \frac{E}{K_d + E} - \gamma_C C \\
\frac{dE}{dt} &= \sigma_E e^{-C/D} - \gamma_E H^* E
\end{aligned}$$
El script calcula primero el estado de equilibrio $(C^*, E^*)$ por relajación libre, aplica una perturbación instantánea simulando una hemorragia aguda (reducción del 30% en la concentración de glóbulos rojos $C$), y rastrea la trayectoria temporal $C(t)$ para evaluar si el retorno al equilibrio presenta sobreimpulso (*overshoot*, régimen de foco estable) o recuperación monótona (nodo estable).

- **Cómo ejecutar**:
  ```bash
  python3 eritropoyesis.py
  ```
- **Salida esperada**:
  ```text
  C_eq=2.367  min=1.659  max=2.371  overshoot=True
  ```
