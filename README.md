# MIDDLEWARE-IOT

Este proyecto simula la generación de métricas eléctricas (voltajes, corrientes, potencia, etc.) y las envía automáticamente a **Azure Cosmos DB**. Cada cierto tiempo, se simula una falla aleatoria para pruebas de detección de anomalías mediante Machine Learning.

> 🔬 Ideal para pruebas de modelos de ML, visualización de métricas, análisis de datos y validación de fallas.

---

## Tecnologías Usadas

- **Python 3.10+**
- **Azure Cosmos DB**
- **Docker (opcional)**
- **uuid, datetime, os, time, random**
- **Azure Cosmos SDK for Python**

---

## ¿Qué hace este proyecto?

- Simula datos de sensores eléctricos cada 5 segundos.
- Genera fallas aleatorias cada 1 minuto para pruebas.
- Envía las métricas a un contenedor en Cosmos DB (`Lecturas`).
- Si se genera una falla, registra un log de la falla en otro contenedor (`logs_fallas`).

---

## Estructura del Proyecto

```bash
middleware-iot/
├── app/
│   ├── auto_sender.py       # Envío automático de métricas a Cosmos DB
│   ├── simulator.py         # Simulación de métricas con fallas aleatorias
│   ├── fault_logger.py      # Registro de logs de fallas en otro contenedor
│   └── main.py              # Punto de entrada principal (opcional)
├── Dockerfile               # Imagen para despliegue opcional en contenedor
├── .env.example             # Variables de entorno (plantilla)
├── .gitignore               # Exclusión de archivos innecesarios
├── README.md                # Documentación del proyecto
└── requirements.txt         # Dependencias del proyecto

---

## ⚠Ejemplo de Falla Simulada

```json
{
  "id": "946feea1-d9b9-4c48-ad6c-720ab47b6e4f",
  "deviceId": "LABVIEW_DEVICE_001",
  "timestamp": "2025-04-03T23:37:02.438603+00:00",
  "faultCode": "F8",
  "description": "Falla simulada automáticamente"
}

##Consultas útiles en Cosmos DB
Consulta para ver registros que contienen posibles fallas:

SELECT *
FROM c
WHERE EXISTS (
    SELECT VALUE m
    FROM m IN c.metrics
    WHERE 
        (m.name = "Vcn" AND m["value"] = 0) OR
        (m.name = "Van" AND m["value"] > 130) OR
        (m.name = "Vbn" AND m["value"] < 105) OR
        (m.name = "voltage_imbalance" AND m["value"] > 7) OR
        (m.name = "Ia" AND m["value"] > 12) OR
        (m.name = "FP" AND m["value"] < 0.85)
)
## Variables de Entorno .env
Ejemplo de archivo .env:
COSMOS_URI=https://<tu-endpoint>.documents.azure.com:443/
COSMOS_KEY=<tu-clave>
DATABASE_NAME=InvernaderoDB
CONTAINER_NAME=Lecturas
LOGS_CONTAINER_NAME=logs_fallas

## Uso con Docker
docker build -t middleware-iot .
docker run --env-file .env middleware-iot
## 👨‍💻 Autor
Alexander Rivas

