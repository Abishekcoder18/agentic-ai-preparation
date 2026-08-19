import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path(__file__).resolve().parent.parent / "logs" / "mcp_audit.json"


def log_tool_call(tool_name, arguments):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": tool_name,
        "arguments": arguments
    }

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")