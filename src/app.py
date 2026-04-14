from flask import Flask , render_template, request , redirect, url_for
# framework de flask para crear aplicaciones web en python
# pip install flask
# directorios de trabajo 
import os
# importar conexion a la base de datos
import database as db


# directorio de plantillas vistas
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#unir directorios
template_dir = os.path.join(template_dir,'src', 'templates')

# crear la aplicación de flask y render de index.html
app = Flask(__name__, template_folder=template_dir)

#rutas de la app

@app.route('/')
#vinculo de funcion con la ruta
def home():
    #cursor para seleccionar datos de la base de datos
    cursor = db.database.cursor()
    cursor.execute('SELECT * FROM users')
    myresult = cursor.fetchall()
    # a diccionario para enviar a la plantilla
    insert_object = [] # arreglo para almacenar los resultados de la consulta
    column_names = [column[0] for column in cursor.description] # obtener los nombres de las columnas de la consulta mediante for
    # recorrer los resultados de la consulta y agregar cada fila como un diccionario al arreglo insert_object
    for result in myresult:
        insert_object.append(dict(zip(column_names, result)))
    
    #cerrar el cursor
    cursor.close()
    
    return render_template('index.html ', data=insert_object) # enviar el arreglo insert_object a la plantilla index.html como variable data

# ruta para agregar un nuevo usuario a la base de datos
@app.route('/user_add', methods=['POST'])

def add_user():
    # datos del formulario
    user_name = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if user_name and name and password: # validar que los campos no estén vacíos
        # cursor para insertar datos en la base de datos
        cursor = db.database.cursor()
        sql = 'INSERT INTO users (username, name, password) VALUES (%s, %s, %s)'
        val = (user_name, name, password)
        cursor.execute(sql, val)
        db.database.commit() # confirmar la transacción
        cursor.close() # cerrar el cursor
    return redirect(url_for('home')) # redirigir a la página principal después de agregar el usuario

# ruta para eliminar un usuario de la base de datos
@app.route('/user_delete/<int:id>', methods=['POST'])

def delete_user(id):
    # cursor para eliminar datos de la base de datos
    cursor = db.database.cursor()
    sql = 'DELETE FROM users WHERE id = %s'
    val = (id,)
    cursor.execute(sql, val)
    db.database.commit() # confirmar la transacción
    cursor.close() # cerrar el cursor
    return redirect(url_for('home')) # redirigir a la página principal después de eliminar el usuario

#ruta de editar o actualizar un usuario de la base de datos
@app.route('/user_update/<int:id>', methods=['POST'])
def update_user(id):
    # datos del formulario
    user_name = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if user_name and name and password: # validar que los campos no estén vacíos
        # cursor para actualizar datos en la base de datos
        cursor = db.database.cursor()
        sql = 'UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s'
        val = (user_name, name, password, id)
        cursor.execute(sql, val)
        db.database.commit() # confirmar la transacción
        cursor.close() # cerrar el cursor
    return redirect(url_for('home')) # redirigir a la página principal después de actualizar el usuario






#ejecucion de la app
if __name__ == '__main__':
    app.run(debug=True, port=4001) # modo debug para desarrollo, no usar en producción


