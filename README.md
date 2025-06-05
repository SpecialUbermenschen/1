# Incident Monitoring System

This repository contains a small monitoring prototype.  It collects basic CPU and memory metrics from the host and scans the system log for error messages.  When an incident is detected it is classified and a suggested resolution is printed.

## Components

- **Python** scripts under `src/main/python` are responsible for collecting metrics and logs, detecting incidents, and resolving them automatically if possible.
- **Java** application under `src/main/java` invokes the Python monitoring logic.

## Running

Ensure you have Python 3 and Java installed.  No external Python packages are required.  Then run:

```bash
javac src/main/java/com/example/monitor/MonitorService.java
java -cp src/main/java com.example.monitor.MonitorService
```

This will execute the Python monitor once and print the JSON output describing any detected incidents.
