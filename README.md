# Middleware IoT Simulado

Simulador de datos de sensores que se envían a Azure Cosmos DB.

## Tecnologías

- Python + Flask
- Azure Cosmos DB (API SQL)
- Docker
- Git + GitHub

## Cómo ejecutar

```bash
docker build -t middleware-iot .
docker run -p 5000:5000 \
  -e COSMOS_URI='https://<tu-uri>.documents.azure.com:443/' \
  -e COSMOS_KEY='<tu-key>' \
  middleware-iot
