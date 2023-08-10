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

@app.route('/pag_princ_usuario.html')
def ppu():
    return render_template('pag_princ_usuario.html')

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        Vusuario = request.form['Usuario']
        Vpassword = request.form['password']
        
        usu = {
            'ABCD123': 'Admin1',
            'EFGH123': 'Usuario1'
        }
        
        if Vusuario == 'ABCD123':
            if Vusuario in usu and usu[Vusuario] == Vpassword:
                session['usuario'] = Vusuario
                return redirect(url_for('HolaU'))
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect(url_for('index'))
        elif Vusuario == 'EFGH123':
            if Vusuario in usu and usu[Vusuario] == Vpassword:
                session['usuario'] = Vusuario
                return redirect(url_for('ppu'))
            else:
                flash('Usuario o contraseña incorrectos')
                return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('index'))
   
    # Si la solicitud es GET, renderiza la plantilla login.html
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

@app.route('/Registros.html')
def Registros():
    return render_template('Registros.html')

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

#@app.route('/Modificar_Usuario', methods=['POST'])
#def modificar_usuario():
    #if request.method == 'POST':
       # nombre = request.form['nombre']
       # apellido_paterno = request.form['apellido_paterno']
        #apellido_materno = request.form['apellido_materno']
        #cargo = request.form['cargo']
        #contraseña = request.form['contrasena']

       # cursor = mysql.connection.cursor()

        #cursor.execute('UPDATE registro_usuario SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, cargo=%s, contrasena=%s WHERE nombre=%s AND apellido_paterno=%s AND apellido_materno=%s', (nombre, apellido_paterno, apellido_materno, cargo, contraseña, nombre,apellido_paterno,apellido_materno))

        # Guardar los cambios en la base de datos
        #mysql.connection.commit()
       # flash('Usuario modificado correctamente')
        #return render_template('Modificar_Usuario.html')

    #return render_template('Modificar_Usuario.html')


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
        IT.execute('insert into inicio_tramite(num_expediente, num_tomo, operacion,id_cliente) values (%s,%s,%s,%s)',(VnumE,VnumT,Vop,Vcli))
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

@app.route('/vcarteraUsuarios') 
def cUsuarios():
    inv=mysql.connection.cursor()
    inv.execute('select * from registro_usuario')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_usuarios.html',listaUsuarios=consulta_inv)

@app.route('/vactualizar/<id>') 
def veditar(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from registro_usuario where id = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_usuario.html',usuarios=consulta)

@app.route('/actualizar/<id>',methods=['POST']) 
def actualizar(id): 
   if request.method == 'POST':
       _nombre=request.form['nombre']
       _AP=request.form['ApellidoP']
       _AM=request.form['ApellidoM']
       _cargo=request.form['Cargo']
       _password=request.form['password']

       curAct=mysql.connection.cursor()
       curAct.execute('update registro_usuario set nombre=%s, apellido_paterno=%s, apellido_materno=%s, cargo=%s, contrasena=%s where id = %s', (_nombre,_AP,_AM,_cargo,_password,id))
       mysql.connection.commit()

       flash('Datos del usuario actualizados en la base de datos correctamente')
       return redirect(url_for('cUsuarios'))

   
@app.route('/veliminar/<id>') 
def eliminarUsuario(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from registro_usuario where id = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('elim_usuario.html',usuarios=consulta)

@app.route('/eliminar/<id>',methods=['POST']) 
def eliminar(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from registro_usuario where id = %s',(id,))
      mysql.connection.commit()

    
    flash('Usuario eliminado correctamente')
    return redirect(url_for('cUsuarios'))

#ruta que envía a tabla de consulta clientes usuario
@app.route('/vcarteraClientes') 
def cClientes():
    inv=mysql.connection.cursor()
    inv.execute('select * from registro_cliente')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_clientes_usuario.html',listaClientes=consulta_inv)

#ruta que redirecciona a la vista "actualizar" cliente usuario
@app.route('/vactualizarC/<id>') 
def editarC(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from registro_cliente where id_cliente = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_cliente.html',clientes=consulta)

#ruta que realiza la consulta de actualizar cliente usuario en la BD
@app.route('/vactualizarCliente/<id>',methods=['POST']) 
def actualizarCliente(id): 
   if request.method == 'POST':
       _nombre=request.form['nombre']
       _AP=request.form['ApellidoP']
       _AM=request.form['ApellidoM']
       _rfc=request.form['RFC']
       _calle=request.form['Calle']
       _numint=request.form['numint']
       _numext=request.form['numext']
       _colonia=request.form['colonia']
       _cp=request.form['cp']
       _del=request.form['delegacion']
       _ciudad=request.form['ciudad']
       _estado=request.form['estado']
       _tel=request.form['telefono']
       _correo=request.form['correo']

       curAct=mysql.connection.cursor()
       curAct.execute('update registro_cliente set nombre=%s, apellido_paterno=%s, apellido_materno=%s, rfc=%s, calle=%s, num_int=%s, num_ext=%s,colonia=%s,codigo_postal=%s,delegacion=%s,ciudad=%s,estado=%s,telefono=%s,correo=%s where id_cliente = %s', (_nombre,_AP,_AM,_rfc,_calle,_numint,_numext,_colonia,_cp,_del,_ciudad,_estado,_tel,_correo,id))
       mysql.connection.commit()

       flash('Datos del cliente actualizados en la base de datos correctamente')
       return redirect(url_for('cClientes'))
   
@app.route('/veliminarC/<id>') 
def eliminarC(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from registro_cliente where id_cliente = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('elim_cliente.html',clientes=consulta)


@app.route('/eliminarCliente/<id>',methods=['POST']) 
def eliminarCliente(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from registro_cliente where id_cliente = %s',(id,))
      mysql.connection.commit()

    
    flash('Cliente eliminado correctamente')
    return redirect(url_for('cClientes'))


@app.route('/vinventarioTramites') 
def inventarioT():
    inv=mysql.connection.cursor()
    inv.execute('select * from inicio_tramite')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_tramites.html',listaTramites=consulta_inv)

@app.route('/vactualizarT/<id>') 
def editarT(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from inicio_tramite where id_tramite = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_tramite.html',tramites=consulta)

@app.route('/actualizarTram/<id>',methods=['POST']) 
def actualizarT(id): 
   if request.method == 'POST':
       _num_exp=request.form['num_exp']
       _num_tomo=request.form['num_tomo']
       _operacion=request.form['operacion']

       curAct=mysql.connection.cursor()
       curAct.execute('update inicio_tramite set num_expediente=%s, num_tomo=%s, operacion=%s where id_tramite = %s', (_num_exp,_num_tomo,_operacion,id))
       mysql.connection.commit()

       flash('Trámite actualizado correctamente')
       return redirect(url_for('inventarioT'))
   

#ruta catálogo pagos administrador
@app.route('/vinventarioPagos_a') 
def invPagos_a():
    inv=mysql.connection.cursor()
    inv.execute('select * from ingresopago')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_pagos_admin.html',listaPagos=consulta_inv)

#ruta para enviar a la vista de actualizar (desde en tabla de consulta)
@app.route('/vactualizarP_a/<id>') 
def vactualizarP_a(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from ingresopago where id_pago = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_pago_admin.html',pagos=consulta)

#ruta que realiza la acción de actualizar pago admin
@app.route('/actualizarP_a/<id>',methods=['POST']) 
def actualizar_p_a(id): 
   if request.method == 'POST':
       _cantidad=request.form['cantidad']
       _tipopago=request.form['tipo_pago']
       _fecha=request.form['fecha']
       

       curAct=mysql.connection.cursor()
       curAct.execute('update ingresopago set cantidad=%s, tipo_pago=%s, fecha=%s where id_pago = %s', (_cantidad,_tipopago,_fecha,id))
       mysql.connection.commit()

       flash('Datos del pago actualizados correctamente')
       return redirect(url_for('invPagos_a'))

#ruta catálogo pagos usuario
@app.route('/vinventarioPagos_u') 
def invPagos_u():
    inv=mysql.connection.cursor()
    inv.execute('select * from ingresopago')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_pagos_usuarios.html',listaPagos=consulta_inv)

#ruta para enviar a la vista de actualizar pago usuario (desde en tabla de consulta)
@app.route('/vactualizarP_u/<id>') 
def vactualizarP_u(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from ingresopago where id_pago = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_pago_usuario.html',pagos=consulta)

#ruta que realiza la acción de actualizar pago admin
@app.route('/actualizarP_u/<id>',methods=['POST']) 
def actualizar_p_u(id): 
   if request.method == 'POST':
       _cantidad=request.form['cantidad']
       _tipopago=request.form['tipo_pago']
       _fecha=request.form['fecha']
       

       curAct=mysql.connection.cursor()
       curAct.execute('update ingresopago set cantidad=%s, tipo_pago=%s, fecha=%s where id_pago = %s', (_cantidad,_tipopago,_fecha,id))
       mysql.connection.commit()

       flash('Datos del pago actualizados correctamente')
       return redirect(url_for('invPagos_u'))

#ruta que direcciona a la vista eliminar pago admin desde la tabla
@app.route('/veliminarP_a/<id>') 
def veliminarP_a(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from ingresopago where id_pago = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('eliminar_pago_admin.html',pagos=consulta)

#ruta que realiza la función de eliminar pago admin en BD
@app.route('/eliminarP_a/<id>',methods=['POST']) 
def eliminarP_a(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from ingresopago where id_pago = %s',(id,))
      mysql.connection.commit()

    
    flash('Pago eliminado correctamente')
    return redirect(url_for('invPagos_a'))

#ruta que direcciona a la vista eliminar pago usuario desde la tabla
@app.route('/veliminarP_u/<id>') 
def veliminarP_u(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from ingresopago where id_pago = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('eliminar_pago_usuario.html',pagos=consulta)

#ruta que realiza la función de eliminar pago usuario en BD
@app.route('/eliminarP_u/<id>',methods=['POST']) 
def eliminarP_u(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from ingresopago where id_pago = %s',(id,))
      mysql.connection.commit()

    
    flash('Pago eliminado correctamente')
    return redirect(url_for('invPagos_u'))

    #ruta que envía a tabla de consulta clientes admin
@app.route('/vcarteraClientes_a') 
def cClientes_a():
    inv=mysql.connection.cursor()
    inv.execute('select * from registro_cliente')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_clientes_admin.html',listaClientes=consulta_inv)

#ruta que redirecciona a la vista "actualizar" cliente admin
@app.route('/vactualizarC_a/<id>') 
def vactualizarC_a(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from registro_cliente where id_cliente = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_cliente_admin.html',clientes=consulta)

#ruta que realiza la consulta de actualizar cliente admin en la BD
@app.route('/actualizarCliente_a/<id>',methods=['POST']) 
def actualizarCliente_a(id): 
   if request.method == 'POST':
       _nombre=request.form['nombre']
       _AP=request.form['ApellidoP']
       _AM=request.form['ApellidoM']
       _rfc=request.form['RFC']
       _calle=request.form['Calle']
       _numint=request.form['numint']
       _numext=request.form['numext']
       _colonia=request.form['colonia']
       _cp=request.form['cp']
       _del=request.form['delegacion']
       _ciudad=request.form['ciudad']
       _estado=request.form['estado']
       _tel=request.form['telefono']
       _correo=request.form['correo']

       curAct=mysql.connection.cursor()
       curAct.execute('update registro_cliente set nombre=%s, apellido_paterno=%s, apellido_materno=%s, rfc=%s, calle=%s, num_int=%s, num_ext=%s,colonia=%s,codigo_postal=%s,delegacion=%s,ciudad=%s,estado=%s,telefono=%s,correo=%s where id_cliente = %s', (_nombre,_AP,_AM,_rfc,_calle,_numint,_numext,_colonia,_cp,_del,_ciudad,_estado,_tel,_correo,id))
       mysql.connection.commit()

       flash('Datos del cliente actualizados correctamente')
       return redirect(url_for('cClientes_a'))

#ruta que dirige a la vista de eliminar cliente admin desde la tabla de consulta   
@app.route('/veliminarC_a/<id>') 
def eliminarC_a(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from registro_cliente where id_cliente = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('elim_cliente_admin.html',clientes=consulta)

#ruta que realiza la consulta en la BD para eliminar cliente admin
@app.route('/eliminarCliente_a/<id>',methods=['POST']) 
def eliminarCliente_a(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from registro_cliente where id_cliente = %s',(id,))
      mysql.connection.commit()

    
    flash('Cliente eliminado correctamente')
    return redirect(url_for('cClientes_a'))

#ruta que dirige a la tabla de consulta de trámites admin
@app.route('/vinventarioTramites_a') 
def inventarioT_a():
    inv=mysql.connection.cursor()
    inv.execute('select * from inicio_tramite')
    mysql.connection.commit()

    consulta_inv=inv.fetchall() 
    return render_template('consulta_tramites_admin.html',listaTramites=consulta_inv)

#ruta que dirige a la vista de actualizar trámite desde la tabla
@app.route('/vactualizarT_a/<id>') 
def editarT_a(id):
    editar=mysql.connection.cursor()
    editar.execute('select * from inicio_tramite where id_tramite = %s',(id,))
    consulta=editar.fetchone() 
    return render_template('actualizar_tramite_admin.html',tramites=consulta)

#ruta que realiza la consulta en la BD para actualizar trámite admin
@app.route('/actualizarTram_a/<id>',methods=['POST']) 
def actualizarT_a(id): 
   if request.method == 'POST':
       _num_exp=request.form['num_exp']
       _num_tomo=request.form['num_tomo']
       _operacion=request.form['operacion']

       curAct=mysql.connection.cursor()
       curAct.execute('update inicio_tramite set num_expediente=%s, num_tomo=%s, operacion=%s where id_tramite = %s', (_num_exp,_num_tomo,_operacion,id))
       mysql.connection.commit()

       flash('Trámite actualizado correctamente')
       return redirect(url_for('inventarioT_a'))

#ruta que dirige a la vista de eliminar trámite admin desde la tabla
@app.route('/veliminarT_a/<id>') 
def veliminarT_a(id):
    eliminar=mysql.connection.cursor()
    eliminar.execute('select * from inicio_tramite where id_tramite = %s',(id,))
    consulta=eliminar.fetchone()
 
    return render_template('elim_tramite.html',tramites=consulta)

#ruta que realiza la consulta en la BD para eliminar un trámite admin
@app.route('/eliminarT_a/<id>',methods=['POST']) 
def eliminarT_a(id):
    if request.method=='POST':
      eliminar=mysql.connection.cursor()
      eliminar.execute('delete from inicio_tramite where id_tramite = %s',(id,))
      mysql.connection.commit()

    
    flash('Trámite eliminado correctamente')
    return redirect(url_for('inventarioT_a'))


if __name__=='__main__':
    app.run(port= 9000, debug=True) #debug=true activaactualizacion 
