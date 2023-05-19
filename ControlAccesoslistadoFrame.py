"""Subclass of listadoFrame, which is generated by wxFormBuilder."""

import wx
import UI
import pymysql.cursors
import config
from ControlAccesosdetalleFrame import ControlAccesosdetalleFrame


# Implementing listadoFrame
class ControlAccesoslistadoFrame(UI.listadoFrame):
    def __init__(self, parent):
        UI.listadoFrame.__init__(self, parent)

    # Handlers for listadoFrame events.
    def listarUsuarios(self, event):
        result = self.ejecutarQueryLectura(
            """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
		FROM usuario u
		INNER JOIN area a ON u.area = a.idarea
		INNER JOIN pais p ON u.pais = p.idpais;"""
        )
        if result:
            self.llenarTabla(result)
        else:
            print("Error al listarUsuarios")

    def Buscar(self, event):
        result = self.ejecutarQueryLectura(
            """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
		FROM usuario u
		INNER JOIN area a ON u.area = a.idarea
		INNER JOIN pais p ON u.pais = p.idpais
		WHERE u.nombreCompleto LIKE '%{}%';""".format(
                self.m_textCtrlBusqueda.GetValue().replace("%", "%%")
            )
        )
        if result:
            self.llenarTabla(result)
        else:
            print("Error al listarUsuarios")
        pass

    def mostrarDetalle(self, event):
        selected_row = self.m_dataViewListCtrlUsuarios.GetSelectedRow()
        usuario_ad = self.m_dataViewListCtrlUsuarios.GetValue(selected_row, 2)
        usuario_id = self.m_dataViewListCtrlUsuarios.GetValue(selected_row, 0)
        usuario_nombreCompleto = self.m_dataViewListCtrlUsuarios.GetValue(
            selected_row, 1
        )
        config.usuarioSeleccionado = usuario_ad
        config.IDusuarioSeleccionado = usuario_id
        config.usuarioSeleccionadoNombreCompleto = usuario_nombreCompleto
        self.Close()
        frame = ControlAccesosdetalleFrame(None)
        frame.Show(True)

    def CerrarSesion(self, event):
        from ControlAccesosautenticacionFrame import ControlAccesosautenticacionFrame

        config.limpiar()
        self.Close()
        frame = ControlAccesosautenticacionFrame(None)
        frame.Show(True)

    def llenarTabla(self, result):
        self.m_dataViewListCtrlUsuarios.DeleteAllItems()
        self.m_dataViewListCtrlUsuarios.ClearColumns()
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("idusuario")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("nombreCompleto")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("usuarioAD")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("area")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("pais")

        for j, item in enumerate(result):
            self.m_dataViewListCtrlUsuarios.AppendItem(
                [
                    str(item["idusuario"]),
                    item["nombreCompleto"],
                    item["usuarioAD"],
                    item["area"],
                    item["pais"],
                ]
            )

    def ejecutarQueryLectura(self, query, params=None):
        try:
            connection = pymysql.connect(
                host="localhost",
                user=config.usuario_actual,
                password=config.contrasena_actual,
                database="accesos",
                cursorclass=pymysql.cursors.DictCursor,
            )
            with connection:
                with connection.cursor() as cursor:
                    if params is not None:
                        cursor.execute(query, (params))
                    else:
                        cursor.execute(query)
            result = cursor.fetchall()

            if result:
                return result
            else:
                print("Error, result no tiene un valor valido.")
        except Exception as e:
            print(f"Error en ejecutarQueryLectura: {str(e)}")

    def CrearUsuario(self, event):
        from ControlAccesosmodificarUsuario import ControlAccesosmodificarUsuario

        self.Close()
        frame = ControlAccesosmodificarUsuario(None)
        frame.Show(True)
        pass
