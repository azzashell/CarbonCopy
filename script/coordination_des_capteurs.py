import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Connexion à l'IoT Hub
connection_string = "your_device_connection_string_here"
client = IoTHubDeviceClient.create_from_connection_string(connection_string)

def generate_temperature():
    """Génère une température aléatoire entre 15 et 30°C."""
    return random.uniform(15, 30)

def detect_fire():
    """Simule la détection de feu avec une probabilité de 5%."""
    return random.choice([True, False])

try:
    while True:
        # Générer des données
        temperature = generate_temperature()
        fire_detected = detect_fire()

        # Créer des messages
        temp_message = Message(f"Temperature: {temperature:.2f}°C")
        fire_message = Message("Fire detected!" if fire_detected else "No fire detected!")

        # Envoyer les messages
        client.send_message(temp_message)
        print(f"Message envoyé : {temp_message.data.decode('utf-8')}")
        
        client.send_message(fire_message)
        print(f"Message envoyé : {fire_message.data.decode('utf-8')}")
        
        # Attendre 5 secondes avant de répéter
        time.sleep(5)

except KeyboardInterrupt:
    print("Envoi de données arrêté par l'utilisateur.")
finally:
    client.shutdown()
