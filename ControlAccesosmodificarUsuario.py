"""Subclass of modificarUsuario, which is generated by wxFormBuilder."""

import UI
import config
import wx


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
        try:
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
            from pyad import pyad
            usuario = pyad.from_cn(self.m_textCtrlActiveDirectory.GetValue())
            usuario.update_attribute("givenName", self.m_textCtrlNombreDePila.GetValue())
            usuario.update_attribute("initials", self.m_textCtrlIniciales.GetValue())
            usuario.update_attribute("sn", self.m_textCtrlApellidos.GetValue())
            # usuario.update()
            wx.MessageBox("El usuario ha sido modificado correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)
        except Exception as e:
            wx.MessageBox("Ocurrió un error al modificar el usuario: {}".format(str(e)), "Error", wx.OK | wx.ICON_ERROR)
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

        #rellenar datos desde Active directory
        from pyad import pyad

        usuarioPyad = pyad.from_cn(datosUsuario[0]["usuarioAD"])
        self.m_textCtrlNombreDePila.SetValue(usuarioPyad.get_attribute("givenName")[0])
        self.m_textCtrlIniciales.SetValue(usuarioPyad.get_attribute("initials")[0])
        self.m_textCtrlApellidos.SetValue(usuarioPyad.get_attribute("sn")[0])

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
