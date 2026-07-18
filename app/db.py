import logging
import sqlite3

DB_FILE = "/data/jkbot.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    logging.info("DB初期化開始")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS channel_personas (
        channel_id INTEGER PRIMARY KEY,
        persona TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    logging.info("DB初期化完了")
