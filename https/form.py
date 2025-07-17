from flask import Blueprint, session, request, redirect, jsonify,url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash

user_api = Blueprint('user', __name__)

@user_api.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('client.home'))

@user_api.route('/login', methods=['GET','POST'])
def login():
    if request.method.upper() == 'POST':
        #Guarda as informações do login
        user = request.form['username']
        senha = request.form['password']
        from database.db import db_cmd
        #Lê o banco de dados e faz o processo de checagem
        db_cmd.execute("SELECT * FROM usuarios WHERE nome=?",  (user,))
        usuario = db_cmd.fetchone()
        if usuario and check_password_hash(usuario[2], senha):
            session['username'] = user
            return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200
        else:
            return jsonify({"mensagem": "Credenciais incorretas"}), 400
    #Vai pra página de login/cadastro caso for a primeira vez que entra
    else:
        return render_template('login.html')

@user_api.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method.upper() == 'POST':
        user = request.form['username']
        senha = request.form['password']

        #Leitura do banco + verificação
        from database.db import db_cmd, db_conn
        db_cmd.execute("SELECT * FROM usuarios WHERE nome=?",  (user,))
        usuario = db_cmd.fetchone()
        if usuario and check_password_hash(usuario[2], senha):
            return jsonify({"mensagem": "Usuário ja existe."}), 400
        
        #Após a verificação, insere no banco o novo user.
        else:
            db_cmd.execute("INSERT INTO usuarios (nome, senha) VALUES (?,?)", (user, generate_password_hash(senha)))
            db_conn.commit()

            #Após o processo, determina a sessão e envia o user pra página principal.
            session['username'] = user
            return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200
    #Retorna à página do cadastro/login caso não esteja enviando dados.
    else:
        return redirect(url_for('client.login'))