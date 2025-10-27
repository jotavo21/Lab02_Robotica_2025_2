from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
##if not robot.Connect():
    ##raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
if not robot.ConnectedState():
    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

print("Robot conectado correctamente.")

#------------------------------------------------
# 2) Cargar el Frame (ya existente) donde quieres dibujar
#    Ajusta el nombre si tu Frame se llama diferente
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# Asignamos este frame al robot
robot.setPoseFrame(frame)
# Usamos la herramienta activa
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

#------------------------------------------------
# 3) Parámetros de la figura (rosa polar)
#------------------------------------------------
num_points = 720       # Cuántos puntos muestreamos (mayor = más suave)
A = 150               # Amplitud (300 mm = radio máximo)
k = 3                  # Parámetro de la rosa (pétalos). Si es impar, habrá k pétalos; si es par, 2k
z_surface = 0          # Z=0 en el plano del frame
z_safe = 50            # Altura segura para aproximarse y salir

#------------------------------------------------
# 4) Movimiento al centro en altura segura
#------------------------------------------------
# El centro de la rosa (r=0) corresponde a x=0, y=0
robot.MoveJ(transl(0, 0, z_surface + z_safe))

# Bajamos a la "superficie" (Z=0)
robot.MoveL(transl(0, 0, z_surface))

#------------------------------------------------
# 5) Dibujar la rosa polar
#    r = A * sin(k*theta)
#    x = r*cos(theta), y = r*sin(theta)
#------------------------------------------------
# Recorremos theta de 0 a 2*pi (una vuelta completa)
full_turn = 2*math.pi

for i in range(num_points+1):
    # Fracción entre 0 y 1
    t = i / num_points
    # Ángulo actual
    theta = full_turn * t

    # Calculamos r
    r = 25 + A *(math.cos(k * theta))

    # Convertimos a coordenadas Cartesianas X, Y
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # Movemos linealmente (MoveL) en el plano del Frame
    robot.MoveL(transl(x, y, z_surface))

# Texto a dibujar
texto = "Ian y Juan"

# Crear un TextPath (contorno del texto)
tp = TextPath((0, 0), texto, size=35)

# Obtener los vértices del texto
X,Y = tp.vertices[:, 0], tp.vertices[:, 1]
# Convertir a coordenadas polares
for i in range(len(X)):
    # Convertimos a coordenadas Cartesianas X, Y
    x = Y[i]-150
    y = X[i]
    # Movemos linealmente (MoveL) en el plano del Frame
    robot.MoveL(transl(x, y, z_surface))

# Al terminar, subimos de nuevo para no chocar
robot.MoveL(transl(x, y, z_surface + z_safe))
robot.MoveL(transl(0, 0, z_surface + z_safe))

print(f"¡Figura (rosa polar) completada en el frame '{frame_name}'!")

