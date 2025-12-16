import time
import uuid
import datetime

# Generate a random UUID string once upon startup
random_string = str(uuid.uuid4())

# Start an infinite loop to output the log
while True:
    # Get the current timestamp in ISO format
    timestamp = datetime.datetime.now().isoformat()
    
    # Print the timestamp and the random string
    # flush=True ensures the output is sent immediately to the console
    print(f"{timestamp}: {random_string}", flush=True)
    
    # Pause execution for 5 seconds
    time.sleep(5)
