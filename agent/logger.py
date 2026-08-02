import json
import os

from config.settings import LOG_FILE


def log_iteration(log_data):
    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_data)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)