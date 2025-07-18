from flask import Blueprint, render_template, url_for, redirect
from app.utils.file_utils import jogos_json
from app.services.auth_service import login_required



user_bp = Blueprint('client',__name__)

@user_bp.route('/', methods=['GET','POST'])
def verif_login():
    return redirect(url_for('client.home'))
    
#login_required garante que o usuário tenha feito um login.
@user_bp.route('/home')
@login_required
def home():
    return render_template('index.html', jogos=jogos_json())

@user_bp.route('/loja')
@login_required
def loja():
    return render_template('loja.html',jogos=jogos_json())

@user_bp.route('/sobre_nós')
@login_required
def sobre():
    return render_template('sobre.html')

@user_bp.route('/Contatos')
def redes():
    return render_template('redes.html')

@user_bp.route('/termos')
def termos():
    return render_template('termos.html')

@user_bp.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')

@user_bp.route('/produto/<nome>')
def produto_detalhe(nome):
    produtos = jogos_json()
    produto = next((p for p in produtos if p['nome'].lower().replace(" ", "-") == nome.lower()), None)
    return render_template('produto.html', produto=produto)