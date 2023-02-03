import sqlite3

con = sqlite3.connect('db_***.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE Empresa ('
	'id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
	'createdAt	TEXT,'
	'modulos	INTEGER NOT NULL,'
	'FOREIGN KEY("modulos") REFERENCES "Modulo"("idModulo")'
')')


#
# cursor.execute('CREATE TABLE Modulo ('
# 	'idModulo	INTEGER PRIMARY KEY AUTOINCREMENT,'
# 	'name TEXT,'
# 	'version	INTEGER,'
# 	'url	TEXT,'
# 	'isActive	TEXT'
# ')')





con.commit()

cursor.close()
con.close()
