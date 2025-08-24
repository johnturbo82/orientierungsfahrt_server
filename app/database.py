import sqlite3
from contextlib import contextmanager

DATABASE_FILE = "database.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_FILE)
    try:
        yield conn
    finally:
        conn.close()

def init_db() -> None:
    """Initialize the database."""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, title TEXT, base64_source TEXT)")
        c.execute("""
            CREATE TABLE IF NOT EXISTS turns (
                id INTEGER PRIMARY KEY, 
                order_num INTEGER, 
                image_name TEXT, 
                name TEXT, 
                description TEXT, 
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def write_images_to_db(images: dict[str, str]) -> None:
    """Write images to database"""
    init_db()
    with get_db_connection() as conn:
        c = conn.cursor()
        for title, base64_data in images.items():
            c.execute("SELECT id FROM images WHERE title = ?", (title,))
            if c.fetchone() is None:
                c.execute("INSERT INTO images (title, base64_source) VALUES (?, ?)", 
                         (title, base64_data))
                print(f"Inserted: {title}")
            else:
                c.execute("UPDATE images SET base64_source = ? WHERE title = ?", 
                         (base64_data, title))
                print(f"Updated: {title}")
        conn.commit()

def get_tours() -> list[Turn]:
    """Get all tours."""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM turns")
        rows = c.fetchall()
        return [Turn(**dict(row)) for row in rows]

def get_image_by_title(title: str) -> str | None:
    """Get image by title."""
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT base64_source FROM images WHERE title = ?", (title,))
        result = c.fetchone()
        return result[0] if result else None
