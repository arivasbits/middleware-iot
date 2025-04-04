import os
from datetime import datetime
from azure.cosmos import CosmosClient
from dotenv import load_dotenv
import uuid

load_dotenv()

COSMOS_URI = os.getenv("COSMOS_URI")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "iotmetrics-itca-sa-v2"
FAULT_CONTAINER = "logs_fallas"

client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
db = client.get_database_client(DATABASE_NAME)
container = db.get_container_client(FAULT_CONTAINER)

def log_fault(fault_code, timestamp):
    try:
        fault_document = {
            "id": str(uuid.uuid4()),
            "deviceId": "LABVIEW_DEVICE_001",
            "timestamp": timestamp,
            "faultCode": fault_code,
            "description": "Falla simulada automáticamente",
        }
        container.upsert_item(body=fault_document)
        print(f"📝 Falla registrada: {fault_code} a las {timestamp}")
    except Exception as e:
        print(f"❌ Error al registrar falla: {e}")
