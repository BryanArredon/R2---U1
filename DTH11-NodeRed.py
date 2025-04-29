import network
import time
from umqtt.simple import MQTTClient
import machine

# Configuración de WiFi
WIFI_SSID = "UTNG_GUEST"
WIFI_PASSWORD = "R3d1nv1t4d0s#UT"

# Configuración del broker MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC_SUB = b"casa/led"  # El mismo tópico del flujo de Node-RED
CLIENT_ID = b"pico_client"

# Pin del LED
LED_PIN = 14  # Ajustar según tu placa

# Función para conectar a WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Conexión WiFi establecida:", wlan.ifconfig())

# Función que se ejecuta cuando llega un mensaje MQTT
def mqtt_callback(topic, msg):
    print(f"Mensaje recibido en {topic}: {msg}")
    if topic == MQTT_TOPIC_SUB:
        if msg == b"ON":
            print("Encendiendo LED")
            led.value(1)
        elif msg == b"OFF":
            print("Apagando LED")
            led.value(0)

# Conectar a MQTT
def connect_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, port=1883)
    client.set_callback(mqtt_callback)
    client.connect()
    print("Conectado al broker MQTT")
    client.subscribe(MQTT_TOPIC_SUB)
    return client

# Inicializar el LED
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Programa principal
try:
    connect_wifi()
    client = connect_mqtt()

    print("Esperando mensajes MQTT...")
    while True:
        client.check_msg()  # Escucha por nuevos mensajes
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Desconectando...")
    client.disconnect()