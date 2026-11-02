import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME", "supply_chain_db"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

BATCH_SIZE = 10000