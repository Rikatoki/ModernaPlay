def create_database_user():
    from os import makedirs
    makedirs('database', exist_ok=True)
    with open('database/usuarios.json', 'w') as f:
        f.write('[]')

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*arg, **kwargs):
        from https.form import session
        if 'username' not in session:
            from flask import redirect,url_for
            return redirect(url_for('user.login'))
        return f(*arg, **kwargs)
    return decorated_function

def jogos():
    with open('database/jogos.json', 'r') as f:
        from json import load
        return load(f)