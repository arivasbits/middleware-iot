# test_sim.py
from app.simulator import generate_metrics
import json

print(json.dumps(generate_metrics(), indent=2))
