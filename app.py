from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/turma')
def turma():
    return render_template('turma.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)
