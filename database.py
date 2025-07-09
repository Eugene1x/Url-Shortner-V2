import sqlite3

conn = sqlite3.connect('urls.db', check_same_thread=False)
cursor = conn.cursor()


def createTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            code TEXT PRIMARY KEY,
            url TEXT NOT NULL
        )
    ''')
    conn.commit()

def insert_url(code: str, url: str):
    cursor.execute('INSERT OR IGNORE INTO urls (code, url) VALUES (?, ?)', (code, url))
    conn.commit()


def get_url(code: str):
    cursor.execute('SELECT url FROM urls WHERE code = ?', (code,))
    result = cursor.fetchone()
    return result[0] if result else None