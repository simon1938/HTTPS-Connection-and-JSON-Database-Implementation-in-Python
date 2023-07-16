from flask import Flask, request, render_template, redirect, session
import bcrypt
import json

app = Flask(__name__)
app.secret_key = 'the_key'  # Clé secrète pour la gestion des sessions

# Charger les utilisateurs depuis le fichier
def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

users = load_users()

@app.route('/', methods=['GET'])
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            return 'Nom d\'utilisateur déjà utilisé'

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        users[username] = hashed_password.decode()

        with open('users.json', 'w') as file:
            json.dump(users, file)

        return 'Inscription réussie. Bienvenue ' + username + '<br><a href="/login">Se connecter</a>'

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username not in users or not bcrypt.checkpw(password.encode(), users[username].encode()):
            return 'Nom d\'utilisateur ou mot de passe invalide'

        # Stocker l'utilisateur connecté dans une session
        session['username'] = username

        return 'Connexion réussie. Bienvenue ' + username + '<br><a href="/logout">Se déconnecter</a>'

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Effacer la session de l'utilisateur connecté
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':

    app.run(debug=True)

    # HTTPS version
    # context = ('server-public-key.pem', 'server-private-key.pem')
    # app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=context)

