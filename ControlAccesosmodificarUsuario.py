"""Subclass of modificarUsuario, which is generated by wxFormBuilder."""

import wx
import UI


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
        # TODO: Implement guardarCambios
        pass
