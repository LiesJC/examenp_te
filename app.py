from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = '8dbe7b26953e32807b5edc08c9f0614d1e067ce92d7c943663be74acfdd09f17'

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

@app.route('/')
def index():
    return render_template('index.html', titulo="Portal Académico")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form.get('usuario')
        p = request.form.get('contrasena')
        
        if u in usuarios and usuarios[u] == p:
            session['usuario'] = u
            return redirect(url_for('cursos'))
        else:
            return render_template('login.html', error="Usuario o contraseña incorrectos.")
            
    return render_template('login.html')


@app.route('/cursos')
def cursos():
    u = session.get('usuario')
    lista_cursos = [
        {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
        {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
        {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
    ]
    return render_template('cursos.html', usuario=u, cursos=lista_cursos)

@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
