from app import db

class User(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    senha = db.Column(db.String(200), nullable=False)
    #Quando der print, retorna o __repr__
    def __repr__(self):
        return f'<{self.nome}>'