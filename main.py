import numpy as np
import matplotlib.pyplot as plt

# Parámetros del péndulo
g = 9.8  # Aceleración debido a la gravedad
L1 = 1.0  # Longitud del primer péndulo
L2 = 1.0  # Longitud del segundo péndulo
m1 = 1.0  # Masa del primer péndulo
m2 = 1.0  # Masa del segundo péndulo


# Función para calcular las derivadas de theta1, theta2, omega1 y omega2
def derivatives(t, state):
    theta1, theta2, omega1, omega2 = state

    # Derivadas de theta1 y theta2
    dtheta1 = omega1
    dtheta2 = omega2

    # Denominadores comunes
    denominator1 = m1 + m2 * np.sin(theta1 - theta2) ** 2
    denominator2 = (L1 / L2) * denominator1

    # Derivadas de omega1 y omega2
    domega1 = (m2 * g * np.sin(theta2) * np.cos(theta1 - theta2) -
               m2 * np.sin(theta1 - theta2) * (L2 * omega2 ** 2 + L1 * omega1 ** 2 * np.cos(theta1 - theta2)) -
               (m1 + m2) * g * np.sin(theta1)) / L1 / denominator1

    domega2 = ((m1 + m2) * (
                L1 * omega1 ** 2 * np.sin(theta1 - theta2) - g * np.sin(theta2) + g * np.sin(theta1) * np.cos(
            theta1 - theta2)) +
               m2 * L2 * omega2 ** 2 * np.sin(theta1 - theta2) * np.cos(theta1 - theta2)) / L2 / denominator2

    return [dtheta1, dtheta2, domega1, domega2]


# Condiciones iniciales
initial_state = [np.pi / 2, np.pi / 2, 0, 0]  # theta1, theta2, omega1, omega2

# Tiempo de integración
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Resolviendo las ecuaciones diferenciales
from scipy.integrate import solve_ivp

solution = solve_ivp(derivatives, t_span, initial_state, t_eval=t_eval)

# Almacenar las trayectorias de los extremos de los péndulos
x1_path, y1_path = [], []
x2_path, y2_path = [], []


# Función para calcular la posición de los péndulos en función del tiempo
def position(theta1, theta2):
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    return x1, y1, x2, y2


# Inicializar la figura
plt.figure()


# Función de animación
def animate(frame):
    plt.cla()
    theta1 = solution.y[0, frame]
    theta2 = solution.y[1, frame]

    x1, y1, x2, y2 = position(theta1, theta2)

    x1_path.append(x1)
    y1_path.append(y1)
    x2_path.append(x2)
    y2_path.append(y2)

    plt.plot(x1_path, y1_path, color='blue', alpha=0.5)  # Trayectoria del extremo del péndulo 1
    plt.plot(x2_path, y2_path, color='red', alpha=0.5)  # Trayectoria del extremo del péndulo 2

    plt.plot([0, x1], [0, y1], '-o', color='blue')  # Péndulo 1
    plt.plot([x1, x2], [y1, y2], '-o', color='red')  # Péndulo 2

    plt.xlim(-2, 2)
    plt.ylim(-2, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Péndulo Doble Caótico')


# Animar
for frame in range(len(t_eval)):
    animate(frame)
    plt.pause(0.05)  # Pausa para actualizar la animación

plt.show()
