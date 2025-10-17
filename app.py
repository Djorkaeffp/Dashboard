from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/turma')
def turma():
    return render_template('turma.html')

@app.route('/cadastra_aluno')
def cadastra_aluno():
    return render_template('cadastra_alunos.html')

if __name__ == '__main__':
    app.run(debug=True)
