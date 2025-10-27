# Laboratorio 02 Robótica - Robótica Industrial - Análisis y Operación del
Manipulador Motoman MH6.
En este laboratorio se estudiaron las características del Manipulador Motoman MH6 y su funcionamiento utilizando el softwar RoboSDK, para esto se programó que el manipulador siguiera una trayectoria polar y finalmente escribiera los nombres de ambos integrantes del grupo.

## Cuadro comparativo entre manipulador Motoman MH6 y manipulador IRB140.

| **Característica** | **Motoman MH6 (Yaskawa)** | **ABB IRB 140 (ABB Robotics)** |
|---------------------|---------------------------|--------------------------------|
| **Carga máxima (payload)** | 6 kg | 6 kg |
| **Alcance máximo** | 1424 mm | 810 mm |
| **Número de ejes / grados de libertad** | 6 ejes | 6 ejes |
| **Repetibilidad** | ± 0.08 mm | ± 0.03 mm |
| **Peso del robot** | 130 kg aprox. | 98 kg |
| **Velocidad eje 1 (base)** | 170 °/s | 250 °/s |
| **Velocidad eje 2** | 160 °/s | 230 °/s |
| **Velocidad eje 3** | 170 °/s | 260 °/s |
| **Velocidad eje 4 (muñeca rotacional)** | 340 °/s | 320 °/s |
| **Velocidad eje 5 (inclinación muñeca)** | 340 °/s | 320 °/s |
| **Velocidad eje 6 (rotación muñeca)** | 520 °/s | 420 °/s |
| **Tipo de montaje** | Piso, pared o invertido | Piso, pared, invertido o en ángulo |
| **Controlador** | DX100 / DX200 | IRC5 Compact |
| **Fuente de alimentación** | 200 – 230 V AC trifásico | 200 – 600 V AC trifásico (según config.) |
| **Grado de protección** | IP54 (cuerpo) / IP67 (muñeca) | IP54 (cuerpo) / IP67 (muñeca) |
| **Rango de temperatura de operación** | 0 – 45 °C | 5 – 45 °C |
| **Flange (montaje de herramienta)** | ISO 9409-1-A50 | ISO 9409-1-A50 |
| **Aplicaciones típicas** | Manipulación general, soldadura por arco, carga/descarga, ensamblaje, paletizado, inspección, corte, dispensado | Ensamblaje de precisión, manipulación de materiales, carga/descarga, atornillado, pulido, laboratorio |
| **Ventajas destacadas** | Gran alcance y estructura robusta; compatible con múltiples montajes | Alta precisión, tamaño compacto, ideal para espacios reducidos |
| **Limitaciones** | Repetibilidad menor que IRB 140, tamaño mayor | Alcance más corto, limitado para piezas grandes |

## Diferencias entre posiciones Home1 y Home2 en el manipulador Motoman MH6
La posición Home 1 corresponde generalmente a una postura de descanso o almacenamiento en la que el robot se encuentra retraído con los brazos y eslabones cerca a la base. En esta configuración, el centro de masa del brazo queda alineado de manera que el peso propio del manipulador ejerce un momento mínimo sobre los frenos de los motores de los ejes principales. Esto reduce el esfuerzo necesario para mantener las articulaciones en su lugar cuando el robot se encuentra desenergizado, evitando desplazamientos por gravedad. Por esta razón, la posición Home 1 se debe utilizar al finalizar la operación ya que contribuye a prolongar la vida útil de los frenos y reductores.

Mientras que la posición Home 2 se define como una posición de referencia geométrica o de calibración más estándar en la que las articulaciones principales se encuentran en 0 grados. En esta posición el manipulador adopta una postura extendida hacia adelante. En esta configuración, los ejes se alinean de manera que el brazo queda orientado de forma recta y perpendicular al plano de la base y el efector final perpendicular al brazo. Esta configuración facilita la orientación del efector final y la programación de trayectorias. 

## Procedimiento detallado para realizar movimientos manuales; traslaciones, rotaciones y modos de operación.
## Velocidad para movimientos manueales, identificación y operación.
## Descripciónn de las principales funcionalidades de RoboDK: Comunicación y Procesos.
## Análisis comparativo entre RoboDK y RobotStudio.
## Diagrama de flujo de acciones del robot.
## Plano de planta de la ubicaciónn de cada uno de los elementos.
## Código desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
## Video de simulación en RoboDK mostrando la trayectoria polar y evidencia de su implementación en el manipulador Motoman de forma física, controlado desde el PC.


