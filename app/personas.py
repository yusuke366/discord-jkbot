from pathlib import Path

from .constants import PERSONA_FILES
from .db import get_connection

try:
    from .constants import PERSONA_FILES
    from .db import get_connection
except ImportError:
    from constants import PERSONA_FILES
    from db import get_connection


def load_persona(filename: str) -> str:
    persona_dir = Path(__file__).resolve().parent / "personas"
    with (persona_dir / filename).open(encoding="utf-8") as f:
        return f.read()

def save_channel_personas(channel_id, persona):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO channel_personas
    (channel_id, persona)
    VALUES (?, ?)
    """, (channel_id, persona))

    conn.commit()
    conn.close()

def load_channel_personas():
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        SELECT channel_id, persona
        FROM channel_personas
        """)

        return {
            row[0]: row[1]
            for row in cur.fetchall()
        }

channel_personas = load_channel_personas()