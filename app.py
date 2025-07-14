from flask import Flask
from https.routes import client_view
app = Flask(__name__, static_folder='style', template_folder='html')

app.secret_key = 'Rikatoki'
app.register_blueprint(client_view)

if __name__ == '__main__':
    app.run(debug=True)