from flask import Flask, render_template
from dao.aluno_dao import alunoDAO

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

@app.route('/aluno')
def listar_aluno():
    dao = alunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)



if __name__ == '__main__':
    app.run(debug=True)
