import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Connexion à l'IoT Hub
connection_string = "HostName=azza.azure-devices.net;DeviceId=Capteur1;SharedAccessKey=Ve+wO+aB81xf/gVtdit/Hkl71goHNrBrSAIoTCWId4Y="
client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# Seuil de température critique
TEMPERATURE_THRESHOLD = 25.0

def generate_temperature():
    """Génère une température aléatoire entre 15 et 30°C."""
    return random.uniform(15, 30)

def detect_fire():
    """Simule la détection de feu avec une probabilité de 5%."""
    return random.choice([True, False])

def activate_water_flow():
    """Simule l'activation du débit d'eau."""
    return "Water flow activated"

def send_message(message):
    """Envoie un message au IoT Hub et affiche le message."""
    msg = Message(message)
    client.send_message(msg)
    print(f"Message envoyé : {message}")

try:
    while True:
        # Générer des données
        temperature = generate_temperature()
        fire_detected = detect_fire()

        # Générer les messages
        if temperature > TEMPERATURE_THRESHOLD:
            send_message(f"ALERT! High temperature detected: {temperature:.2f}°C")
            if fire_detected:
                send_message("Fire detected! Activating water flow.")
                water_message = activate_water_flow()
                send_message(water_message)
            else:
                send_message("No fire detected. Temperature high but no action taken.")
        else:
            send_message(f"Temperature: {temperature:.2f}°C")
            if fire_detected:
                send_message("Fire detected! Water flow needed but temperature is normal.")
            else:
                send_message("No fire detected. Temperature normal.")

        # Attendre 5 secondes avant de répéter
        time.sleep(5)

except KeyboardInterrupt:
    print("Envoi de données arrêté par l'utilisateur.")
finally:
    client.shutdown()
