import psycopg2
from config import Config
import os

def init_db():
    # Read schema file
    with open('schema.sql', 'r') as f:
        schema = f.read()

    # Connect to database
    conn = psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    )
    
    try:
        with conn.cursor() as cur:
            # Execute schema
            cur.execute(schema)
            conn.commit()
            print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()