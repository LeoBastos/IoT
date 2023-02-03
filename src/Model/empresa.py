import sqlite3


class EmpresaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, createdAt, modulos):
        consulta = 'INSERT OR IGNORE INTO Empresa (createdAt, modulos) VALUES (?, ?)'
        self.cursor.execute(consulta, (createdAt, modulos))
        self.conn.commit()

    def editar(self, createdAt):
        consulta = 'UPDATE OR IGNORE Empresa SET createdAt=?, WHERE id=?'
        self.cursor.execute(consulta, (createdAt, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM Empresa WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM Empresa')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM Empresa WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    empresa = EmpresaDB('/home/leonardo/PycharmProjects/Projeto/src/Model/db_***.db')
    #empresa.inserir('2021-10-10', 3)

    empresa.listar()
    #empresa.buscar('PC')

