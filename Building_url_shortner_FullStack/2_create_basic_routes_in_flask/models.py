import sqlite3

DB_NAME = 'database.db'


def get_connection():
    """Create a database connection and set row_factory to return dict-like rows."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database and create the URLs table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                visit_count INTEGER DEFAULT 0
            )
        ''')
        conn.commit()


def insert_url(original_url, short_code):
    """Insert a new URL and its short code into the database."""
    with get_connection() as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_code)
            VALUES (?, ?)
        ''', (original_url, short_code))
        conn.commit()


def get_url(short_code):
    """Retrieve a URL record by its short code."""
    with get_connection() as conn:
        cur = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,))
        return cur.fetchone()


def increment_visit_count(short_code):
    """Increment the visit count for a given short code."""
    with get_connection() as conn:
        conn.execute('''
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?
        ''', (short_code,))
        conn.commit()


def get_all_urls():
    """Retrieve all URLs ordered by ID (newest first)."""
    with get_connection() as conn:
        cur = conn.execute('''
            SELECT original_url, short_code, visit_count
            FROM urls
            ORDER BY id DESC
        ''')
        return cur.fetchall()


def delete_url_by_code(short_code):
    """Delete a URL record by its short code."""
    with get_connection() as conn:
        conn.execute('DELETE FROM urls WHERE short_code = ?', (short_code,))
        conn.commit()