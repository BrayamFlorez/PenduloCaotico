Descripción General del Código:

El código simula un péndulo doble bajo el efecto de la gravedad y muestra la animación de las oscilaciones de los péndulos.
Utiliza las ecuaciones de movimiento de un péndulo doble para resolver numéricamente las posiciones de los péndulos en función del tiempo.
La animación muestra las trayectorias seguidas por los extremos de ambos péndulos en el plano mientras se mueven.

Variables que se pueden alterar:

g: Aceleración debido a la gravedad. Puedes cambiar este valor para simular el péndulo en diferentes condiciones de gravedad.
L1, L2: Longitud de los péndulos. Alterar estos valores cambiará las longitudes de los péndulos en la simulación.
m1, m2: Masas de los péndulos. Cambiar estos valores modificará las masas de los péndulos en la simulación.
initial_state: Condiciones iniciales de los ángulos y velocidades angulares de los péndulos.
t_span: Tiempo de integración. Puedes cambiar el tiempo total de simulación ajustando estos valores.
t_eval: Array de tiempo para evaluar las soluciones. Puedes ajustar esto para controlar la resolución temporal de la simulación.
plt.pause(0.05): Controla la velocidad de la animación. Puedes cambiar este valor para acelerar o desacelerar la animación.
