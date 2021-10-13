import sqlite3


class ModuloDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()


    def inserir(self, name, version, url, isActive):
        consulta = 'INSERT OR IGNORE INTO modulo (name, version, url, isActive) VALUES (?, ?, ?, ?)'
        self.cursor.execute(consulta, (name, version, url, isActive))
        self.conn.commit()


    def editar(self, name, version, url, isActive, id):
        consulta = 'UPDATE OR IGNORE Modulo SET name=?, version=?, url=?, isActive=? WHERE id=?'
        self.cursor.execute(consulta, (name, version, url, isActive, id))
        self.conn.commit()


    def excluir(self, id):
        consulta = 'DELETE FROM Modulo WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()


    def listar(self):
        self.cursor.execute('SELECT * FROM Modulo')

        for linha in self.cursor.fetchall():
            print(linha)


    def buscar(self, valor):
        consulta = 'SELECT * FROM Modulo WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)


    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    modulo = ModuloDB('db_criare.db')
    ########### Id, Nome, Versão, Url, isActive
    #modulo.inserir('PCCOUNT2', 3, 'http://127.0.0.1/', True)
    modulo.listar()
    #modulo.buscar(1)

