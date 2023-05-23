"""Subclass of listadoFrame, which is generated by wxFormBuilder."""

import UI
import config
from ControlAccesosdetalleFrame import ControlAccesosdetalleFrame


# Implementing listadoFrame
class ControlAccesoslistadoFrame(UI.listadoFrame):
    def __init__(self, parent):
        UI.listadoFrame.__init__(self, parent)

    # Handlers for listadoFrame events.
    def listarUsuarios(self, event):
        result = config.ejecutarQueryLectura(
            """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
		FROM usuario u
		INNER JOIN area a ON u.area = a.idarea
		INNER JOIN pais p ON u.pais = p.idpais;"""
        )
        if result:
            self.llenarTabla(result)
        else:
            print("Error al listarUsuarios")

        # LLENAR COMBOBOX PAIS
        resultComboBoxPais = config.ejecutarQueryLectura(
            """SELECT nombre AS pais FROM pais;"""
        )
        self.m_comboBoxPais.Append("Todos")
        if resultComboBoxPais:
            for j, item in enumerate(resultComboBoxPais):
                self.m_comboBoxPais.Append(item["pais"])
        else:
            print("Error al listar Combobox")
        if not config.admin:
            self.m_buttonPanelControl.Enable(False)

        # LLENAR COMBOBOX AREA
        resultComboBoxPais = config.ejecutarQueryLectura(
            """SELECT nombre AS area FROM area;"""
        )
        self.m_comboBoxArea.Append("Todos")
        if resultComboBoxPais:
            for j, item in enumerate(resultComboBoxPais):
                self.m_comboBoxArea.Append(item["area"])
        else:
            print("Error al listar Combobox")
        if not config.admin:
            self.m_buttonPanelControl.Enable(False)

    def Buscar(self, event):
        query = """SELECT u.idusuario, u.nombreCompleto, u.usuarioAD, a.nombre AS area, p.nombre AS pais
		FROM usuario u
		INNER JOIN area a ON u.area = a.idarea
		INNER JOIN pais p ON u.pais = p.idpais
		WHERE u.nombreCompleto LIKE '%{}%'""".format(
            self.m_textCtrlBusqueda.GetValue().replace("%", "%%")
        )

        if self.m_comboBoxPais.GetValue() != "Todos":
            query += " AND p.nombre = '{}'".format(self.m_comboBoxPais.GetValue())

        if self.m_comboBoxArea.GetValue() != "Todos":
            query += " AND a.nombre = '{}'".format(self.m_comboBoxArea.GetValue())

        result = config.ejecutarQueryLectura(query)

        if result:
            self.llenarTabla(result)
        else:
            self.vaciarTabla()
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

    def vaciarTabla(self):
        self.m_dataViewListCtrlUsuarios.DeleteAllItems()
        self.m_dataViewListCtrlUsuarios.ClearColumns()
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("idusuario")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("nombreCompleto")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("usuarioAD")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("area")
        self.m_dataViewListCtrlUsuarios.AppendTextColumn("pais")

    def panelDeControl(self, event):
        from ControlAccesospanelDeControl import ControlAccesospanelDeControl

        self.Close()
        frame = ControlAccesospanelDeControl(None)
        frame.Show(True)
        pass

    def m_comboBoxAreaOnCombobox(self, event):
        self.Buscar(self)

    def m_comboBoxPaisOnCombobox(self, event):
        self.Buscar(self)
