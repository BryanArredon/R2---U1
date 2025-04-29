import machine
import time
import random

# Configurar los LEDs
led_rojo = machine.Pin(27, machine.Pin.OUT)  # Cambia 16 por tu pin del LED rojo
led_verde = machine.Pin(14, machine.Pin.OUT) # Cambia 17 por tu pin del LED verde

while True:
    # Simular una temperatura aleatoria entre 20 y 40 grados
    temperatura = random.randint(20, 40)
    print('Temperatura simulada: {}°C'.format(temperatura))

    if temperatura > 30:
        led_verde.off()
        # Parpadeo de alerta
        for _ in range(6):  # Parpadea 3 veces (on + off = 1 parpadeo)
            led_rojo.on()
            time.sleep(0.2)  # 200 ms encendido
            led_rojo.off()
            time.sleep(0.2)  # 200 ms apagado
    else:
        led_rojo.off()
        led_verde.on()
        time.sleep(2)  # Espera 2 segundos en verde antes de la siguiente lectura

