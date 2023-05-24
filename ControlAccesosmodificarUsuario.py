"""Subclass of modificarUsuario, which is generated by wxFormBuilder."""

import UI
import config


# Implementing modificarUsuario
class ControlAccesosmodificarUsuario(UI.modificarUsuario):
    def __init__(self, parent):
        UI.modificarUsuario.__init__(self, parent)

    # Handlers for modificarUsuario events.
    def Regresar(self, event):
        from ControlAccesosdetalleFrame import ControlAccesosdetalleFrame

        self.Close()
        frame = ControlAccesosdetalleFrame(None)
        frame.Show(True)

    def guardarCambios(self, event):
        config.ejecutarQueryUpdate(
            """
					UPDATE usuario
						JOIN area ON usuario.area = area.idarea
						SET usuario.nombreCompleto = %s,
							usuario.usuarioAD = %s,
							usuario.area = (SELECT idarea FROM area WHERE nombre = %s),
                            usuario.pais = (SELECT idpais FROM pais WHERE nombre = %s)
					WHERE usuario.idusuario = %s;
				""",
            (
                self.m_textCtrlNombreCompleto.GetValue(),
                self.m_textCtrlActiveDirectory.GetValue(),
                self.m_comboBoxArea.GetValue(),
                self.m_comboBoxPais.GetValue(),
                config.IDusuarioSeleccionado,
            ),
        )
        self.Regresar(self)

    def traerDatosParaFormulario(self, event):
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

        # obtener datos del usuario seleccionado para prellenar el formulario y realizar actualizaciones
        datosUsuario = config.ejecutarQueryLectura(
            """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
				FROM usuario u
				INNER JOIN area a ON u.area = a.idarea
				INNER JOIN pais p ON u.pais = p.idpais where u.idusuario = %s;""",
            config.IDusuarioSeleccionado,
        )

        self.m_textCtrlNombreCompleto.SetValue(datosUsuario[0]["nombreCompleto"])
        self.m_textCtrlActiveDirectory.SetValue(datosUsuario[0]["usuarioAD"])

        index_pais = self.m_comboBoxPais.FindString(datosUsuario[0]["pais"])
        self.m_comboBoxPais.SetSelection(index_pais)

        index_area = self.m_comboBoxArea.FindString(datosUsuario[0]["area"])
        self.m_comboBoxArea.SetSelection(index_area)
