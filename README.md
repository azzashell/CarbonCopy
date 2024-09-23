# CarbonCopy

Ce projet contient des définitions de modèles pour un système IoT simulant des capteurs connectés à Azure IoT Hub. Les fichiers JSON décrivent divers éléments tels que des usines, des étages, des machines, des chambres, des chariots élévateurs et des unités de stockage.

## Structure du Répertoire

```
Models/
│
├── definitions/
│   ├── factory.json         # Modèle de l'usine
│   ├── floor.json           # Modèle d'un étage
│   ├── forklift.json        # Modèle d'un chariot élévateur
│   ├── machine.json         # Modèle d'une machine
│   ├── room.json            # Modèle d'une chambre
│   └── storageUnit.json     # Modèle d'une unité de stockage
│
└── script/
    ├── coordination_des_capteurs.py # Script de simulation des capteurs
    └── etapes_a_suivre.txt          # Instructions pour exécuter le script
```

## Modèles

### 1. Factory (`factory.json`)
- **Type**: Interface
- **Propriétés**:
  - `name`: Nom de l'usine
  - `location`: Emplacement de l'usine
  - `totalArea`: Superficie totale

### 2. Floor (`floor.json`)
- **Type**: Interface
- **Propriétés**:
  - `floorNumber`: Numéro de l'étage
  - `totalArea`: Superficie totale

### 3. Forklift (`forklift.json`)
- **Type**: Interface
- **Propriétés**:
  - `status`: État du chariot élévateur
  - `batteryLevel`: Niveau de batterie
- **Télémétrie**:
  - `location`: Localisation du chariot élévateur

### 4. Machine (`machine.json`)
- **Type**: Interface
- **Propriétés**:
  - `model`: Modèle de la machine
  - `operationalStatus`: État opérationnel
- **Télémétrie**:
  - `runningHours`: Heures de fonctionnement
  - `temperature`: Température de la machine

### 5. Room (`room.json`)
- **Type**: Interface
- **Propriétés**:
  - `roomName`: Nom de la chambre
  - `roomType`: Type de chambre
- **Relations**:
  - `containsForklifts`: Chariots élévateurs contenus
  - `containsMachines`: Machines contenues
  - `containsStorageUnits`: Unités de stockage contenues

### 6. Storage Unit (`storageUnit.json`)
- **Type**: Interface
- **Propriétés**:
  - `capacity`: Capacité de l'unité de stockage
  - `contents`: Contenu de l'unité
- **Télémétrie**:
  - `inventoryLevel`: Niveau d'inventaire

## Exécution du Script

Le script `coordination_des_capteurs.py` simule des capteurs IoT connectés à Azure IoT Hub, envoyant des messages basés sur des conditions simulées telles que la température et la détection de feu.

### Étapes à Suivre

1. Installez le module requis :
   ```bash
   pip install azure-iot-device
   ```

2. Vérifiez si le module est accessible :
   ```bash
   pip show azure-iot-device
   ```

3. Créez le fichier à exécuter :
   ```bash
   nano coordination_des_capteurs.py
   ```

4. Exécutez le code :
   ```bash
   python coordination_des_capteurs.py
   ```

### Résultat

Le résultat de l'exécution sera enregistré dans `resultat-d-execution.mp4`.

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des demandes de tirage ou à signaler des problèmes.
