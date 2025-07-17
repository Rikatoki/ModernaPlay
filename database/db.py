import sqlite3
db_conn = sqlite3.connect(database='database/jogos.db', check_same_thread=False)
db_cmd = sqlite3.Cursor()

