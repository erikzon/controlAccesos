"""Subclass of detalleFrame, which is generated by wxFormBuilder."""

import wx
import UI
import config


# Implementing detalleFrame
class ControlAccesosdetalleFrame(UI.detalleFrame):
    def __init__(self, parent):
        UI.detalleFrame.__init__(self, parent)

    def OnCheckBox(self, event):
        checkbox = event.GetEventObject()
        nombre_acceso = checkbox.GetLabel()
        valor_acceso = checkbox.GetValue()
        config.ejecutarQueryUpdate(
            """UPDATE usuario_acceso 
							SET valor_acceso = %s
							WHERE idusuario = %s AND id_acceso = (
							SELECT id_acceso FROM acceso WHERE nombre_acceso = %s);
							""",
            (
                int(valor_acceso),
                config.IDusuarioSeleccionado,
                nombre_acceso,
            ),
        )

    # Handlers for detalleFrame events.
    def obtenerDetalles(self, event):
        result = config.ejecutarQueryLectura(
            """SELECT p.nombre_acceso, up.valor_acceso
					FROM usuario AS u
					JOIN usuario_acceso AS up ON u.idusuario = up.idusuario
					JOIN acceso AS p ON up.id_acceso = p.id_acceso
				WHERE u.usuarioAD = %s;""",
            config.usuarioSeleccionado,
        )
        gbSizerDinamicoAccesos = wx.GridBagSizer(0, 0)
        gbSizerDinamicoAccesos.SetFlexibleDirection(wx.BOTH)
        gbSizerDinamicoAccesos.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        for i, acceso in enumerate(result):
            nombre = acceso["nombre_acceso"]
            valor = acceso["valor_acceso"]
            checkbox = wx.CheckBox(
                self, wx.ID_ANY, nombre, wx.DefaultPosition, wx.DefaultSize, 0
            )
            checkbox.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
            checkbox.SetValue(valor)

            gbSizerDinamicoAccesos.Add(
                checkbox, wx.GBPosition(i + 5, 0), wx.GBSpan(1, 1), wx.ALL, 5
            )
        self.SetSizer(gbSizerDinamicoAccesos)

        datosUsuario = config.ejecutarQueryLectura(
            """SELECT u.nombreCompleto, u.usuarioAD
				FROM usuario u
				WHERE u.idusuario = %s;""",
            config.IDusuarioSeleccionado,
        )
        self.m_staticTextNombreUsuario.SetLabelText(datosUsuario[0]["usuarioAD"])
        self.m_staticText9NombreCopleto.SetLabelText(datosUsuario[0]["nombreCompleto"])

        # si no es admin deshabilitar los checkbox y no permitir eliminar y editar un usuario:
        if not config.admin:
            self.m_buttonEliminarUsuario.Enable(False)
            self.m_buttonEditarUsuario.Enable(False)
            for control in self.GetChildren():
                if isinstance(control, wx.CheckBox):
                    control.Enable(False)

        # from pyad import pyad
        # user = pyad.from_cn(config.usuarioSeleccionado)
        # status = user.get_user_account_control_settings()
        # if status["ACCOUNTDISABLE"]:
        #     self.m_checkBoxToggleActiveDirectory.SetValue(False)
        #     self.m_checkBoxToggleActiveDirectory.SetLabel(
        #         "Usuario Deshabilitado en Active Directory"
        #     )
        # else:
        #     self.m_checkBoxToggleActiveDirectory.SetValue(True)
        #     self.m_checkBoxToggleActiveDirectory.SetLabel(
        #         "Usuario Habilitado en Active Directory"
        #     )

    def regresar(self, event):
        from ControlAccesoslistadoFrame import ControlAccesoslistadoFrame

        self.Close()
        frame = ControlAccesoslistadoFrame(None)
        frame.Show(True)
        pass

    def toggleActiveDirectory(self, event):
        # from pyad import pyad
        # user = pyad.from_cn(config.usuarioSeleccionado)
        # status = user.get_user_account_control_settings()
        # if status["ACCOUNTDISABLE"]:
        #     user.enable()
        #     self.m_checkBoxToggleActiveDirectory.SetLabel(
        #         "Usuario Deshabilitado en Active Directory"
        #     )
        # else:
        #     user.disable()
        #     self.m_checkBoxToggleActiveDirectory.SetLabel(
        #         "Usuario Habilitado en Active Directory"
        #     )
        pass

    def editarUsuario(self, event):
        from ControlAccesosmodificarUsuario import ControlAccesosmodificarUsuario

        self.Close()
        frame = ControlAccesosmodificarUsuario(None)
        frame.Show(True)
