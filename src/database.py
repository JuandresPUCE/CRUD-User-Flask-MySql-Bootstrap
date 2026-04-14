# conexion de BDD My SQL con python 
# capa de persistencia, se encarga de establecer la conexión con la base de datos y proporcionar un objeto de conexión que pueda ser utilizado por los repositorios para ejecutar consultas SQL. En este caso, se utiliza el conector MySQL oficial para Python (mysql-connector-python) para conectarse a una base de datos MySQL local.
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


