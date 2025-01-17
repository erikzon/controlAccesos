"""Subclass of panelDeControl, which is generated by wxFormBuilder."""

import config
import UI
import wx


# Implementing panelDeControl
class ControlAccesospanelDeControl(UI.panelDeControl):
	def __init__(self, parent):
		UI.panelDeControl.__init__(self, parent)

	# Handlers for panelDeControl events.
	def inicializarPanelDeControl(self, event):
		# llenar comboBox Pais
		datosPais = config.ejecutarQueryLectura("""SELECT nombre AS pais FROM pais;""")
		if datosPais:
			for i, item in enumerate(datosPais):
				self.m_comboBoxPais.Append(item["pais"])
		else:
			print("Error al listar Combobox pais")

		# llenar comboBox Area
		datosArea = config.ejecutarQueryLectura("""SELECT nombre AS area FROM area;""")
		if datosArea:
			for j, item in enumerate(datosArea):
				self.m_comboBoxArea.Append(item["area"])
		else:
			print("Error al listar Combobox area")
		pass

	# llenar comboBox Area
		datosPermisos = config.ejecutarQueryLectura("""SELECT nombre_acceso FROM acceso;""")
		if datosPermisos:
			for j, item in enumerate(datosPermisos):
				self.m_comboBoxPermisos.Append(item["nombre_acceso"])
		else:
			print("Error al listar Combobox accesos")
		pass
		

	def Regresar(self, event):
		from ControlAccesoslistadoFrame import ControlAccesoslistadoFrame

		self.Close()
		frame = ControlAccesoslistadoFrame(None)
		frame.Show(True)

	def CrearUsuario(self, event):
		
		from pyad import pyad
		#El componente de dominio (dc) del usuario 'pruebaAdmin' es: ['CN=pruebaAdmin,CN=Users,DC=analisis,DC=local']
		try:
			ou = pyad.adcontainer.ADContainer.from_dn("CN=Users,DC=analisis,DC=local") 
			new_user = pyad.aduser.ADUser.create(
				self.m_textCtrlActiveDirectory.GetValue(),
				ou,
				password=self.m_textCtrlContrasena.GetValue(),
				optional_attributes={
				"givenName" : self.m_textCtrlNombreDePila.GetValue(),
				"initials" : self.m_textCtrlIniciales.GetValue(),
				"sn" : self.m_textCtrlApellidos.GetValue(),
				}
			)
			# Crear el usuario en Active Directory
			
			# Crear el usuario en Base de datos
			config.ejecutarQueryInsert(
				"""
					INSERT INTO usuario (nombreCompleto, usuarioAD, area, pais)
					VALUES (%s, %s, (SELECT idarea FROM area WHERE nombre = %s), (SELECT idpais FROM pais WHERE nombre = %s));
				""",
				(
					self.m_textCtrlNombreCompleto.GetValue(),
					self.m_textCtrlActiveDirectory.GetValue(),
					self.m_comboBoxArea.GetValue(),
					self.m_comboBoxPais.GetValue(),
				),
			)

			IDusuarioRecienCreado = config.ejecutarQueryLectura(
				"""SELECT idusuario FROM usuario where usuarioAD = %s;""",
				self.m_textCtrlActiveDirectory.GetValue(),
			)

			config.usuarioSeleccionado = self.m_textCtrlActiveDirectory.GetValue()
			config.IDusuarioSeleccionado = IDusuarioRecienCreado[0]["idusuario"]
			config.usuarioSeleccionadoNombreCompleto = (
				self.m_textCtrlNombreCompleto.GetValue()
			)
			wx.MessageBox("El usuario ha sido creado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
			self.Close()
			from ControlAccesosdetalleFrame import ControlAccesosdetalleFrame

			frame = ControlAccesosdetalleFrame(None)
			frame.Show(True)

		except Exception as e:
			wx.MessageBox("Ocurrió un error al crear el usuario en Active Directory: {}".format(str(e)), "Error", wx.OK | wx.ICON_ERROR)
			
		

	def validarBotonCrear(self, event):
		# el boton Crear usuario solo se activara si todos los text_ctrl tienen un valor
		text_ctrls = [
			control
			for control in self.GetChildren()
			if isinstance(control, wx.TextCtrl)
		]
		enable_button = all(len(text_ctrl.GetValue()) > 1 for text_ctrl in text_ctrls)

		self.m_buttonCrearUsuario.Enable(enable_button)

	def moverSiguiente(self, event):
		if event.GetKeyCode() == wx.WXK_TAB:
			focus_ctrl = self.FindFocus()
			if focus_ctrl is self.m_textCtrlNombreCompleto:
				self.m_textCtrlActiveDirectory.SetFocus()
			elif focus_ctrl is self.m_textCtrlActiveDirectory:
				self.m_textCtrlNombreDePila.SetFocus()
			elif focus_ctrl is self.m_textCtrlNombreDePila:
				self.m_textCtrlIniciales.SetFocus()
			elif focus_ctrl is self.m_textCtrlIniciales:
				self.m_textCtrlApellidos.SetFocus()
			elif focus_ctrl is self.m_textCtrlApellidos:
				self.m_textCtrlNombreCompleto.SetFocus()
		event.Skip()

	def eliminarPermiso(self, event):
		try:
			config.ejecutarQueryDelete(
			"""DELETE FROM acceso WHERE nombre_acceso = %s;""",
			self.m_comboBoxPermisos.GetValue(),
			)
			
			wx.MessageBox("El permiso ha sido eliminado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
			# llenar comboBox Area
			self.m_comboBoxPermisos.Clear()
			datosPermisos = config.ejecutarQueryLectura("""SELECT nombre_acceso FROM acceso;""")
			if datosPermisos:
				for j, item in enumerate(datosPermisos):
					self.m_comboBoxPermisos.Append(item["nombre_acceso"])
			else:
				print("Error al listar Combobox accesos")
			pass
		except Exception as e:
			wx.MessageBox("Ocurrió un error al eliminar el permiso: {}".format(str(e)), "Error", wx.OK | wx.ICON_ERROR)


	def crearPermiso(self, event):
		config.ejecutarQueryInsert(
			"""
				INSERT INTO acceso (nombre_acceso) VALUES (%s);
			""",
			(
				self.m_textCtrlNombreNuevoPermiso.GetValue(),
			),
		)
		wx.MessageBox("El permiso ha sido creado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
		# llenar comboBox Area
		self.m_comboBoxPermisos.Clear()
		datosPermisos = config.ejecutarQueryLectura("""SELECT nombre_acceso FROM acceso;""")
		if datosPermisos:
			for j, item in enumerate(datosPermisos):
				self.m_comboBoxPermisos.Append(item["nombre_acceso"])
		else:
			print("Error al listar Combobox accesos")
		pass
		self.m_textCtrlNombreNuevoPermiso.SetValue('')