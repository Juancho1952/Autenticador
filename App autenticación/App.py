from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flask'

# Datos de usuario de ejemplo (simulando una base de datos)
USERS = {
    'admin': '12345',  # Usuario: Contraseña
    'user': 'password'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Verificar si el usuario está en la "base de datos"
    if username in USERS and USERS[username] == password:
        flash('¡Autenticación exitosa!', 'success')
        return redirect(url_for('success', username=username))
    else:
        flash('Autenticación fallida. Usuario o contraseña incorrectos.', 'danger')
        return redirect(url_for('home'))

@app.route('/success/<username>')
def success(username):
    return f'¡Bienvenido, {username}! Autenticación completada.'

if __name__ == '__main__':
    app.run(debug=True)
