from flask import Blueprint, session, request, redirect,url_for, render_template


auth_bp = Blueprint('user', __name__)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('client.home'))

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method.upper() == 'POST':
        from app.services.auth_service import login_verif
        #Guarda as informações do login
        user = request.form['username']
        senha = request.form['password']
        return login_verif(user,senha)
    #Retorna à página de login/cadastro caso for não esteja recebendo dados.
    else:
        return render_template('login.html')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    #Ao tentar cadastrar, guarda as informações e faz a verificação.
    if request.method.upper() == 'POST':
        from app.services.auth_service import cadastro_verif
        user = request.form['username']
        senha = request.form['password']
        return cadastro_verif(user,senha)
    #Retorna à página do cadastro/login caso não esteja recebendo dados.
    else:
        return redirect(url_for('client.login'))