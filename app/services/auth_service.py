#Function para garantir que a criatura fique logada nas coisas
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*arg, **kwargs):
        from app.routes.auth_routes import session
        if 'username' not in session:
            from flask import redirect,url_for
            return redirect(url_for('user.login'))
        return f(*arg, **kwargs)
    return decorated_function

#Function de verificação do login
def login_verif(nome:str, senha:str):
    from app import db
    from app.models import User
    from flask import jsonify, url_for, session
    from werkzeug.security import check_password_hash
    #Faz a requisição no banco e vê se as informações batem
    usuario = db.session.query(User).filter_by(nome=nome).first()
    if usuario and check_password_hash(usuario.senha, senha):
        session['username'] = nome
        return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200
    else:
        return jsonify({"mensagem": "Nome ou Senha incorretas. Tente novamente."}), 400
    
#Function para verificar o cadastro
def cadastro_verif(nome:str, senha:str):
    from werkzeug.security import generate_password_hash
    from flask import session, jsonify, url_for
    from app import db
    from app.models import User

    #Leitura do banco + verificação
    usuario = db.session.query(User).filter_by(nome=nome).first()
    if usuario:
        return jsonify({"mensagem": "Usuário ja existe."}), 400
    
    #Após a verificação, insere no banco o novo user.
    novo_user = User(nome=nome, senha=generate_password_hash(senha))
    db.session.add(novo_user)
    db.session.commit()
    #Após o processo, determina a sessão e envia o user pra página principal.
    session['username'] = nome
    return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200