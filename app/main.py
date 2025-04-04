from flask import Flask, jsonify
from simulator import generate_metrics
from azure.cosmos import CosmosClient
import os

app = Flask(__name__)

# Variables de entorno
COSMOS_URI = os.getenv("COSMOS_URI", "https://TU-URI.documents.azure.com:443/")
COSMOS_KEY = os.getenv("COSMOS_KEY", "TU-CLAVE-REAL")
DATABASE_NAME = "iotmetrics-itca-sa"
CONTAINER_NAME = "telemetria"

client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

@app.route("/")
def home():
    return "Middleware IoT funcionando. Usa /send para enviar datos."

@app.route("/send", methods=["GET"])
def send_data():
    payload = generate_metrics()
    container.create_item(body=payload)
    return jsonify({"status": "ok", "data": payload}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
