from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "pi_flask"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)


@app.route('/Registro_Nuevo_Usuario.html')
def Registro_Nuevo_Usuario():
    return render_template('Registro_Nuevo_Usuario.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        Vusuario = request.form['nombre']
        Vpassword = request.form['password']
        
        usu = {
            'DiegoFloresRuiz': 'Admin1',
            'IvanManzoRuiz': 'Admin2'
        }
        
        if Vusuario == 'DiegoFloresRuiz':
            if Vusuario in usu and usu[Vusuario] == Vpassword:
                session['usuario'] = Vusuario
                return redirect(url_for('Registro_Nuevo_Usuario'))
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect(url_for('index'))
        elif Vusuario == 'IvanManzoRuiz':
            if Vusuario in usu and usu[Vusuario] == Vpassword:
                session['nombre'] = Vusuario
                return redirect(url_for('Registro_Nuevo_Usuario'))
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('index'))
    
    # Si la solicitud es GET, renderiza la plantilla index.html
    return render_template('index.html')

@app.route('/BuscarUsuario.html')
def BuscarUsuario():
    return render_template('BuscarUsuario.html')

@app.route('/Registro_Nuevo_Usuario.html')
def Registrar_Nuevo_Usuario():
    return render_template('Registro_Nuevo_Usuario.html')

@app.route('/Modificar_Usuario.html')
def Modificar_Usuario():
    return render_template('Modificar_Usuario.html')

@app.route('/Eliminar_Usuario.html')
def Eliminar_Usuario():
    return render_template('Eliminar_Usuario.html')


@app.route('/RegistrarCliente.html')
def RegistrarCliente():
    return render_template('RegistrarCliente.html')

@app.route('/ModificarCliente.html')
def ModificarCliente():
    return render_template('ModificarCliente.html')

@app.route('/EditarTramite.html')
def EditarTramite():
    return render_template('EditarTramite.html')


@app.route('/EliminarFactura.html')
def EliminarFactura():
    return render_template('EliminarFactura.html')


@app.route('/IngresoPago.html')
def IngresoPago():
    return render_template('IngresoPago.html')

@app.route('/BuscarTramite.html')
def BuscarTramite():
    return render_template('BuscarTramite.html')

@app.route('/BuscarCliente.html')
def BuscarCliente():
    return render_template('BuscarCliente.html')

@app.route('/Guargar', methods=['POST'])
def Guardar():
    if request.method == 'POST':
        Vnombre = request.form['nombre']
        Vap = request.form['ApellidoP']
        Vam = request.form['ApellidoM']
        Vcargo = request.form['Cargo']
        Vcontra = request.form['password']
        CS = mysql.connection.cursor()
        CS.execute('insert into registro_usuario(nombre,apellido_paterno,apellido_materno,cargo,contrasena) values (%s,%s,%s,%s,%s)',(Vnombre,Vap,Vam,Vcargo,Vcontra))
        mysql.connection.commit()
    flash('Usuario Agregado Correctamente')
    return redirect(url_for('Registrar_Nuevo_Usuario'))

@app.route('/buscarusuario', methods=['POST'])
def buscar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM registro_usuario WHERE id = %s', (id_usuario,))
        usuario = cursor.fetchone()

        if usuario:
            nombre = usuario[1]
            apellido_paterno = usuario[2]
            apellido_materno = usuario[3]

            flash('Usuario encontrado')
            return render_template('BuscarUsuario.html', nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno)
        else:
            flash('Usuario no encontrado')

    return render_template('BuscarUsuario.html')

@app.route('/Modificar_Usuario', methods=['POST'])
def modificar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM registro_usuario WHERE id = %s', (id_usuario,))
        usuario = cursor.fetchone()

        if usuario:
            nombre = usuario[1]
            apellido_paterno = usuario[2]
            apellido_materno = usuario[3]
            cargo = usuario[4]
            contraseña = usuario[5]

            flash('Usuario encontrado')
            return render_template('Modificar_Usuario.html', id_usuario=id_usuario, nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, cargo=cargo, contraseña=contraseña)
        else:
            flash('Usuario no encontrado')

    return render_template('Modificar_Usuario.html')

@app.route('/Eliminar_Usuario', methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':
        vid_usuario = request.form['id_usuario']
        CS = mysql.connection.cursor()
        CS.execute('DELETE FROM registro_usuario WHERE id = %s', (vid_usuario,))
        mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect(url_for('Eliminar_Usuario'))




        


if __name__=='__main__':
    app.run(port= 9000, debug=True) #debug=true activaactualizacion 
