"""Subclass of detalleFrame, which is generated by wxFormBuilder."""

import wx
import UI
import pymysql.cursors
import config


# Implementing detalleFrame
class ControlAccesosdetalleFrame(UI.detalleFrame):
    def __init__(self, parent):
        UI.detalleFrame.__init__(self, parent)

    # Handlers for detalleFrame events.
    def obtenerDetalles(self, event):
        self.m_staticTextNombreUsuario.SetLabelText(config.usuarioSeleccionado)
        if not config.admin:
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

    def toggleAnydesk(self, event):
        # TODO: Implement toggleAnydesk
        pass

    def toggleGoogleDrive(self, event):
        # TODO: Implement toggleGoogleDrive
        pass
