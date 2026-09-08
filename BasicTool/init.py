import os
import subprocess
from pathlib import Path

set_env = os.environ.get("ASCEND_TOOLKIT_HOME", "/usr/local/Ascend/cann") + "/set_env.sh"
if not Path(set_env).exists():
    set_env = "/usr/local/Ascend/cann/set_env.sh"

result = subprocess.run(
    ["bash", "-lc", f"source {set_env} && env"],
    capture_output=True,
    text=True,
    check=True,
)
for line in result.stdout.strip().split("\n"):
    if "=" in line and not line.startswith(("#", " ")):
        key, value = line.split("=", 1)
        os.environ[key] = value

print("Environment initialization process completed successfully.")
