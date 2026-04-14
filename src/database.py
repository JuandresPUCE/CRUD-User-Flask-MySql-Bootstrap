# conexion de BDD My SQL con python
# py -m pip install mysql-connector-python==8.0.29
import mysql.connector

# conexion local mysql://root:admin@localhost:3306/bd_py_mysql

# conexion a la base de datos
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bd_py_mysql',
    port = 3306
)

# verificar la conexion
if database.is_connected():
    print('Conexion exitosa a la base de datos')
else:    print('Error al conectar a la base de datos')


