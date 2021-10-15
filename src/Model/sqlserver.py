import pyodbc

CONN_STR = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=criareDB;UID=sa;PWD=-00388ut32Leo'
conn = pyodbc.connect(CONN_STR)
cursor = conn.cursor()


def insertSql(name, version, url, isActive):
    query = 'INSERT INTO MODULO (name, version, url, isActive) VALUES (?, ?, ?, ?)'
    cursor.execute(query, (name, version, url, isActive))
    conn.commit()
    print('Inserido com Sucesso!')


def updateSql(name, version, url, isActive, idModulo):
    query = 'UPDATE MODULO SET name=?, version=?, url=?, isActive=? WHERE idModulo=?'
    cursor.execute(query, (name, version, url, isActive, idModulo))
    conn.commit()
    print('Atualizado com Sucesso!')


def deleteSql(idModulo):
    query = 'DELETE FROM MODULO WHERE idModulo=?'
    cursor.execute(query, (idModulo,))
    conn.commit()
    print('Excluido com Sucesso!')





### Inserção:
#insertSql("PC-Count-6", 1, "http://127.0.0.1:8000/8478F87E-6E34-47C2-B378-07427751D059", True);

### Update:
#updateSql("PC-Count-6", 1, "http://127.0.0.1:8000/E5465105-963D-4060-84BA-F6C30CAF58AA", True, 'E5465105-963D-4060-84BA-F6C30CAF58AA');

# #Delete
# deleteSql('E5465105-963D-4060-84BA-F6C30CAF58AA')
#
#
# Select
# cursor.execute('SELECT * FROM MODULO')
# for row in cursor:
#     print('row = %r' % (row,))
#
