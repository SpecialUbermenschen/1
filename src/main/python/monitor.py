"""Simple incident monitoring logic."""

import json
import os
import re
from typing import Optional, List

from ai_classifier import IncidentClassifier

class IncidentMonitor:
    """Monitor system metrics and logs to detect incidents."""

    def __init__(self):
        self.classifier = IncidentClassifier()
        self.incident_history = {
            "cpu": "Consider scaling up or optimizing running processes",
            "memory": "Check for memory leaks or increase available RAM",
            "error": "Inspect logs for stack traces or service issues",
        }

    def collect_metrics(self) -> dict:
        """Collect basic CPU and memory metrics."""
        metrics = {}
        if hasattr(os, "getloadavg"):
            metrics["cpu_load"] = os.getloadavg()[0]
        try:
            with open("/proc/meminfo") as f:
                meminfo = f.read()
            total = int(re.search(r"MemTotal:\s+(\d+)", meminfo).group(1))
            avail = int(re.search(r"MemAvailable:\s+(\d+)", meminfo).group(1))
            metrics["memory_percent"] = ((total - avail) / total) * 100
        except Exception:
            metrics["memory_percent"] = 0
        return metrics

    def collect_logs(self) -> List[str]:
        """Return last few lines from system log."""
        log_paths = ["/var/log/syslog", "/var/log/messages"]
        for path in log_paths:
            try:
                with open(path) as f:
                    return f.readlines()[-100:]
            except FileNotFoundError:
                continue
        return []

    def detect_incident(self, metrics: dict, logs: List[str]) -> Optional[dict]:
        """Detect basic incidents based on metrics and logs."""
        if metrics.get("cpu_load", 0) > 2:
            return {"type": "high_cpu", "metrics": metrics}
        if metrics.get("memory_percent", 0) > 80:
            return {"type": "high_memory", "metrics": metrics}
        for line in logs:
            if "ERROR" in line:
                return {"type": "error_log", "log": line.strip()}
        return None

    def classify_incident(self, incident: dict) -> str:
        """Classify incident using rule based classifier."""
        return self.classifier.classify(incident)

    def resolve_incident(self, classification: str) -> str:
        """Resolve incident automatically if known."""
        if classification in self.incident_history:
            return self.incident_history[classification]
        return "No automated resolution available"

    def monitor_loop(self):
        """Run monitoring cycle."""
        metrics = self.collect_metrics()
        logs = self.collect_logs()
        incident = self.detect_incident(metrics, logs)
        if incident:
            classification = self.classify_incident(incident)
            solution = self.resolve_incident(classification)
            print(json.dumps({"incident": incident, "class": classification, "solution": solution}))

if __name__ == "__main__":
    monitor = IncidentMonitor()
    monitor.monitor_loop()
