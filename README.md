# Incident Monitoring System

This repository contains a simple prototype for a monitoring system that detects and classifies incidents on servers and Docker containers.

## Components

- **Python** scripts under `src/main/python` are responsible for collecting metrics and logs, detecting incidents, and resolving them automatically if possible.
- **Java** application under `src/main/java` invokes the Python monitoring logic.

## Running

Ensure you have Python 3 and Java installed. Then run:

```bash
javac src/main/java/com/example/monitor/MonitorService.java
java -cp src/main/java com.example.monitor.MonitorService
```

This will execute the Python monitor once and print the JSON output describing any detected incidents.
