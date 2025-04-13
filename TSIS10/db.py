import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def get_user(username):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            return cur.fetchone()[0]

def get_last_score(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT level, score, saved_state FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
            return cur.fetchone()

def save_score(user_id, level, score, state_bytes):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO user_score (user_id, level, score, saved_state) VALUES (%s, %s, %s, %s)",
                (user_id, level, score, state_bytes)
            )
