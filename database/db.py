import sqlite3
db_conn = sqlite3.connect(database='database/usuarios.db', check_same_thread=False)
db_cmd = db_conn.cursor()