from flask import Flask
from https.routes import client_view
from https.form import user_api
from database.db import db_cmd, db_conn
app = Flask(__name__, static_folder='style', template_folder='html')
db_cmd.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               senha TEXT NOT NULL)
""")
db_conn.commit()

app.secret_key = 'Rikatoki'
app.register_blueprint(client_view)
app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=True)