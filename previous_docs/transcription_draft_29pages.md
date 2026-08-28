# Biomate notes draft — transcription of notes_drafts_biomate_1.pdf

## Page 1

### Clase 1

#### Sobre la evaluación:

Recuerden que hay Mini Proyectos, mini labs & Proyectos Finales, el proyecto final es para ca. el último cuarto del semestre (más o menos el último mes). Los minis son largos & usualmente se dan 15 días para hacerlo. Los Mini Labs son opcionales, pero bien útiles si los quieren para perderle el miedo a la programación.

Ahora, yo califico todo, sé que se copian. La verdad es que los problemas los desarrolle yo entonces sé que es muy probable que para la gran mayoría no estén las soluciones en internet. Ahora bien, sé que pueden & van a copiar, no me molesta, pero lo que sí me molesta es no ver la cita al trabajo de la otra persona, el plagio sí es un problema para mí. Entonces, si copian, escríbanlo, no voy a penalizarlos pero sí si no dan los créditos correspondientes.

**NOTA:** Lo que sí no voy a aceptar es que me pongan una foto del trabajo de la otra persona. Creo que al menos, usando sus propias manos para escribirlo / typearlo hace que aprendan algo.

---

## Page 2

### Sobre el temario

Estos cursos son complicados pues requieren muchos precedentes en particular EDOs y Álgebra lineal, también cálculo, especialmente dibujar curvas y un poco/mucho de pensamiento geométrico.

Si han llevado materias de otras carreras ó estudiado algo de transdisciplina / multidisciplina más o menos ya se van a saber este juego. Si quieren aprender a como jugar un poco con las herramientas que nos brindan las matemáticas y la modelación se van a divertir.

Es una materia que, va a parecer trivial, pero que si la dejan & no le presten atención les puede dar una sorpresa por las sutilezas. No va a parecer un curso de matemáticas en el sentido estándar pues no habrá mucho de demostración-teorema-corolario sino usaremos ciertos resultados para poder avanzar. Hay que usar mucha intuición, pensamiento geométrico y dibujos.

Lo primero que vamos a trabajar y repasar es sistemas dinámicos no-lineales. Para esto vemos con un poco de historia:

---

## Page 3

### Historical Overview

- **1666 Newton** — Cálculo, Órbitas (Kepler: Elipses), Planetas, Leyes de la óptica, Problema de 2-cuerpos.
  - $\hookrightarrow$ ¿Qué pasa con 3-Planetas, N-Planetas?

> "Ningún Problema me ha hecho doler tanto la cabeza como el problema de el Sol-Tierra-Luna" *(problema de la Luna)* — Carta a Halley.

- **$\sim 200$ AÑOS** Euler, Gauss fallan.
- **Finales de 1800:** Poincaré, demuestra / da argumentos de la dificultad de poder encontrar una forma cerrada.
  - $\hookrightarrow$ Se introduce la idea del plano fase.
  - $\hookrightarrow$ Sus ideas son lo que ahora llamamos **caos**.

**CAOS:** Comportamiento aperiódico en un sistema determinista que exhibe "sensibilidad a condiciones iniciales".

**FACT:** Poincaré era terrible dibujando, tan terrible que en los exámenes de ingreso en la prueba de dibujo mecánico sacó un 0. Sin embargo su aproximación a los sistemas era muy visual, muy geométrica. A pesar de que en sus artículos no dibujaba nada, pero describía cosas. Al no dibujar sus trabajos pasaron desapercibidos.

---

## Page 4

- Además de todo, sus trabajos pasaron un poco desapercibidos pues la acción no estaba en la mecánica clásica en la época sino en la mecánica cuántica, la relatividad.
- (1939–1941 — WWII)
- **1920s – 1950s:** Non linear oscillators (Physics & Engineering)
  - $\hookrightarrow$ Radio – Vacuum tube (Diodes) – Non linear oscillator
  - radars
  - Lasers.
  - phase locked loops

[FIGURE: Block diagram of a Phase Locked Loop (PLL): input signal $v_i \rightarrow [\Phi \text{ phase comparator}] \rightarrow [\text{loop filter}] \rightarrow [\text{VCO}] \rightarrow v_o$, with feedback loop returning from output $v_o$ into the phase comparator.]

- **1950:** Computer invented. (War motivated).
- **1954:** Artículo de Lanchester.
- **1957:** Sputnik 1
- **1960's:** Lorenz @ MIT (mat & meteorologist).
  - $\hookrightarrow$ Chaotic systems on a model of convection in the atmosphere
  - He was interested on weather forecasting, while simplifying the system found this behavior
- **1963** "Deterministic non-periodic flow".
  - $\hookrightarrow$ Desde este artículo se debió iniciar la revolución del caos pero fue ignorado.
  - Partly because it was published on a meteorology journal *"The Journal of the Atmospheric Sciences"* (no mathematicians read this) & the physicists thought it was a ridiculous model.

---

## Page 5

- Also there is a work by Smale
- KAM (Kolmogorov-Arnold-Moser)
  - $\hookrightarrow$ Very mathematical course
- **1975 • Bob May** (Pop. biologist): Chaos in iterated maps
  $$x_{n+1} = f(x_n)$$
  - $\hookrightarrow$ 1976 "Simple Mathematical Models with very complicated Dynamics" was published on *Nature*.
  - $\hookrightarrow$ **NEW MATHEMATICS**
  - Evangelical Plea: Stop teaching only linear mathematics. *"Si permitimos a los sistemas ser no-lineales es donde aparece la magia"*.
- Logistic Eqn in population biology.
- **Mandelbrot:** Fractals — Very obsessed with the forms in nature.
- **Winfree:** Non-linear oscillators in biology.
  - $\hookrightarrow$ topology $\longrightarrow$ in biology
- **Ruelle & Takens:** Llevaron el caos al problema de la turbulencia & Navier-Stokes.
  - ¿Es la turbulencia una forma de caos? ¿Son lo mismo?

---

## Page 6

- **$\sim 1978$ Feigenbaum (Physicist)**
  - $\hookrightarrow$ Vió conexiones entre el mapeo logístico [...] y trabajando en la teoría de caos
  - "Universal route to chaos" — How to progress to chaos.
  - Renormalization group & phase transitions in statistical physics.
- **$\sim 1980$s — Chaos, non-linear dynamics, fractals HOT!**
  - **1987** — *Chaos: Making a New Science* — James Gleick
    - a way to take the mathematics to the general public / Best sellers
    - $\downarrow$ Tazas & playeras
    - $\downarrow$ **1993** — *Jurassic Park* / "La mariposa"
    - $\dots$ *"Es difícil de explicar que va a pasar con los dinos."*
  - Experimental confirmation of chaos theory.
- **$\sim 1990$s — Engineering Application of Chaos**
  - $\hookrightarrow$ Encoding signals,
  - $\hookrightarrow$ Complex systems.
  - Statistical Physics $\pm$ Classical Mechanics

---

## Page 7

- **Fun Fact:** Tiene que ver con órbitas y misiones espaciales... incluso se usó el conocimiento de la mecánica N-cuerpos para mover a un satélite que orbitaba el sol para caer en un cometa: ISEE-3 (International Sun-Earth Explorer 3)
  - 1985 Giacobini-Zinner / ICE (International Comet Explorer).

---

### Logical Structure of dynamics (De lo que cambia respecto a algo)

**D.E.** $\bar{x}' = \bar{F}(\bar{x})$, where $\bar{x} \in \mathbb{R}^n$, $F: \mathbb{R}^n \rightarrow \mathbb{R}^n$, $\mathbb{R}^n$: Phase Space.

$$\begin{aligned}
x_1' &= f_1(x_1, x_2, x_3, \dots, x_n) \\
&\;\;\vdots \\
x_n' &= f_n(x_1, x_2, x_3, \dots, x_n)
\end{aligned}$$

Decimos que un sistema es lineal si todos los $x_i$ en el lado derecho son productos de primer orden.

$$x_i^2, \quad x_i x_j, \quad \sin(x_i) \longrightarrow \text{No-lineal.}$$

---

## Page 8

### Simple Examples

- $m\ddot{x} + kx = 0$ [oscilador armónico $\dots$ sistema lineal de segundo orden]
- $\ddot{x} + \sin(x) = 0 \implies \begin{cases} \dot{x} = v \\ \dot{v} = -\sin(x) \end{cases} \longrightarrow$ Sistema no-lineal de segundo orden (péndulo).

### Poincaré idea

[FIGURE: Two phase portrait sketches in $(x, v)$ state space. Left: Concentric circular/elliptical orbits centered at $(0,0)$ representing the harmonic oscillator. Right: Nonlinear pendulum phase portrait showing nested closed orbits (librations) centered at stable equilibria, separating curves (separatrices) with saddle points, and wavy open trajectories (rotations) labeled "Solución".]

Solución $(x(t), v(t)) \longrightarrow$ punto moviéndose en una trayectoria en el espacio $x-v$ (Kinda — Es una parametrización de la curva).

> "Cómo se verán las soluciones sin resolver el problema, sin encontrar una solución explícita".

**Retrato Fase** $\equiv$ Una imagen de todas las posibles trayectorias diferentes, se encuentran sin resolver analíticamente los sistemas.

---

## Page 9

### Hands-on Example

Pensemos en 1D systems: $\dot{x} = f(x)$

La idea geométrica es un flujo en una línea.

Pensemos en el sistema:

$$\dot{x} = ax, \quad x_0 = x(t=0)$$

Si queremos resolver analíticamente entonces proponemos:

$$\frac{dx}{dt} = ax \implies \frac{1}{x}\frac{dx}{dt} = a$$

$$\implies \int \frac{1}{x}\frac{dx}{dt} dt = \int a dt$$

$$\hat{x} = x, \quad d\hat{x} = \frac{dx}{dt}dt \implies \int \frac{1}{x}\frac{dx}{dt}dt = \int \frac{1}{\hat{x}} d\hat{x} = \ln(\hat{x})$$

$$\implies \ln(x) = \int \frac{1}{x}\frac{dx}{dt} dt = \int a dt = at + \text{cte.}$$

$$\implies \ln(x) = at + \text{cte.} \implies x(t) = e^{at + \text{cte.}} = k e^{at} \quad \text{[Solución general]}$$

$$\implies x(0) = x_0 \implies k e^{a \cdot 0} = x_0 \implies k = x_0$$

$$\implies x(t) = x_0 e^{at} \longrightarrow \text{Solución particular.}$$

¿Qué nos dice esto del sistema?

[FIGURE: Graph of $f(x)$ vs $x$, showing a straight line through the origin with slope $a$. Along the $x$-axis, arrows point outward away from the origin, illustrating an unstable fixed point at $x=0$. Annotations indicate "Derivada" and "La derivada siempre crece / decrece".]

---

## Page 10

Hagamos un ejemplo más loco:

$$x' = \sin(x), \quad x_0 = x(t=0)$$

$$\frac{dx}{dt} = \sin(x) \implies \int \frac{1}{\sin(x)}\frac{dx}{dt} dt = \int dt = t + \text{cte}$$

$$\implies \int \frac{1}{\sin(\hat{x})} d\hat{x} = \int dt; \quad \frac{1}{\sin(x)} = \csc(x)$$

$$\implies \int \csc(\hat{x}) d\hat{x} = -\ln|\csc(x) + \cot(x)|$$

$$\implies -\ln|\csc(x) + \cot(x)| = t + \text{cte} \longrightarrow \text{Solución general.}$$

$$t=0 \to x = x_0$$

$$\implies t = \ln\left| \frac{\csc(x_0) + \cot(x_0)}{\csc(x) + \cot(x)} \right| \quad (?)$$

- ¿Qué pasa si $x_0 = \pi/4$? ¿Cuál es el comportamiento $t \to \infty$?
- ¿Qué pasa con $x_0 = \pi$?

[FIGURE: Plot of $f(x) = \sin(x)$ vs $x$ over the range $[-2\pi, 2\pi]$. The $x$-axis shows equilibria at multiples of $\pi$: $x^* = \pi, x^* = n\pi$ (zero velocity). In $(0, \pi)$, $f(x) > 0$ ("Positive velocity", rightward arrow $\rightarrow$). In $(\pi, 2\pi)$, $f(x) < 0$ ("Negative velocity", leftward arrow $\leftarrow$). Fixed point at $0$ is unstable (repellor), fixed point at $\pi$ is stable (attractor).]

If $x_0 = \pi/4$, then $x \to \pi$ as $t \to \infty$.

[FIGURE: Graph of $x(t)$ vs $t$ showing an S-shaped trajectory starting at $x(0) = \pi/4$ at $t=0$, passing through inflection around $\pi/2$, and asymptotically leveling off at the horizontal asymptote $x = \pi$.]

---

## Page 11

### One dimensional Flows

We know that the systems are of the form:

$$\vec{x}' = \bar{F}(\bar{x}) \quad \begin{cases} \dot{x}_1 = f_1(x_1, x_2, x_3, \dots, x_n) \\ \;\;\vdots \\ \dot{x}_n = f_n(x_1, x_2, \dots, x_n) \end{cases}$$

If we limit ourselves to 1D then we are on the terrain of first order system / 1D sys.

#### NOTE:
1. I use system in the sense of dynamical systems, not in the classical sense of equations systems, thus a single equation could be a "system".
2. We won't allow to depend $f$ explicitly on the time. "Non-autonomous" equations or time-dependent of the form $\dot{x} = f(x,t)$ are more complicated because they need two pieces of information "$x$ & $t$", thus $\dot{x} = f(x,t)$ should be regarded as two dimensional system or second order.

---

## Page 12

### Fixed Points & stability

The ideas of the last section/class could be extended to any one-dimensional system $\dot{x} = f(x)$.

[FIGURE: Four examples comparing $f(x)$ vs $x$ plots with their corresponding 1D vertical phase lines:
1. Upward parabola crossing at $a$ and $b$: phase line shows flow into $a$ (Stable) and away from $b$ (Inestable).
2. Function crossing at $a$, touching/tangent at $b$, and crossing at $c$: phase line shows $a$ is Stable, $b$ is a half-stable Node, and $c$ is Inestable.
3. Linear function with negative slope crossing at $a$: phase line shows flow converging to $a$ (Stable).
4. Linear function with positive slope crossing at $a$: phase line shows flow diverging from $a$ (Inestable).]

---

## Page 13

Let's notice that if the system $x' = f(x)$, we say that the equilibrium point is defined as any $x^*$ s.t.:

$$\boxed{f(x^*) = 0}$$

Then also we could define stability (in the sense of Lyapunov) as:

1. $x^*$ is said to be **stable** if for every $\varepsilon > 0$ $\exists\ \delta > 0$ such that if $\|x(0) - x^*\| < \delta$ then $\forall t \ge 0$ we have $\|x(t) - x^*\| < \varepsilon$.
   So basically if the solution starts "close enough" to the equilibrium, remains "close enough" forever.

[FIGURE: Lyapunov stability diagram showing an inner $\delta$-neighborhood centered at equilibrium point $x^*$ containing initial point $x_0$, surrounded by an outer $\varepsilon$-neighborhood. Trajectory $\phi(t, x_0)$ remains bounded within the $\varepsilon$-neighborhood for all future time.]

2. $x^*$ is said to be **asymptotically stable** if it's Lyapunov stable & $\exists\ \delta > 0$ such that if $\|x(0) - x^*\| < \delta$ then:

$$\lim_{t \to \infty} \|x(t) - x^*\| = 0$$

Basically means that solutions that start close enough not only remain close enough forever but also converge to the equilibrium.

[FIGURE: Asymptotic stability diagram showing a trajectory $\phi_{x_0}(t)$ starting at $x_0$ within a neighborhood of $x^*$ and spiraling/converging directly into $x^*$.]

- $\hookrightarrow$ What about the time? Converges linearly, polynomially, exp, etc.

---

## Page 14

Consider the electrical circuit. A resistor $R$ and a capacitor $C$ are in series with battery of constant voltage $V_0$ (DC).

Suppose the switch is close at $t=0$, and there is no charge in capacitor initially. Let $Q(t)$ denote the charge on the capacitor at time $t \ge 0$.

$$Q = CV \implies \dot{Q} = I$$

[FIGURE: Electric circuit schematic diagram consisting of a constant DC voltage source $V_0$, a switch closed at $t=0$, a resistor $R$, and a capacitor $C$ in series with ground, with current loop $I$.]

$$V_0 = \frac{Q}{C} + RI = \frac{Q}{C} + R\dot{Q}$$

$$R\dot{Q} + \frac{Q}{C} - V_0 = 0$$

$$\dot{Q} = f(Q) = \frac{V_0}{R} - \frac{Q}{RC}$$

¿$\dot{Q} = 0$? $Q^*$?

$$Q^* = CV_0$$

[FIGURE: Phase line plot of $\dot{Q} = f(Q)$ vs $Q$ with vertical intercept $V_0/R$ and negative slope $-1/(RC)$, crossing the axis at equilibrium $Q^* = CV_0$. Inward arrows indicate monotonic convergence to $Q^*$.]

[FIGURE: Trajectories $Q(t)$ vs $t$ exponentially approaching the horizontal asymptote $Q = CV_0$ from both above and below.]

- $\dot{Q}$ decreases linearly as $Q(t)$ approaches the fixed point.

---

## Page 15

### EXAMPLE

Sketch the phase portrait of $x' = x - \cos x$ and determine the stability of all the fixed points.

**SOL:** We could draw the graph $x - \cos x$ but we depend into looking what $x - \cos x$ looks like. There is an easier solution, which exploits the fact that we know how to graph $y = x$ & $y = \cos x$.

Let's notice that:

$$x^* - \cos x^* = 0 \implies x^* = \cos x^* \implies f(x^*) = 0$$

[FIGURE: Simultaneous plot of the line $y = x$ and the curve $y = \cos x$, intersecting at a single root $x^*$. Below, a 1D phase line along the $x$-axis shows arrows pointing left ($\leftarrow$) for $x < x^*$ where $x < \cos x \implies x - \cos x < 0$, and arrows pointing right ($\rightarrow$) for $x > x^*$ where $x > \cos x \implies x - \cos x > 0$. The fixed point $x^*$ is thus unstable.]

Now if $x > \cos(x)$ then $x - \cos(x) > 0$.
$x < \cos(x) \implies x - \cos(x) < 0$.

We have the stability without finding the explicit equation.

---

## Page 16

### Popn Growth

The simplest model we could talk of is $N' = rN$, where $N(t)$ is the population at time $t$, and $r$ is the growth rate ($r > 0$).

$$N' = \frac{dN}{dt} = rN \implies \int \frac{1}{N}\frac{dN}{dt} dt = \int r dt$$

$$\implies \int \frac{1}{N}\frac{dN}{dt} dt = \int \frac{1}{\hat{N}} d\hat{N} = \ln(\hat{N}) = rt + \text{cte}$$

where $\hat{N} = N$, $\frac{d\hat{N}}{dt} dt = d\hat{N}$.

$$\implies \hat{N}(t) = N(t) = e^{(\text{cte} + rt)} = e^{\text{cte}} e^{rt} = N_0 e^{rt}$$

Notice that $N(t=0) = N_0$.

$$\left[\frac{N'}{N} = r\right] \longrightarrow \text{Growth rate per capita const.}$$

[FIGURE: Graph of $N'$ vs $N$ showing a straight line with slope $r > 0$ passing through origin, with arrows pointing outward along the $N$-axis representing unstable exponential growth.]

[FIGURE: Plot of per capita growth rate $N'/N$ vs $N$ as a flat horizontal line at constant height $r$.]

We know that the popn. starts to fight for resources when there is over crowd population. Let's understand resources as something big.

[FIGURE: Plot of per capita growth rate $N'/N$ vs $N$ with negative slope $-r/K$, vertical intercept $r$, and horizontal intercept at carrying capacity $K$: $\frac{N'}{N} = r - \frac{rN}{K}$.]

$$\implies N' = rN\left(1 - \frac{N}{K}\right)$$

[FIGURE: Plot of $N'$ vs $N$ showing an inverted downward-opening parabola with roots at $N=0$ and $N=K$, and peak at $K/2$. Phase arrows along the $N$-axis point away from $N=0$ (unstable repellor) and converge into $N=K$ from both left and right (stable attractor).]

---

## Page 17

[FIGURE: Family of logistic trajectory curves $N(t)$ vs $t$ starting from different initial population values $N_0$, all sigmoidally or asymptotically converging toward the carrying capacity asymptote $N = K$.]

This is a metaphor!

- **Krebs (1972, pp. 190–200)** $\longrightarrow$ bacteria, yeast $\longrightarrow$ cajas Petri.
- **Krebs (1972)** — Fruit Flies, escarabajos $\longrightarrow$ eggs $\longrightarrow$ larvae $\longrightarrow$ pupae $\longrightarrow$ adults.
- Fluctuations due to age-structure and time delayed effects of overcrowding pop.n $\longrightarrow$ Many eggs dont affect one short time.

---

### Linear Stability Analysis

Let $\dot{x} = f(x)$ be our system, and let $x^*$ a point such that $f(x^*) = 0$.

and let $\eta(t) = x(t) - x^*$ a small perturbation away from $x^*$. Let's measure if the perturbation gets closer or goes away.

$$\eta'(t) = (x(t) - x^*)' = \dot{x} \implies \eta' = \dot{x} = f(x) = f(x^* + \eta)$$

Taylor expansion:

$$f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots$$

---

## Page 18

$$f(x^* + \eta) = f(x^*) + f'(x^*)(x - x^*) + \mathcal{O}(\eta^2)$$

where $\|x^* - x(t)\| < \varepsilon \ll 1$.

$$= f(x^*) + \eta f'(x^*) + \mathcal{O}(\eta^2)$$

(since $f(x^*) = 0$ and $\mathcal{O}(\eta^2) \to 0$)

$$f(x^* + \eta) = \eta f'(x^*) + \mathcal{O}(\eta^2)$$

Now, if $f'(x^*) \neq 0$ and $\mathcal{O}(\eta^2)$ son despreciables:

$$\eta' \approx \eta f'(x^*) \longrightarrow \text{linearization about } x^*$$

This means that a perturbation grows exponentially if $f'(x^*) > 0$ and decays if $f'(x^*) < 0$. If $f'(x^*) = 0$ then we cannot ignore $\mathcal{O}(\eta^2)$ terms and we need to perform non-linear analysis to determine stability.

**NOTICE THAT NOW** we can KNOW HOW stable/unstable a point $x^*$ is. This is quantified on the value $f'(x^*)$ (Not only the sign is important). Also notice that $1/|f'(x^*)|$ is called "characteristic time scale" and it's basically the required time required for $x(t)$ to vary significantly around $x^*$.

---

## Page 19

### Example
Determine the stability & fixed points of $x' = \sin x$.

**SOL:**

$$x' = f(x) = \sin x = 0 \implies x_k^* = k\pi, \quad k \in \mathbb{Z}$$

$$f'(x) = \cos(x)$$

$$f'(x_k^*) = \begin{cases} 1 & \text{if } k \text{ is even} \longrightarrow \text{Unstable} \\ -1 & \text{if } k \text{ is odd} \longrightarrow \text{Stable} \end{cases}$$

[FIGURE: Plot of $f(x) = \sin x$ vs $x$ over the range $[0, 2\pi]$. Equilibrium points at $x=0$ and $x=2\pi$ are unstable (open circles with outward arrows), while $x=\pi$ is stable (filled circle with inward arrows).]

---

### Ex. Find the eq. points using from Logistic:

$$N' = rN\left(1 - \frac{N}{K}\right), \quad (r > 0)$$

Notice that $f(N) = rN\left(1 - \frac{N}{K}\right)$ and $f'(N) = r - \frac{2rN}{K}$.

$$rN\left(1 - \frac{N}{K}\right) = 0 \iff N_1^* = 0, \quad N_2^* = K$$

$$f'(0) = r > 0 \implies \text{UNSTABLE}$$

$$f'(K) = -r < 0 \implies \text{STABLE}$$

$$\frac{1}{|f'(N_i^*)|} = \frac{1}{r}$$

[FIGURE: Graph of $f(N)$ vs $N$ downward-opening parabola with roots at $0$ (unstable) and $K$ (stable). Below, a plot shows the characteristic exponential decay curve toward equilibrium.]

---

## Page 20

### Ex. ¿Qué podemos decir sobre $f'(x^*) = 0$?

- $x' = -x^3$
  [FIGURE: Plot of $x' = -x^3$ vs $x$ passing through origin. Inward phase arrows $\rightarrow \bullet \leftarrow$ indicate origin is Stable.]
- $x' = x^3$
  [FIGURE: Plot of $x' = x^3$ vs $x$ passing through origin. Outward phase arrows $\leftarrow \bullet \rightarrow$ indicate origin is Unstable.]
- $x' = x^2$
  [FIGURE: Plot of $x' = x^2$ vs $x$ touching origin from above. Phase arrows $\rightarrow \bullet \rightarrow$ indicate origin is Half-stable / Node.]
- $x' = k$
  [FIGURE: Horizontal line $x' = k$.]

$f'(x^*) = 0$ does not mean that is a node.

---

### IMPOSSIBILITY OF OSCILLATIONS

Notice that by now the solution tends to an accumulation point or goes to $\pm\infty$. The reason is that the solutions are forced to increase or decrease monotonically (or remains constant). What does this means? The phase point never reversals the direction. This means that damped/overshoot osc. could never occur.

[FIGURE: Crossed-out sketch of a damped oscillatory waveform.]

**HENCE THERE ARE NO PERIODIC SOLUTIONS.**

**LETS REMEMBER THAT WE ARE ON A STRAIGHT LINE (FLOW). THE FLOW COULD NOT RETURN SUDDENLY!**

---

## Page 21

- NOTICE THAT WE COULD FLOW ON CIR...

### EXAMPLE: Mechanical Analogy

Notice that spring force $F(x) = m\ddot{x} + b\dot{x}$.

$$\text{if } b\dot{x} \gg m\ddot{x} \implies F(x) = b\dot{x} \longrightarrow \frac{1}{b}F(x) = \dot{x} = f(x)$$

[FIGURE: Schematic diagram of an overdamped mechanical system: a mass $m$ attached to a spring inside a container of high-viscosity fluid labeled "HONEY", with initial position $x_0$ and applied external force $F(x)$.]

---

### Potentials

There is a way to visualize how the systems behave based on the physical idea of potential energy.

$$\text{potential } V(x): \quad f(x) = -\frac{dV}{dx}$$

$$V(x) := V(x(t))$$

[FIGURE: Potential energy landscape curve $V(x)$ showing valleys and hills with a ball rolling down toward the bottom of the potential well.]

$$V' = \frac{dV}{dt} = \frac{dV}{dx}\frac{dx}{dt} = -\left(\frac{dV}{dx}\right)^2 \le 0$$

$\hookrightarrow V(t)$ DECREASES along trajectories, i.e. in particular always moves towards the lower potential. Notice that local minima of $V(x)$ are stable points, maximum are unstable points.

$$\dot{x} = -x \implies -\frac{dV}{dx} = -x$$

$$\dot{x} = x - x^3 \implies -\frac{dV}{dx} = x - x^3$$

---

## Page 22

# BIFURCATIONS

[FIGURE: Sketches illustrating mechanical buckling: an upright signpost versus a signpost buckling/bending sideways under an applied critical load.]

### BIF. SADDLE - NODE

$$x' = r + x^2$$

[FIGURE: Three phase portrait plots for $x' = r + x^2$:
- $r < 0$: two fixed points $x^* = \pm\sqrt{-r}$ (left is stable, right is unstable).
- $r = 0$: single half-stable fixed point at $x = 0$.
- $r > 0$: no fixed points; positive velocity everywhere to the right.]

[FIGURE: Bifurcation diagram on the $(r, x^*)$ plane: a parabola opening to the left $r = -(x^*)^2$. The upper branch is unstable (dashed line, labeled UNST), the lower branch is stable (solid line, labeled STB), meeting at the saddle-node bifurcation point $(0,0)$. Labeled "Bifurcation Diagram".]

$$\pm\sqrt{-r}$$

**blue sky bifurcation** — Abraham & Shaw '88
> "out of the clear blue sky a pair of fixed points appear"

$$\therefore x' = r - x^2$$

- $r < 0 \longrightarrow \text{NO EQ. P.}$
- $r = 0 \longrightarrow 1$
- $r > 0 \longrightarrow \text{Two of them}$

---

### EXAMPLE

$$x' = r - x - e^{-x}$$

$$r - x - e^{-x} = 0 \implies r - x = e^{-x} \quad \text{Also find derivative}$$

$$\frac{d}{dx}(r - x) = \frac{d}{dx}(e^{-x}) \implies -e^{-x} = -1 \implies x^* = 0 \implies r_c = 1$$

[FIGURE: Graphical solution showing the intersection of the straight line $y = r-x$ and the curve $y = e^{-x}$. Left: for $r > 1$, there are two intersections (one stable, one unstable). Right: for $r = r_c = 1$, the line is tangent to the exponential curve at $x^* = 0$.]

---

## Page 23

### Formas normales / Normal forms

In some way the family $x' = r \pm x^2$ are representative of **all** saddle-node bifurcations. We call them then "prototypical" and the main idea is that near enough to the eq. point in the range of the bifurcation, then it looks like $x' = r \pm x^2$.

Let's consider our last example:

$x' = r - x - e^{-x}$, let's remember that the Taylor series around a point $a$ is:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots$$

[NOTE: $a=0 \implies$ Maclaurin series]

$$e^{-x} = e^{-a}\left[1 + (-(x-a)) + \frac{1}{2}(x-a)^2 + \frac{1}{6}(-(x-a))^3 + \cdots\right]$$

At $a=0$:

$$e^{-x} = \left(1 - x + \frac{x^2}{2} + \cdots\right)$$

Then if we take our system and expand around $x=0$ (which is the Eq. P. around $r=1$):

$$\begin{aligned}
x' = r - x - e^{-x} &\approx r - x - \left[1 - x + \frac{x^2}{2} + \mathcal{O}(x^3)\right] \\
&\approx (r-1) + x - x - \frac{x^2}{2} \\
&\approx (r-1) - \frac{x^2}{2} + \mathcal{O}(x^3) \sim X' = R - X^2 \quad \text{[SEEMS LIKE]}
\end{aligned}$$

---

## Page 24

It's easy to understand why this happens. Graphically, we could expect that these bifurcations always that $f(x)$ has/look locally as a bowl, nearby this means that two roots are together.

[FIGURE: Family of curves $f(x, r)$ shifting vertically upward as parameter $r$ increases through $r < r_c$ (two real roots), $r = r_c$ (tangent minimum at $x$-axis), and $r > r_c$ (minimum above axis, zero real roots). Inset shows local parabolic bowl geometry.]

Algebraically speaking, let $x' = f(x; r)$ be a continuous dynamical system where $f(x^*) = 0$ and the critical parameter $r_c$.

1st let's remember that the Taylor function for a 2-variable function is:

$$\begin{aligned}
f(x_1, x_2) = f(a_1, a_2) &+ \left[(x_1 - a_1)\partial_1 f + (x_2 - a_2)\partial_2 f\right]_{(a_1, a_2)} \\
&+ \frac{1}{2!}\left[(x_1 - a_1)^2 \partial_1^2 f + 2(x_1 - a_1)(x_2 - a_2)\partial_{12}^2 f + (x_2 - a_2)^2 \partial_2^2 f\right] + \cdots
\end{aligned}$$

Then our system:

$$\begin{aligned}
x' = f(x, r)|_{(x^*, r_c)} = f(x^*, r_c) &+ \left[(x - x^*)\partial_x f(x^*, r_c) + (r - r_c)\partial_r f(x^*, r_c)\right] \\
&+ \frac{1}{2!}\left[(x - x^*)^2 \partial_x^2 f(x^*, r_c) + \partial_r^2 f(x^*, r_c)(r - r_c)^2 + 2(x - x^*)(r - r_c)\partial_{xr}^2 f(x^*, r_c)\right] \\
&+ \mathcal{O}(r_c^3, a^3)
\end{aligned}$$

Note $f(x^*, r_c) = 0, \quad \partial_x f(x^*, r_c) = 0$ (saddle-node)

$$= \partial_r f(x^*, r_c)(r - r_c) + \frac{1}{2}\partial_x^2 f(x^*, r_c)(x - x^*)^2 + \cdots$$

$$= a(r - r_c) + b(x - x^*)^2 + \cdots \quad \longleftarrow \textbf{NORMAL FORM}$$

---

## Page 25

### Transcritical Bifurcations

There are certain situations where a fixed point will never be destroyed. Eg. the logistic equation & other simple models for the growth of a single species, there is a fixed point at $N=0$ but the stability could change as the growth rate or parameters varies (I called this "the context"), this kind of systems are said to exhibit a **transcritical bifurcation**.

The normal form is:

$$x' = rx - x^2$$

[FIGURE: Three phase portrait plots of $x' = rx - x^2$:
- $r < 0$: roots at $x = r$ (unstable repellor) and $x = 0$ (stable attractor).
- $r = 0$: single degenerate root at $x = 0$ (half-stable node).
- $r > 0$: roots at $x = 0$ (unstable repellor) and $x = r$ (stable attractor).]

[FIGURE: Transcritical bifurcation diagram on the $(r, x^*)$ plane: the trivial branch $x^* = 0$ is stable (solid line) for $r < 0$ and unstable (dashed line) for $r > 0$; the moving branch $x^* = r$ is unstable (dashed line) for $r < 0$ and stable (solid line) for $r > 0$. The two branches intersect at the origin $(0,0)$. Labeled "SOME PEOPLE SAY THIS is an exchange of stabilities".]

---

## Page 26

### Ex. Show that the system undergoes a transcritical bifurcation at $x=0$:

$$x' = x(1 - x^2) - a(1 - e^{-bx})$$

when $ab$ satisfy certain eq. (the eq. will define a bifurcation curve in the $(a,b)$ parameter space). Then find an approximated formula for the fixed point that bifurcates from $x=0$, assuming parameter $a,b$ near to the bifurcation curve.

**SOL:** NOTICE THAT AROUND 0 THE EQ LOOK LIKE:

$$\begin{aligned}
x' &= x(1 - x^2) - a(1 - e^{-bx}) \\
&= x(1 - x^2) - a\left[1 - \left(1 - bx + \frac{1}{2}b^2 x^2 + \mathcal{O}(x^3)\right)\right] \\
&= x(1 - x^2) - a\left[bx - \frac{1}{2}b^2 x^2 + \mathcal{O}(x^3)\right] \\
&= x(1 - x^2) - abx + \frac{ab^2}{2}x^2 + \mathcal{O}(x^3) \\
&= x - x^3 + \mathcal{O}(x^6) - abx + \frac{ab^2}{2}x^2 + \mathcal{O}(x^3) \\
&= x - abx + \frac{ab^2}{2}x^2 + \mathcal{O}(x^3) \\
&= (1 - ab)x + \frac{ab^2}{2}x^2 + \mathcal{O}(x^3)
\end{aligned}$$

Bifurcation condition: $1 - ab = 0 \implies ab = 1$.

$$\textbf{NORMAL FORM: } x' = Rx - x^2 \quad \text{(TRANSCRITICAL BIFURCATION)}$$

[FIGURE: Bifurcation curve in $(a, b)$ parameter space showing the hyperbolic curve $ab = 1$ in the first quadrant separating different qualitative dynamical behaviors.]

We know that:

$$x' \approx (1 - ab)x + \frac{ab^2}{2}x^2$$

$$(1 - ab)x^* + \frac{ab^2}{2}(x^*)^2 \approx 0$$

$$(1 - ab) + \frac{ab^2}{2}x^* \approx 0 \implies x^* \approx \frac{2(ab - 1)}{ab^2}$$

NOTICE THAT ONLY VALID IF $x \ll 1$ & $ab \sim 1$.

---

## Page 27

### Laser Threshold (Haken, 1983)

- $\hookrightarrow$ LASER THEORY
- $\hookrightarrow$ LASER OUTPUT $\rightarrow$ EXPLOTE

[FIGURE: Schematic of a solid-state laser cavity showing an active laser medium (Nd:YAG Crystal, $Yttrium / O \times 14 / Alu$) between two mirrors (left mirror totally reflecting, right mirror partially transmitting laser output), excited by a flashlamp / pump connected to a capacitor discharging electrical pulses.]

The flashlamp / pump excites the atoms on the material, once is excited the atoms returns to ground state and emits light.

Then, we could think on atoms as antennas emitting energy? When the pumping is relatively weak the atoms travel at random but when we start to increase the strength of pumping then the photons start to oscillate in phase and we have a laser.

Notice that, for having that effect of laser we need to trespass certain threshold.

This phenomena is called **synchronization / self-organizing**.

Now a proper model would requires to know a bit of Electrodynamics, Quantum Physics & bit of solid state physics (atomics). But we could extract a model simplified from Haken, 1983 (pp. 127–129) proposes a model where we measure $n(t)$ "the number of photons in laser field":

$$n' = \text{gain} - \text{loss} = GnN - kn$$

---

## Page 28

- **gain:** stimulated emission $\longrightarrow$ light exciting atoms.
  - **NOTICE:** This is a random phenomena, this means that a rate proportional to $n(t)$ (the number of photons) & the number of $N(t)$.
  - $G > 0$ & is called "gain coefficient".
- **loss:** the loss of photons is because the possible escape of photons either by laser or heat.
  - $k > 0$ & is a rate, $\tau = 1/k$ is the mean expectancy life in laser.

Now, after an atom gets excited then emits a photon and then returns to a ground state, we need then a eq that relates $N(t)$ with $n(t)$, $N(t)$ will decrease by emission of photons.

Let's think only in one pulse of the pump, then we will have $N_0$ excited atoms and they will reduce by a factor by the laser process:

$$N(t) = N_0 - \alpha n(t), \quad \alpha > 0$$

$\alpha$: the ratio at which the atoms return to their ground state.

$$n' = Gn(N_0 - \alpha n) - kn = (GN_0 - k)n - \alpha G n^2$$

& finally we are on familiar ground.

---

## Page 29

[FIGURE: Three phase portrait plots of $n' = (GN_0 - k)n - \alpha G n^2$ vs $n$ (downward-opening parabolas):
- Left: $N_0 < k/G$. The only physical fixed point in $n \ge 0$ is $n^* = 0$, which is stable (decaying to zero photons).
- Middle: $N_0 = k/G$. Critical threshold where the vertex of the parabola touches the origin $n^* = 0$.
- Right: $N_0 > k/G$. The origin $n_1^* = 0$ becomes unstable, and a positive stable fixed point $n_2^*$ emerges, representing coherent laser emission.]

$$0 = n\left[(GN_0 - k) - \alpha G n\right]$$

$$n_1^* = 0$$

$$n_2^* \implies GN_0 - k - \alpha G n = 0 \implies \boxed{n_2^* = \frac{GN_0 - k}{\alpha G}}$$

[FIGURE: Bifurcation diagram of steady-state photon number $n$ versus pump parameter $N_0$. For $N_0 < k/G$ (labeled "LAMP"), the stable steady state is $n^* = 0$. At $N_0 = k/G$ (labeled "LASER THRESHOLD"), a transcritical bifurcation occurs, and for $N_0 > k/G$ (labeled "LASER"), the branch $n_2^* = \frac{GN_0 - k}{\alpha G}$ grows linearly with $N_0$ as a stable attractor.]

---

## Observed topic sequence

1. **Course Administration & Evaluation Policy** (Page 1) — Mini-projects, mini-labs, final project, academic integrity / anti-plagiarism policy.
2. **Prerequisites, Course Philosophy & Geometric Mindset** (Page 2) — ODEs, linear algebra, geometric intuition, nonstandard math format without formal theorem-proof structure.
3. **Historical Overview of Dynamics & Chaos (1666–Late 1800s)** (Page 3) — Newton, Kepler, optics, 2-body problem, 3-body / $N$-body problem, letter to Halley on Moon problem, Euler and Gauss failures, Poincaré, phase plane introduction, definition of deterministic chaos.
4. **Historical Overview: Engineering Oscillators, Early Computing & Lorenz** (Page 4) — 1920s–1950s nonlinear oscillators in physics & engineering (vacuum tubes, diodes, radar, lasers, PLLs), early computers, Lorenz atmospheric convection model (1963) and deterministic non-periodic flow.
5. **Historical Overview: Biological Chaos, Fractals & Turbulence** (Page 5) — Smale, KAM theory, Robert May (1975/1976 iterated maps & population biology, "Simple Mathematical Models with very complicated Dynamics"), Mandelbrot fractals, Winfree biological oscillators, Ruelle & Takens turbulence.
6. **Historical Overview: Universality, Popularization & Modern Applications** (Page 6) — Feigenbaum universality and renormalization group, James Gleick's *Chaos* (1987), Jurassic Park pop culture (1993), experimental confirmation, 1990s engineering applications (signal encoding, complex systems).
7. **Celestial Mechanics Fun Fact & General Mathematical Formulation** (Page 7) — ISEE-3 / ICE cometary mission using $N$-body dynamics; formal differential equation system $\vec{x}' = \vec{F}(\vec{x})$ on phase space $\mathbb{R}^n$, definition of linearity vs. nonlinearity.
8. **Phase Space & Geometric Intuition** (Page 8) — 2nd-order linear harmonic oscillator vs. nonlinear pendulum, $(x, v)$ phase portraits, librations, rotations, separatrices, qualitative solution without analytical integration.
9. **One-Dimensional Flows: Linear Example** (Page 9) — $\dot{x} = ax$, analytical separation of variables vs. vector field / phase line flow.
10. **One-Dimensional Flows: Nonlinear Trigonometric Example** (Page 10) — $\dot{x} = \sin x$, analytical integration ($t = \ln|\dots|$), asymptotic behavior ($t \to \infty$), phase line velocity analysis.
11. **Formal Definition of 1D Autonomous Flows** (Page 11) — First-order 1D dynamical systems, definition of "system", restriction to autonomous ODEs ($\dot{x} = f(x)$).
12. **Fixed Points & Qualitative Stability Classification in 1D** (Page 12) — Roots $f(x^*) = 0$, graphical sign analysis, stable attractors, unstable repellors, half-stable nodes.
13. **Formal Definitions of Stability** (Page 13) — Equilibrium condition $f(x^*)=0$, Lyapunov $\varepsilon$-$\delta$ stability, asymptotic stability, convergence rates.
14. **Physical Application: RC Circuit Dynamics** (Page 14) — First-order series RC circuit ODE ($\dot{Q} = V_0/R - Q/(RC)$), fixed point $Q^* = CV_0$, monotonic exponential approach.
15. **Graphical Root Finding & Stability for Transcendental Vector Fields** (Page 15) — $\dot{x} = x - \cos x$, finding fixed point via curve intersection $y=x$ and $y=\cos x$, stability determination without closed-form solution.
16. **Biological Population Dynamics: Exponential vs. Logistic Growth** (Page 16) — Malthusian model ($N' = rN$), per capita growth rate, carrying capacity $K$, logistic equation $N' = rN(1 - N/K)$ phase line.
17. **Biological Context & Introduction to Linear Stability Analysis** (Page 17) — Biological limitations of logistic model (Krebs 1972, age-structure, time delays); definition of small perturbation $\eta(t) = x(t) - x^*$, Taylor series expansion.
18. **Derivation of Linear Stability Analysis & Time Scales** (Page 18) — Linearized equation $\eta' \approx f'(x^*)\eta$, exponential growth/decay criterion, characteristic time scale $\tau = 1/|f'(x^*)|$.
19. **Linear Stability Analysis Examples** (Page 19) — Verification of stability for $\dot{x} = \sin x$ ($x_k^* = k\pi$) and the logistic equation ($N_1^* = 0$, $N_2^* = K$).
20. **Higher-Order Fixed Points & Impossibility of Oscillations in 1D** (Page 20) — Degenerate fixed points where $f'(x^*)=0$ ($x' = -x^3, x^3, x^2$), proof/explanation why periodic solutions and oscillations are impossible in 1D flows (monotonicity on a line).
21. **Mechanical Analogies & Potential Energy Landscapes** (Page 21) — Overdamped spring-mass system in viscous fluid ("honey"); potential function $V(x)$ where $f(x) = -dV/dx$, monotonic decrease of $V(t)$ along trajectories, stability at potential minima.
22. **Introduction to Bifurcations: Saddle-Node Bifurcation** (Page 22) — Structural stability changes under parameter variation, mechanical buckling analogy, prototype $x' = r + x^2$ (or $r - x^2$), blue sky bifurcation, transcendental example $x' = r - x - e^{-x}$ with critical parameter $r_c = 1$.
23. **Normal Forms: Local Taylor Series Approximations** (Page 23) — Prototypical nature of $x' = r \pm x^2$, expanding $x' = r - x - e^{-x}$ around $(x^*=0, r_c=1)$ to recover the standard saddle-node normal form.
24. **Multivariable Taylor Derivation of Saddle-Node Normal Form** (Page 24) — Geometric explanation (parabolic bowl shifting vertically); 2-variable Taylor expansion $f(x, r)$ near $(x^*, r_c)$, rigorous derivation of $x' \approx a(r - r_c) + b(x - x^*)^2$.
25. **Transcritical Bifurcations: Concept & Normal Form** (Page 25) — Persistent fixed points undergoing stability change, normal form $x' = rx - x^2$, exchange of stabilities between branches at $r=0$.
26. **Transcritical Bifurcation Example: Non-Polynomial System** (Page 26) — System $x' = x(1 - x^2) - a(1 - e^{-bx})$, Taylor expansion near $x=0$, bifurcation condition $ab = 1$, non-zero fixed point approximation $x^* \approx \frac{2(ab-1)}{ab^2}$.
27. **Physical Application: Laser Dynamics & Threshold Phenomenon** (Page 27) — Haken (1983) laser model, spontaneous vs. stimulated emission, self-organization/synchronization threshold, photon rate equation $n' = GnN - kn$.
28. **Laser Physics: Gain, Cavity Loss & Excited Atom Depletion** (Page 28) — Gain coefficient $G$, cavity loss rate $k$ and photon lifetime $\tau = 1/k$, excited atom depletion $N(t) = N_0 - \alpha n(t)$, closed equation $n' = (GN_0 - k)n - \alpha G n^2$.
29. **Transcritical Bifurcation Analysis of Laser Threshold** (Page 29) — Fixed points $n_1^* = 0$ and $n_2^* = \frac{GN_0 - k}{\alpha G}$, phase portraits below, at, and above critical pump threshold $N_{0,c} = k/G$, lamp regime vs. lasing regime.
