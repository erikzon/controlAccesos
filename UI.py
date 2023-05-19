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
        self.m_buttonLogin.Bind( wx.EVT_BUTTON, self.iniciarSesion )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def obtenerDatosMySQL( self, event ):
        event.Skip()

    def iniciarSesion( self, event ):
        event.Skip()


###########################################################################
## Class listadoFrame
###########################################################################

class listadoFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usuarios", pos = wx.DefaultPosition, size = wx.Size( 622,545 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 244, 244, 244 ) )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button4CerrarSesion = wx.Button( self, wx.ID_ANY, u"Cerrar Sesion", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_button4CerrarSesion, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Filtrar Por Pais:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        gbSizer4.Add( self.m_staticText18, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBox3Choices = []
        self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
        gbSizer4.Add( self.m_comboBox3, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Filtrar Por Area:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        gbSizer4.Add( self.m_staticText19, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_comboBox4Choices = []
        self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
        gbSizer4.Add( self.m_comboBox4, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Busqueda por nombre usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer4.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrlBusqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer4.Add( self.m_textCtrlBusqueda, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

        self.m_buttonBuscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_buttonBuscar, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonCrearUsuario = wx.Button( self, wx.ID_ANY, u"Crear Usuario", wx.DefaultPosition, wx.Size( 85,-1 ), 0 )
        gbSizer4.Add( self.m_buttonCrearUsuario, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

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
        self.m_buttonBuscar.Bind( wx.EVT_BUTTON, self.Buscar )
        self.m_buttonCrearUsuario.Bind( wx.EVT_BUTTON, self.CrearUsuario )
        self.m_dataViewListCtrlUsuarios.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.mostrarDetalle, id = wx.ID_ANY )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def listarUsuarios( self, event ):
        event.Skip()

    def CerrarSesion( self, event ):
        event.Skip()

    def Buscar( self, event ):
        event.Skip()

    def CrearUsuario( self, event ):
        event.Skip()

    def mostrarDetalle( self, event ):
        event.Skip()


###########################################################################
## Class detalleFrame
###########################################################################

class detalleFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Informacion de Accesos", pos = wx.DefaultPosition, size = wx.Size( 500,298 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nombre de Usuario en Active Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gbSizer5.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonRegresar = wx.Button( self, wx.ID_ANY, u"Regresar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonRegresar, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonEliminarUsuario = wx.Button( self, wx.ID_ANY, u"Eliminar Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonEliminarUsuario, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_buttonEditarUsuario = wx.Button( self, wx.ID_ANY, u"Editar Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.m_buttonEditarUsuario, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crear Usuario", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer6.Add( self.m_textCtrl8, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Pais:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gbSizer6.Add( self.m_staticText14, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_buttonRegresar = wx.Button( self, wx.ID_ANY, u"Regresar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonRegresar, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )

        self.m_buttonAgregarPermisos = wx.Button( self, wx.ID_ANY, u"Agregar Permisos", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer6.Add( self.m_buttonAgregarPermisos, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Guatemala", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
        gbSizer6.Add( self.m_comboBox2, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"IT", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        gbSizer6.Add( self.m_comboBox1, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        self.SetSizer( gbSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_buttonRegresar.Bind( wx.EVT_BUTTON, self.Regresar )
        self.m_buttonAgregarPermisos.Bind( wx.EVT_BUTTON, self.AgregarPermisos )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Regresar( self, event ):
        event.Skip()

    def AgregarPermisos( self, event ):
        event.Skip()


