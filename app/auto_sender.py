import time
from simulator import generate_metrics
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv
import os
import hashlib

# Cargar archivo .env
load_dotenv()

# Cargar variables de entorno
COSMOS_URI = os.getenv("COSMOS_URI")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "iotmetrics-itca-sa-v2"
CONTAINER_NAME = "telemetria"
PARTITION_KEY_PATH = "/deviceId"


#Pruebas
print("🧪 COSMOS_URI:", COSMOS_URI)
print("🧪 COSMOS_KEY:", COSMOS_KEY[:10] + "...")  # muestra solo un pedazo

# Conectar a Cosmos DB
client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

print("🚀 Iniciando envío automático de métricas cada 5 segundos...")

# Bucle infinito
while True:
    try:
        data = generate_metrics()
        print("📤 Enviando ID:", data["id"])
        print("🔍 Hash de objeto data:", hashlib.md5(str(data).encode()).hexdigest())

        container.upsert_item(body=data)
        
        print(f"✅ [{data['timestamp']}] Métricas enviadas: {data['messageId']}")
    except Exception as e:
        print("❌ Error al enviar:", str(e))
        print("---------------------------------------------------------------------------")
    time.sleep(5)
