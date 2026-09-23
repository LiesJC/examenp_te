from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Portal Académico")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
