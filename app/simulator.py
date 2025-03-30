import random
import uuid
from datetime import datetime

def generate_metrics():
    metrics = [
        {"name": "Van", "value": round(random.uniform(115, 125), 2), "unit": "V", "group": "voltages"},
        {"name": "Vbn", "value": round(random.uniform(115, 125), 2), "unit": "V", "group": "voltages"},
        {"name": "Vcn", "value": round(random.uniform(115, 125), 2), "unit": "V", "group": "voltages"},
        {"name": "Ia", "value": round(random.uniform(2, 10), 2), "unit": "A", "group": "currents"},
        {"name": "Ib", "value": round(random.uniform(2, 10), 2), "unit": "A", "group": "currents"},
        {"name": "Ic", "value": round(random.uniform(2, 10), 2), "unit": "A", "group": "currents"},
        {"name": "P", "value": round(random.uniform(1500, 1700), 2), "unit": "W", "group": "power"},
        {"name": "Q", "value": round(random.uniform(200, 300), 2), "unit": "VAR", "group": "power"},
        {"name": "S", "value": round(random.uniform(1600, 1800), 2), "unit": "VA", "group": "power"},
        {"name": "FP", "value": round(random.uniform(0.95, 1.00), 2), "unit": "ratio", "group": "power"},
        {"name": "voltage_imbalance", "value": round(random.uniform(0.5, 2.5), 2), "unit": "%", "group": "imbalances"},
        {"name": "current_imbalance", "value": round(random.uniform(10, 80), 2), "unit": "%", "group": "imbalances"},
    ]

    return {
        "deviceId": "LABVIEW_DEVICE_001",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "messageId": str(uuid.uuid4()),
        "location": {
            "site": "ITCA-SantaAna",
            "asset": "TableroCC2"
        },
        "status": "OK",
        "metrics": metrics
    }
