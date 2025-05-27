# eHealth IoT + Machine Learning Project

Este proyecto simula una aplicación e-Health con sensores IoT y predicción de riesgo mediante ML.

## Componentes

- **Simulador de sensores:** `data_simulator.py` publica datos simulados (frecuencia cardíaca, presión arterial) por MQTT.
- **Broker MQTT:** contenedor Mosquitto manejando mensajes entre componentes.
- **Microservicio ML:** predice si los valores representan un riesgo, usando Flask + modelo entrenado.
- **Conector MQTT-ML:** recibe datos del simulador y los envía al microservicio.

## Uso

1. Instala Docker y Docker Compose.
2. Ejecuta:

```bash
docker-compose up --build
```

3. En otra terminal, entrena el modelo:

```bash
cd ml_service
python train.py
```

4. Lanza el simulador:

```bash
python data_simulator.py
```

5. En otra terminal, ejecuta el conector:

```bash
python mqtt_to_ml.py
```

Verás predicciones de riesgo en consola.