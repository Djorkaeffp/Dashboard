from flask import Flask, render_template
from dao.aluno_dao import alunoDAO
from dao.professor_dao import professorDAO
from dao.curso_dao import cursoDAO

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/curso')
def listar_curso():
    dao = cursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/aluno')
def listar_aluno():
    dao = alunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)


@app.route('/professor')
def listar_professor():
    dao = professorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)



if __name__ == '__main__':
    app.run(debug=True)
