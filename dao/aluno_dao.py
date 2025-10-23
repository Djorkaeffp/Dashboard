from dao.db_config import get_connection

class alunoDAO:

    sqlSelect = ' SELECT id, nome, idade, cidade FROM aluno'

    def listar(self):
        conn = get_connection()
        cursor = conn.curso()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista