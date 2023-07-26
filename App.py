from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "pi_flask"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/HolaU')
def HolaU():
    return render_template('HolaU.html')


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
                return redirect(url_for('HolaU'))
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect(url_for('index'))
        elif Vusuario == 'IvanManzoRuiz':
            if Vusuario in usu and usu[Vusuario] == Vpassword:
                session['nombre'] = Vusuario
                return redirect(url_for('HolaU'))
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
        nombreUs = request.form['id_usuario']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM registro_usuario WHERE nombre = %s', (nombreUs,))
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
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido_paterno']
        apellido_materno = request.form['apellido_materno']
        cargo = request.form['cargo']
        contraseña = request.form['contrasena']

        cursor = mysql.connection.cursor()

        cursor.execute('UPDATE registro_usuario SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, cargo=%s, contrasena=%s WHERE id=%s', (nombre, apellido_paterno, apellido_materno, cargo, contraseña, id_usuario))

        # Guardar los cambios en la base de datos
        mysql.connection.commit()
        flash('Usuario modificado correctamente')
        return render_template('Modificar_Usuario.html')

    return render_template('Modificar_Usuario.html')


@app.route('/Eliminar_Usuario', methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':
        vnombre = request.form['id_usuario']
        vap = request.form['apellido_paterno']
        Vma = request.form['apellido_mat']
        CS = mysql.connection.cursor()
        CS.execute('DELETE FROM registro_usuario WHERE nombre = %s AND apellido_paterno = %s AND apellido_materno = %s', (vnombre,vap,Vma))
        mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect(url_for('Eliminar_Usuario'))


@app.route('/RegistrarNCliente', methods=['POST'])
def RegistrarNCliente():
    if request.method == 'POST':
        Vnombre = request.form['NombreCli']
        Vap = request.form['ApellidoPCLI']
        Vam = request.form['ApellidoMCLI']
        Vrfc = request.form['RFCCLI']
        Vcalle = request.form['CalleCLI']
        Vni = request.form['NICLI']
        Vne = request.form['NECLI']
        Vcolonia = request.form['coloniaCLI']
        Vcp = request.form['CPCLI']
        Vdel = request.form['DELEGACIONCLI']
        Vciudad = request.form['CiudadCLI']
        Vestado = request.form['EstadoCLI']
        Vtelefono = request.form['TelefonoCLI']
        Vcorreo = request.form['correCLI']
        GC = mysql.connection.cursor()
        GC.execute('insert into registro_cliente(nombre, apellido_paterno, apellido_materno, RFC, calle, num_int, num_ext, colonia, codigo_postal, delegacion, ciudad, estado, telefono, correo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Vnombre,Vap,Vam,Vrfc,Vcalle,Vni,Vne,Vcolonia,Vcp,Vdel,Vciudad,Vestado,Vtelefono,Vcorreo))
        mysql.connection.commit()
    flash('Usuario Agregado Correctamente')
    return redirect(url_for('RegistrarCliente'))

@app.route('/Inciar_Tramite', methods=['POST'])
def Inciar_Tramite():
    if request.method == 'POST':
        VnumE = request.form['NumeroExpediente']
        VnumT = request.form['NumeroTomo']
        Vop = request.form['Operacion']
        Vcli = request.form['Cliente']
        IT = mysql.connection.cursor()
        IT.execute('insert into inicio_tramite(num_expediente, num_tomo, operacion, cliente) values (%s,%s,%s,%s)',(VnumE,VnumT,Vop,Vcli))
        mysql.connection.commit()
    flash('Datos de nuevo trámite agregados correctamente a la base de datos')
    return redirect(url_for('EditarTramite'))

@app.route('/Ingresar_pago', methods=['POST'])
def Ingresar_pago():
    if request.method == 'POST':
        VCant = request.form['CantidadPa']
        VTP = request.form['TipoPago']
        VFecha = request.form['FechaP']
        IP = mysql.connection.cursor()
        IP.execute('insert into IngresoPago(cantidad, tipo_pago, fecha) values (%s,%s,%s)',(VTP,VCant,VFecha))
        mysql.connection.commit()
    flash('Información del pago agregado correctamente a la base de datos')    
    return redirect(url_for('Ingresar_pago'))
        

@app.route('/buscartramite', methods=['POST'])
def buscar_tramite():
    if request.method == 'POST':
        num_expediente = request.form['NumeroExpediente']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM inicio_tramite WHERE num_expediente = %s', (num_expediente,))
        tramite = cursor.fetchone()

        if tramite:
            num_expediente = tramite[1]
            num_tomo = tramite[2]
            operacion = tramite[3]
            cliente = tramite[4]

            flash('Trámite encontrado')
            return render_template('BuscarTramite.html', num_expediente=num_expediente, num_tomo=num_tomo, operacion=operacion, cliente=cliente)
        else:
            flash('Trámite no encontrado')

    return render_template('BuscarTramite.html')

# modificar
@app.route('/buscarcliente', methods=['POST'])
def buscarcliente():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        apellido_paterno = request.form['ApellidoP']
        apellido_materno = request.form['ApellidoM']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM registro_cliente WHERE nombre = %s AND apellido_paterno = %s AND apellido_materno = %s', (nombre, apellido_paterno, apellido_materno))
        tramite = cursor.fetchone()

        if tramite:
            nombre = tramite[1]
            apellido_paterno = tramite[2]
            apellido_materno = tramite[3]
            RFC = tramite[4]
            calle = tramite[5]
            num_int = tramite[6]
            num_ext = tramite[7]
            colonia = tramite[8]
            codigo_postal = tramite[9]
            delegacion = tramite[10]
            ciudad = tramite[11]
            estado = tramite[12]
            telefono = tramite[13]
            correo = tramite[14]


            flash('Cliente encontrado')
            return render_template('BuscarCliente.html', nombre=nombre, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, RFC=RFC, calle=calle, num_int=num_int, num_ext=num_ext, colonia=colonia, codigo_postal=codigo_postal, delegacion=delegacion, ciudad=ciudad, estado=estado, telefono=telefono, correo=correo)
        else:
            flash('Trámite no encontrado')

    return render_template('BuscarCliente.html')


if __name__=='__main__':
    app.run(port= 9000, debug=True) #debug=true activaactualizacion 
