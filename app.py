from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import alunoDAO
from dao.professor_dao import professorDAO
from dao.curso_dao import cursoDAO

app = Flask(__name__)
app.secret_key ="kf"


@app.route('/')
def home():
    return render_template('index.html')

# ---------------- CURSO ------------------

@app.route('/curso')
def listar_curso():
    dao = cursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)

@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso=None)

@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso():
    id = request.form.get("id")
    nome = request.form.get("nome")
    duracao = request.form.get("duracao")

    id = int(id) if id not in ("", None, "None") else None

    dao = cursoDAO()
    resultado = dao.salvar(id, nome, duracao)

    if resultado["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect("/curso")

@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = cursoDAO()
    curso = dao.buscar_por_id(id)
    if not curso:
        flash("Curso não encontrado!", "danger")
        return redirect('/curso')
    return render_template('curso/form.html', curso=curso)

@app.route('/curso/remover/<int:id>')
def remover_curso(id):
    dao = cursoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Curso removido com sucesso!", "success")
    else:
        flash("Erro: " + resultado["mensagem"], "danger")
    return redirect('/curso')







@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/aluno')
def listar_aluno():
    dao = alunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)


@app.route('/aluno/form')
def form_aluno():
    # Formulário vazio para cadastro
    return render_template('aluno/form.html', aluno=None)


@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno():
    id = request.form.get("id")  # agora o id vem do hidden no formulário
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']

    # Converte id para int quando existir
    id = int(id) if id not in (None, "", "None") else None

    dao = alunoDAO()
    result = dao.salvar(id, nome, idade, cidade)

    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')


@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = alunoDAO()
    aluno = dao.buscar_por_id(id)

    if not aluno:
        flash("Aluno não encontrado!", "danger")
        return redirect('/aluno')

    return render_template('aluno/form.html', aluno=aluno)

@app.route('/aluno/remover/<int:id>')
def remover_aluno(id):
    dao = alunoDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Aluno removido com sucesso!", "success")
    else:
        flash("Erro ao remover: " + resultado["mensagem"], "danger")

    return redirect('/aluno')






# ---------------- PROFESSOR ------------------

@app.route('/professor')
def listar_professor():
    dao = professorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)


@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=None)


@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor():
    id = request.form.get("id")
    nome = request.form["nome"]
    disciplina = request.form["disciplina"]

    id = int(id) if id not in ("", None, "None") else None

    dao = professorDAO()
    resultado = dao.salvar(id, nome, disciplina)

    if resultado["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect("/professor")


@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = professorDAO()
    professor = dao.buscar_por_id(id)

    if not professor:
        flash("Professor não encontrado!", "danger")
        return redirect('/professor')

    return render_template('professor/form.html', professor=professor)


@app.route('/professor/remover/<int:id>')
def remover_professor(id):
    dao = professorDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Professor removido com sucesso!", "success")
    else:
        flash("Erro: " + resultado["mensagem"], "danger")

    return redirect('/professor')



if __name__ == '__main__':
    app.run(debug=True)
