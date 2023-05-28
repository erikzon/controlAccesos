# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class autenticacionFrame
###########################################################################

class autenticacionFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Autenticación", pos = wx.DefaultPosition, size = wx.Size( 491,227 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.Colour( 247, 247, 247 ) )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Autenticacion", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticTextMensajeError = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextMensajeError.Wrap( -1 )

        self.m_staticTextMensajeError.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

        bSizer2.Add( self.m_staticTextMensajeError, 0, wx.ALL, 5 )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.VERTICAL )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gbSizer5.Add( self.m_staticText6, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrlUsuario = wx.TextCtrl( self, wx.ID_ANY, u"administradorAccesos", wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
        self.m_textCtrlUsuario.SetMaxLength( 150 )
        gbSizer5.Add( self.m_textCtrlUsuario, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Contrasena", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gbSizer5.Add( self.m_staticText7, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlContrasena = wx.TextCtrl( self, wx.ID_ANY, u"4125", wx.DefaultPosition, wx.Size( 240,-1 ), wx.TE_PASSWORD )
        self.m_textCtrlContrasena.SetMaxLength( 150 )
        gbSizer5.Add( self.m_textCtrlContrasena, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_buttonLogin = wx.Button( self, wx.ID_ANY, u"Acceder", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gbSizer5.Add( self.m_buttonLogin, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer2.Add( gbSizer5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.obtenerDatosMySQL )
        self.m_textCtrlUsuario.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlContrasena.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_buttonLogin.Bind( wx.EVT_BUTTON, self.iniciarSesion )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def obtenerDatosMySQL( self, event ):
        event.Skip()

    def moverSiguiente( self, event ):
        event.Skip()


    def iniciarSesion( self, event ):
        event.Skip()


###########################################################################
## Class listadoFrame
###########################################################################

class listadoFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usuarios", pos = wx.DefaultPosition, size = wx.Size( 627,545 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 244, 244, 244 ) )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button4CerrarSesion = wx.Button( self, wx.ID_ANY, u"Cerrar Sesion", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_button4CerrarSesion, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Pais:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        gbSizer4.Add( self.m_staticText18, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBoxPaisChoices = []
        self.m_comboBoxPais = wx.ComboBox( self, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize, m_comboBoxPaisChoices, 0 )
        gbSizer4.Add( self.m_comboBoxPais, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Area:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        gbSizer4.Add( self.m_staticText19, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        m_comboBoxAreaChoices = []
        self.m_comboBoxArea = wx.ComboBox( self, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize, m_comboBoxAreaChoices, 0 )
        gbSizer4.Add( self.m_comboBoxArea, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Busqueda por nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer4.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlBusqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer4.Add( self.m_textCtrlBusqueda, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_buttonBuscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_buttonBuscar, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonPanelControl = wx.Button( self, wx.ID_ANY, u"Panel de Control", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        gbSizer4.Add( self.m_buttonPanelControl, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        gbSizer9 = wx.GridBagSizer( 0, 0 )
        gbSizer9.SetFlexibleDirection( wx.BOTH )
        gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_dataViewListCtrlUsuarios = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_dataViewListCtrlUsuarios.SetMinSize( wx.Size( 600,400 ) )

        gbSizer9.Add( self.m_dataViewListCtrlUsuarios, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        gbSizer4.Add( gbSizer9, wx.GBPosition( 3, 0 ), wx.GBSpan( 5, 5 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        self.SetSizer( gbSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.listarUsuarios )
        self.m_button4CerrarSesion.Bind( wx.EVT_BUTTON, self.CerrarSesion )
        self.m_comboBoxPais.Bind( wx.EVT_COMBOBOX, self.m_comboBoxPaisOnCombobox )
        self.m_comboBoxArea.Bind( wx.EVT_COMBOBOX, self.m_comboBoxAreaOnCombobox )
        self.m_textCtrlBusqueda.Bind( wx.EVT_CHAR_HOOK, self.detectarEnter )
        self.m_buttonBuscar.Bind( wx.EVT_BUTTON, self.Buscar )
        self.m_buttonPanelControl.Bind( wx.EVT_BUTTON, self.panelDeControl )
        self.m_dataViewListCtrlUsuarios.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.mostrarDetalle, id = wx.ID_ANY )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def listarUsuarios( self, event ):
        event.Skip()

    def CerrarSesion( self, event ):
        event.Skip()

    def m_comboBoxPaisOnCombobox( self, event ):
        event.Skip()

    def m_comboBoxAreaOnCombobox( self, event ):
        event.Skip()

    def detectarEnter( self, event ):
        event.Skip()

    def Buscar( self, event ):
        event.Skip()

    def panelDeControl( self, event ):
        event.Skip()

    def mostrarDetalle( self, event ):
        event.Skip()


###########################################################################
## Class detalleFrame
###########################################################################

class detalleFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Informacion de Accesos", pos = wx.DefaultPosition, size = wx.Size( 533,511 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nombre de Usuario en Active Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gbSizer5.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonRegresar = wx.Button( self, wx.ID_ANY, u"Regresar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonRegresar, wx.GBPosition( 20, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonEliminarUsuario = wx.Button( self, wx.ID_ANY, u"Eliminar Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonEliminarUsuario, wx.GBPosition( 20, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_buttonEditarUsuario = wx.Button( self, wx.ID_ANY, u"Editar Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonEditarUsuario, wx.GBPosition( 20, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticTextNombreUsuario = wx.StaticText( self, wx.ID_ANY, u"<nombre usuario>", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextNombreUsuario.Wrap( -1 )

        gbSizer5.Add( self.m_staticTextNombreUsuario, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre Completo:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer5.Add( self.m_staticText8, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText9NombreCopleto = wx.StaticText( self, wx.ID_ANY, u"<nombre completo>", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9NombreCopleto.Wrap( -1 )

        gbSizer5.Add( self.m_staticText9NombreCopleto, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer51 = wx.GridBagSizer( 0, 0 )
        gbSizer51.SetFlexibleDirection( wx.BOTH )
        gbSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_checkBoxToggleActiveDirectory = wx.CheckBox( self, wx.ID_ANY, u"Activar/Desactivar Usuario en Active Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer51.Add( self.m_checkBoxToggleActiveDirectory, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )


        gbSizer5.Add( gbSizer51, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        self.SetSizer( gbSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.obtenerDetalles )
        self.m_buttonRegresar.Bind( wx.EVT_BUTTON, self.regresar )
        self.m_buttonEliminarUsuario.Bind( wx.EVT_BUTTON, self.eliminarUsuario )
        self.m_buttonEditarUsuario.Bind( wx.EVT_BUTTON, self.editarUsuario )
        self.m_checkBoxToggleActiveDirectory.Bind( wx.EVT_CHECKBOX, self.toggleActiveDirectory )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def obtenerDetalles( self, event ):
        event.Skip()

    def regresar( self, event ):
        event.Skip()

    def eliminarUsuario( self, event ):
        event.Skip()

    def editarUsuario( self, event ):
        event.Skip()

    def toggleActiveDirectory( self, event ):
        event.Skip()


###########################################################################
## Class modificarUsuario
###########################################################################

class modificarUsuario ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Modificar Usuario", pos = wx.DefaultPosition, size = wx.Size( 500,275 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Nombre Completo:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gbSizer6.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlNombreCompleto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlNombreCompleto, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Usuario Active Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gbSizer6.Add( self.m_staticText12, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Iniciales:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        gbSizer6.Add( self.m_staticText15, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlIniciales = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlIniciales, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrlActiveDirectory = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlActiveDirectory, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticTextNombreDePila = wx.StaticText( self, wx.ID_ANY, u"Nombre de Pila:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextNombreDePila.Wrap( -1 )

        gbSizer6.Add( self.m_staticTextNombreDePila, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlNombreDePila = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlNombreDePila, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Area de empresa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        gbSizer6.Add( self.m_staticText13, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Apellidos:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        gbSizer6.Add( self.m_staticText17, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlApellidos = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlApellidos, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Pais:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gbSizer6.Add( self.m_staticText14, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_buttonRegresar = wx.Button( self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonRegresar, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_buttonGuardarCambios = wx.Button( self, wx.ID_ANY, u"Guardar Cambios y volver", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonGuardarCambios, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        m_comboBoxPaisChoices = []
        self.m_comboBoxPais = wx.ComboBox( self, wx.ID_ANY, u"Guatemala", wx.DefaultPosition, wx.DefaultSize, m_comboBoxPaisChoices, 0 )
        gbSizer6.Add( self.m_comboBoxPais, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_comboBoxAreaChoices = []
        self.m_comboBoxArea = wx.ComboBox( self, wx.ID_ANY, u"IT", wx.DefaultPosition, wx.DefaultSize, m_comboBoxAreaChoices, 0 )
        gbSizer6.Add( self.m_comboBoxArea, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.SetSizer( gbSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.traerDatosParaFormulario )
        self.m_textCtrlNombreCompleto.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlIniciales.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlActiveDirectory.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlNombreDePila.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlApellidos.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_buttonRegresar.Bind( wx.EVT_BUTTON, self.Regresar )
        self.m_buttonGuardarCambios.Bind( wx.EVT_BUTTON, self.guardarCambios )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def traerDatosParaFormulario( self, event ):
        event.Skip()

    def moverSiguiente( self, event ):
        event.Skip()





    def Regresar( self, event ):
        event.Skip()

    def guardarCambios( self, event ):
        event.Skip()


###########################################################################
## Class panelDeControl
###########################################################################

class panelDeControl ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Panel de Control", pos = wx.DefaultPosition, size = wx.Size( 491,516 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"CREAR USUARIO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )

        gbSizer6.Add( self.m_staticText36, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Nombre Completo:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gbSizer6.Add( self.m_staticText11, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlNombreCompleto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlNombreCompleto, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Usuario Active Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gbSizer6.Add( self.m_staticText12, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlActiveDirectory = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlActiveDirectory, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticTextNombreDePila = wx.StaticText( self, wx.ID_ANY, u"Nombre de Pila:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextNombreDePila.Wrap( -1 )

        gbSizer6.Add( self.m_staticTextNombreDePila, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlNombreDePila = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlNombreDePila, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Iniciales:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        gbSizer6.Add( self.m_staticText15, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlIniciales = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlIniciales, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Apellidos:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        gbSizer6.Add( self.m_staticText17, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlApellidos = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlApellidos, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Area de empresa:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        gbSizer6.Add( self.m_staticText13, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBoxAreaChoices = []
        self.m_comboBoxArea = wx.ComboBox( self, wx.ID_ANY, u"IT", wx.DefaultPosition, wx.DefaultSize, m_comboBoxAreaChoices, 0 )
        gbSizer6.Add( self.m_comboBoxArea, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Pais:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gbSizer6.Add( self.m_staticText14, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBoxPaisChoices = []
        self.m_comboBoxPais = wx.ComboBox( self, wx.ID_ANY, u"Guatemala", wx.DefaultPosition, wx.DefaultSize, m_comboBoxPaisChoices, 0 )
        gbSizer6.Add( self.m_comboBoxPais, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        gbSizer6.Add( self.m_staticText27, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlContrasena = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
        gbSizer6.Add( self.m_textCtrlContrasena, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        gbSizer6.Add( self.m_staticline1, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )

        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"CREAR PERMISO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        gbSizer6.Add( self.m_staticText28, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )

        gbSizer6.Add( self.m_staticText29, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_textCtrlNombreNuevoPermiso = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrlNombreNuevoPermiso, wx.GBPosition( 11, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonCrearPermiso = wx.Button( self, wx.ID_ANY, u"Crear Permiso", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonCrearPermiso, wx.GBPosition( 11, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        gbSizer6.Add( self.m_staticline2, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND|wx.ALL, 5 )

        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"ELIMINAR PERMISO", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )

        gbSizer6.Add( self.m_staticText30, wx.GBPosition( 13, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Seleccione un permiso:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        gbSizer6.Add( self.m_staticText31, wx.GBPosition( 14, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        m_comboBoxPermisosChoices = []
        self.m_comboBoxPermisos = wx.ComboBox( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 200,-1 ), m_comboBoxPermisosChoices, 0 )
        gbSizer6.Add( self.m_comboBoxPermisos, wx.GBPosition( 14, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonEliminarPermiso = wx.Button( self, wx.ID_ANY, u"Eliminar Permiso", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonEliminarPermiso, wx.GBPosition( 14, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_buttonRegresar = wx.Button( self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonRegresar, wx.GBPosition( 15, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_buttonCrearUsuario = wx.Button( self, wx.ID_ANY, u"Crear usuario y proceder a modificar accesos", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonCrearUsuario.Enable( False )

        gbSizer6.Add( self.m_buttonCrearUsuario, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.SetSizer( gbSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.inicializarPanelDeControl )
        self.m_textCtrlNombreCompleto.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlNombreCompleto.Bind( wx.EVT_TEXT, self.validarBotonCrear )
        self.m_textCtrlActiveDirectory.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlActiveDirectory.Bind( wx.EVT_TEXT, self.validarBotonCrear )
        self.m_textCtrlNombreDePila.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlNombreDePila.Bind( wx.EVT_TEXT, self.validarBotonCrear )
        self.m_textCtrlIniciales.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlIniciales.Bind( wx.EVT_TEXT, self.validarBotonCrear )
        self.m_textCtrlApellidos.Bind( wx.EVT_CHAR_HOOK, self.moverSiguiente )
        self.m_textCtrlApellidos.Bind( wx.EVT_TEXT, self.validarBotonCrear )
        self.m_buttonCrearPermiso.Bind( wx.EVT_BUTTON, self.crearPermiso )
        self.m_buttonEliminarPermiso.Bind( wx.EVT_BUTTON, self.eliminarPermiso )
        self.m_buttonRegresar.Bind( wx.EVT_BUTTON, self.Regresar )
        self.m_buttonCrearUsuario.Bind( wx.EVT_BUTTON, self.CrearUsuario )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def inicializarPanelDeControl( self, event ):
        event.Skip()

    def moverSiguiente( self, event ):
        event.Skip()

    def validarBotonCrear( self, event ):
        event.Skip()









    def crearPermiso( self, event ):
        event.Skip()

    def eliminarPermiso( self, event ):
        event.Skip()

    def Regresar( self, event ):
        event.Skip()

    def CrearUsuario( self, event ):
        event.Skip()


