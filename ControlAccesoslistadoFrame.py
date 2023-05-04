"""Subclass of listadoFrame, which is generated by wxFormBuilder."""

import wx
import UI
import pymysql.cursors
import config


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
                print(result)
            else:
                print("Error al listarUsuarios")
        except Exception as e:
            print(f"Error en listarUsuarios: {str(e)}")

    def Buscar(self, event):
        # TODO: Implement Buscar
        pass

    def mostrarDetalle(self, event):
        # TODO: Implement mostrarDetalle
        pass
