🔌 Middleware IoT para Simulación y Registro de Métricas Eléctricas
Este proyecto simula métricas de sensores eléctricos de un sistema industrial y las envía automáticamente a Azure Cosmos DB. Incluye simulación de fallas eléctricas comunes y registro paralelo de logs de fallas, que pueden ser usados posteriormente en un sistema de detección con Machine Learning.

🧰 Tecnologías Utilizadas
Python 3.10+

Azure Cosmos DB

SDK azure-cosmos

Docker (opcional para despliegue)

Variables de entorno con os.getenv

Formato JSON y estructura jerárquica para datos de sensores

UUID para trazabilidad (id, messageId)

📁 Estructura del Proyecto

middleware-iot/
├── auto_sender.py        --> Envío automático de métricas a Cosmos DB
├── simulator.py          --> Simulación de métricas con fallas aleatorias
├── fault_logger.py       --> Registro de logs de fallas en otro contenedor
├── Dockerfile            --> Imagen para despliegue opcional
├── .env.example          --> Variables de entorno (plantilla)
└── README.md             --> Documentación del proyecto

⚙️ Configuración de Variables de Entorno
Crea un archivo .env (o usa .env.example como base) con el siguiente contenido:

COSMOS_URI=https://<tu-cuenta>.documents.azure.com:443/
COSMOS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DATABASE_NAME=NombreDeTuBD
METRICS_CONTAINER=NombreContenedorMétricas
FAULTS_CONTAINER=NombreContenedorFallas

🚀 Cómo Ejecutar
Para ejecutar el envío automático de métricas:
python auto_sender.py

Cada minuto se genera una métrica, y cada hora (o cada 60 segundos en modo pruebas) se inyecta una falla simulada y se registra un log asociado en el contenedor de fallas.

📦 Despliegue con Docker (opcional)
Puedes construir y correr la imagen con Docker:


# Construir la imagen
docker build -t middleware-iot .

# Ejecutar usando las variables de entorno del archivo .env
docker run --env-file .env middleware-iot


🧠 Futuras funcionalidades
Dashboard con métricas y análisis (Streamlit, Dash o Power BI)

Detección de anomalías con Machine Learning en tiempo real

Pruebas unitarias para validación de simulaciones

👨‍💻 Desarrollado por
Alexander Rivas
GitHub: @arivasbits
Proyecto académico y de práctica con Azure Cosmos DB, Python y Docker.