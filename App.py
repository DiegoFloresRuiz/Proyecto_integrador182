from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "Notaria--"

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

@app.route('/IngresoPago.html')
def IngresoPago():
    return render_template('IngresoPago.html')

if __name__=='__main__':
    app.run(port= 9000, debug=True) #debug=true activaactualizacion 
