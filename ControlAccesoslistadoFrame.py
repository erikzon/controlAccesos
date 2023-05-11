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
                    sql = """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
							FROM usuario u
							INNER JOIN area a ON u.area = a.idarea
							INNER JOIN pais p ON u.pais = p.idpais;"""
                    cursor.execute(sql)
            result = cursor.fetchall()

            if result:
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

            else:
                print("Error al listarUsuarios")
        except Exception as e:
            print(f"Error en listarUsuarios: {str(e)}")

    def Buscar(self, event):
        # TODO: Implement Buscar
        pass

    def mostrarDetalle(self, event):
        selected_row = self.m_dataViewListCtrlUsuarios.GetSelectedRow()
        usuario_ad = self.m_dataViewListCtrlUsuarios.GetValue(selected_row, 2)

        config.usuarioSeleccionado = usuario_ad
        self.Close()
        frame = ControlAccesosdetalleFrame(None)
        frame.Show(True)

    def CerrarSesion(self, event):
        from ControlAccesosautenticacionFrame import ControlAccesosautenticacionFrame

        config.limpiar()
        self.Close()
        frame = ControlAccesosautenticacionFrame(None)
        frame.Show(True)
