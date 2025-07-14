from flask import Blueprint, render_template, url_for, session, request, redirect, jsonify
from py.function import create_database_user, login_required, jogos
from werkzeug.security import check_password_hash, generate_password_hash
from json import load, dump, JSONDecodeError


client_view = Blueprint('client',__name__)

@client_view.route('/', methods=['GET','POST'])
def verif_login():
    return redirect(url_for('client.home'))
    
#login_required garante que o usuário tenha feito um login.
@client_view.route('/home')
@login_required
def home():
    return render_template('index.html', jogos=jogos())

@client_view.route('/loja')
@login_required
def loja():
    return render_template('loja.html',jogos=jogos())

@client_view.route('/sobre_nós')
@login_required
def sobre():
    return render_template('sobre.html')

@client_view.route('/login', methods=['GET','POST'])
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
                    jogos = jogos()
                    return jsonify({"redirect": url_for('client.home', username=session['username'], jogos=jogos())}), 200
            return jsonify({"mensagem": "Credenciais incorretas"}), 400
            
        #Cria a pasta e o arquivo do banco de dados caso ela não exista.
        except (FileNotFoundError, FileExistsError):
            create_database_user()
            return jsonify({"mensagem": "Pasta do banco de dados não encontrada, tente novamente."}), 400
    #Vai pra página de login/cadastro caso for a primeira vez que entra
    else:
        return render_template('login.html')

@client_view.route('/cadastro', methods=['GET', 'POST'])
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