import random
import uuid
from datetime import datetime, timezone
from fault_logger import log_fault

# Global para control de tiempo
last_fault_minute = None

def generate_metrics():
    global last_fault_minute

    # Valores normales
    voltages = {
        "Van": round(random.uniform(115, 125), 2),
        "Vbn": round(random.uniform(115, 125), 2),
        "Vcn": round(random.uniform(115, 125), 2)
    }
    currents = {
        "Ia": round(random.uniform(2, 10), 2),
        "Ib": round(random.uniform(2, 10), 2),
        "Ic": round(random.uniform(2, 10), 2)
    }
    power = {
        "P": round(random.uniform(1500, 1700), 2),
        "Q": round(random.uniform(200, 300), 2),
        "S": round(random.uniform(1600, 1800), 2),
        "FP": round(random.uniform(0.95, 1.00), 2)
    }
    imbalance = {
        "voltage_imbalance": round(random.uniform(0.5, 2.5), 2),
        "current_imbalance": round(random.uniform(10, 80), 2)
    }

    now = datetime.now(timezone.utc)
    current_minute = now.minute

    apply_fault = False
    if last_fault_minute is None or (current_minute - last_fault_minute) >= 1:
        last_fault_minute = current_minute
        apply_fault = True

    if apply_fault:
        fault_code = random.choice(["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11"])
        print("⚠️ Simulando falla:", fault_code)

        if fault_code == "F1":
            voltages["Vcn"] = 0.0
        elif fault_code == "F2":
            voltages["Van"] = round(random.uniform(130, 140), 2)
        elif fault_code == "F3":
            voltages["Vbn"] = round(random.uniform(90, 105), 2)
        elif fault_code == "F4":
            voltages["Vcn"] = round(voltages["Van"] - 15, 2)
            imbalance["voltage_imbalance"] = round(random.uniform(6, 10), 2)
        elif fault_code == "F5":
            currents["Ia"] = round(random.uniform(12, 16), 2)
        elif fault_code == "F6":
            currents["Ic"] = round(random.uniform(0.1, 0.4), 2)
        elif fault_code == "F7":
            currents["Ib"] = round(random.uniform(2, 3), 2)
            currents["Ic"] = round(random.uniform(10, 12), 2)
            imbalance["current_imbalance"] = round(random.uniform(90, 120), 2)
        elif fault_code == "F8":
            power["FP"] = round(random.uniform(0.6, 0.84), 2)
        elif fault_code == "F9":
            power["Q"] = round(random.uniform(401, 450), 2)
        elif fault_code == "F10":
            power["P"] = 0.0
            power["S"] = 0.0
        elif fault_code == "F11":
            imbalance["voltage_imbalance"] = round(random.uniform(7.1, 10), 2)
            imbalance["current_imbalance"] = round(random.uniform(101, 120), 2)

        # Log de la falla
        log_fault(fault_code=fault_code, timestamp=now.isoformat())

    metrics = []
    for name, value in voltages.items():
        metrics.append({"name": name, "value": value, "unit": "V", "group": "voltages"})
    for name, value in currents.items():
        metrics.append({"name": name, "value": value, "unit": "A", "group": "currents"})
    for name, value in power.items():
        unit = "ratio" if name == "FP" else ("W" if name == "P" else "VAR" if name == "Q" else "VA")
        metrics.append({"name": name, "value": value, "unit": unit, "group": "power"})
    for name, value in imbalance.items():
        metrics.append({"name": name, "value": value, "unit": "%", "group": "imbalances"})

    new_id = str(uuid.uuid4())
    return {
        "id": new_id,
        "messageId": new_id,
        "deviceId": "LABVIEW_DEVICE_001",
        "timestamp": now.isoformat(),
        "location": {
            "site": "ITCA-SantaAna",
            "asset": "TableroCC2"
        },
        "status": "OK",
        "metrics": metrics
    }
