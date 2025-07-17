from flask import Blueprint, render_template, url_for, redirect
from py.function import login_required, jogos



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

@client_view.route('/Contatos')
def redes():
    return render_template('redes.html')

@client_view.route('/termos')
def termos():
    return render_template('termos.html')

@client_view.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')