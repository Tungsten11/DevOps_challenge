from dotenv import load_dotenv
import os

# Load .env files
load_dotenv()

# Access environment variables
log_file = os.getenv("LOG_FILE")
mode = os.getenv("MODE")

print(f"Log file: {log_file}")
print(f"Running in {mode} mode.")
