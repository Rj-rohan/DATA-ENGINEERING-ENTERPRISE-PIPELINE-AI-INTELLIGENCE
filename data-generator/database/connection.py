import psycopg
from config.settings import DB_CONFIG

def get_connection():
    return psycopg.connect(**DB_CONFIG)