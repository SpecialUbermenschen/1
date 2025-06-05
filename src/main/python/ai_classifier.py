"""Simple rule based incident classifier."""

from typing import Dict


class IncidentClassifier:
    def __init__(self):
        # Map simplified incident type to classification label
        self.known_incidents: Dict[str, str] = {
            "high_cpu": "cpu",
            "high_memory": "memory",
            "error_log": "error",
        }

    def classify(self, incident: Dict) -> str:
        """Return a classification label for the incident."""
        incident_type = str(incident.get("type", "")).lower()
        return self.known_incidents.get(incident_type, "unknown")
