from flask import Blueprint, session, request, redirect, jsonify,url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from json import load, dump, JSONDecodeError
from py.function import create_database_user

user = Blueprint('user', __name__)

@user.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('client.home'))

@user.route('/login', methods=['GET','POST'])
def login():
    if request.method.upper() == 'POST':
        #Guarda as informações do login
        user = request.form['username']
        senha = request.form['password']

        #Lê o banco de dados e faz o processo de checagem
        try:
            with open('database/usuarios.json', 'r') as data_users:
                try:
                    usuarios = load(data_users)
                except JSONDecodeError:
                    usuarios = []
            for u in usuarios:
                if user == u['username'] and check_password_hash(u['password'], senha):
                    session['username'] = user
                    return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200
            return jsonify({"mensagem": "Credenciais incorretas"}), 400
            
        #Cria a pasta e o arquivo do banco de dados caso ela não exista.
        except (FileNotFoundError, FileExistsError):
            create_database_user()
            return jsonify({"mensagem": "Pasta do banco de dados não encontrada, tente novamente."}), 400
    #Vai pra página de login/cadastro caso for a primeira vez que entra
    else:
        return render_template('login.html')

@user.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method.upper() == 'POST':
        user = request.form['username']
        senha = request.form['password']
        #Leitura do banco + verificação
        try:
            with open('database/usuarios.json', 'r') as data_user:
                try:
                    usuarios = load(data_user)
                except JSONDecodeError:
                    usuarios = []
            for u in usuarios:
                if u['username'] == user:
                    return jsonify({"mensagem": "Já existe um usuário com este nome."}), 400
            #Adiciona o novo usuário após a verificação e em seguida rescreve o banco com o novo user.
            usuarios.append({
                        "username": user,
                        "password": generate_password_hash(senha)
                    })
            with open('database/usuarios.json','w') as data_user_append:
                dump(
                    usuarios, data_user_append, indent=4
                )
            #Após o processo, determina a sessão e envia o user pra página principal.
            session['username'] = user
            return jsonify({"redirect": url_for('client.home', username= session['username'])}), 200
        #Tratamento de erro de arquivo inexistente.
        except (FileExistsError, FileNotFoundError):
            create_database_user()
            return jsonify({"mensagem": "Pasta do banco de dados não encontrada, tente novamente."}), 400
    #Retorna à página do cadastro/login caso não esteja enviando dados.
    else:
        return redirect(url_for('client.login'))