import time
import uuid
import datetime
import os

random_string = str(uuid.uuid4())
file_path = "/usr/src/app/files/log.txt"

# Ensure directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

while True:
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"{timestamp}: {random_string}"
    print(f"Writing: {log_entry}", flush=True)
    
    with open(file_path, "w") as f:
        f.write(log_entry)
        
    time.sleep(5)
