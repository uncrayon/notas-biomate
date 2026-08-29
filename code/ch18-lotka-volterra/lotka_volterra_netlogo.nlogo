; ==============================================================================
; Modelo de Lotka-Volterra basado en agentes (Presas y Depredadores)
; Referencia: Capítulo 18 - Modelo de Lotka-Volterra y ciclos límites (Sección 18.2)
; Notas de Matemáticas Biológicas - Sistemas Dinámicos No Lineales
; ==============================================================================

globals [presas-iniciales depredadores-iniciales]
turtles-own [energia]

to setup
  clear-all
  if presas-iniciales = 0 [ set presas-iniciales 100 ]
  if depredadores-iniciales = 0 [ set depredadores-iniciales 20 ]
  create-turtles presas-iniciales [
    setxy random-xcor random-ycor
    set color green  set energia 10
  ]
  create-turtles depredadores-iniciales [
    setxy random-xcor random-ycor
    set color red
  ]
  reset-ticks
end

to go
  ask turtles [
    ifelse color = red
      [ let presa min-one-of turtles with [color = green]
                        [distance myself]
        if presa != nobody [
          face presa
          fd 1.2
          if distance presa < 1 [
            ask presa [ die ]
          ]
        ] ]
      [ fd 1  set energia energia - 1
        if energia < 2 [ die ] ]
  ]
  tick
end
@#$#@#$#@
GRAPHICS-WINDOW
210
10
640
440
-1
-1
13.0
1
10
1
1
1
0
0
0
1
-16
16
-16
16
1
1
1
ticks
30.0

BUTTON
20
20
95
55
setup
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
20
65
95
100
go
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

SLIDER
20
110
190
143
presas-iniciales
presas-iniciales
0
500
100.0
10
1
NIL
HORIZONTAL

SLIDER
20
155
190
188
depredadores-iniciales
depredadores-iniciales
0
200
20.0
5
1
NIL
HORIZONTAL
@#$#@#$#@
## QUÉ ES ESTE MODELO

Este modelo ilustra la dinámica clásica presa-depredador (Lotka-Volterra) a nivel de agentes individuales discretos (turtles).

- **Presas (verde)**: se mueven en el espacio y consumen energía.
- **Depredadores (rojo)**: persiguen activamente a la presa más cercana.

Referencia: Sección 18.2 de las Notas de Matemáticas Biológicas.
@#$#@#$#@
@#$#@#$#@
NetLogo 6.4.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250
@#$#@#$#@
@#$#@#$#@
1
@#$#@#$#@
