# ⚙️ Middleware IoT – Simulación de Métricas con Fallas para Azure Cosmos DB

Este proyecto es un middleware en Python que simula métricas eléctricas provenientes de un sistema IoT (como LabVIEW) y las envía automáticamente a Azure Cosmos DB. Cada cierto tiempo, también se genera una falla eléctrica aleatoria para alimentar datasets de Machine Learning. Las fallas se registran en un contenedor separado.

---

## 📁 Estructura del Proyecto

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

🚀 Tecnologías Utilizadas
Python 3.10+

Azure Cosmos DB

SDK azure-cosmos

Docker (opcional para despliegue)

dotenv para manejo de variables de entorno

⚙️ Funcionalidad Principal
✅ Generación de métricas IoT (voltajes, corrientes, potencias, etc.)

⚡ Simulación automática de fallas eléctricas (caída de fase, FP bajo, brownout, etc.)

📤 Envío a contenedor de métricas en Azure Cosmos DB

🛑 Registro de fallas en contenedor separado como dataset etiquetado

📦 Desplegable como imagen Docker

{
  "id": "c24a1a6e-3abc-4ea1-a6be-843c9cdaab6b",
  "deviceId": "LABVIEW_DEVICE_001",
  "timestamp": "2025-04-03T23:37:02.438603+00:00",
  "status": "OK",
  "metrics": [
    {"name": "Van", "value": 122.4, "unit": "V", "group": "voltages"},
    {"name": "Ia", "value": 7.23, "unit": "A", "group": "currents"},
    ...
  ]
}

📊 Consulta de Fallas desde Azure Cosmos DB
Consulta básica en Data Explorer para detectar métricas anómalas:

SELECT *
FROM c
WHERE EXISTS (
    SELECT VALUE m
    FROM m IN c.metrics
    WHERE
        (m.name = "Vcn" AND m.value = 0) OR
        (m.name = "Van" AND m.value > 130) OR
        (m.name = "Vbn" AND m.value < 105) OR
        (m.name = "voltage_imbalance" AND m.value > 7) OR
        (m.name = "Ia" AND m.value > 12) OR
        (m.name = "FP" AND m.value < 0.85)
)
📂 Uso del Proyecto
Clonar el repositorio

bash
Copiar
Editar
git clone https://github.com/arivasbits/middleware-iot.git
cd middleware-iot
Crear archivo .env basado en el .env.example
Reemplaza con tus credenciales de Azure Cosmos DB.

Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Ejecutar el envío automático

bash
Copiar
Editar
python app/auto_sender.py
🐳 Docker (Opcional)
Para ejecutar desde contenedor:

bash
Copiar
Editar
docker build -t middleware-iot .
docker run --env-file .env middleware-iot
🔒 Notas de Seguridad
No subas tu archivo .env con claves privadas.

Usa gitignore correctamente para evitar exponer información sensible.

🧠 Uso futuro del log de fallas
Los registros en el contenedor logs_fallas permitirán:

Entrenar modelos de detección de anomalías

Realizar trazabilidad y auditoría de eventos

Comparar predicciones del modelo con eventos reales etiquetados

✍️ Autor
Alexander Rivas – @arivasbits
Proyecto académico con fines de monitoreo inteligente IoT + IA