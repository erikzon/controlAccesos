# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usuarios", pos = wx.DefaultPosition, size = wx.Size( 922,611 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 244, 244, 244 ) )

        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Busqueda por nombre usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gbSizer4.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrlBusqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_textCtrlBusqueda, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_buttonBuscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer4.Add( self.m_buttonBuscar, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gbSizer9 = wx.GridBagSizer( 0, 0 )
        gbSizer9.SetFlexibleDirection( wx.BOTH )
        gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_gridUsuarios = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,500 ), 0 )

        # Grid
        self.m_gridUsuarios.CreateGrid( 10, 5 )
        self.m_gridUsuarios.EnableEditing( True )
        self.m_gridUsuarios.EnableGridLines( True )
        self.m_gridUsuarios.EnableDragGridSize( False )
        self.m_gridUsuarios.SetMargins( 0, 0 )

        # Columns
        self.m_gridUsuarios.EnableDragColMove( False )
        self.m_gridUsuarios.EnableDragColSize( True )
        self.m_gridUsuarios.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_gridUsuarios.SetRowSize( 0, 24 )
        self.m_gridUsuarios.SetRowSize( 1, 21 )
        self.m_gridUsuarios.SetRowSize( 2, 21 )
        self.m_gridUsuarios.SetRowSize( 3, 21 )
        self.m_gridUsuarios.SetRowSize( 4, 21 )
        self.m_gridUsuarios.SetRowSize( 5, 21 )
        self.m_gridUsuarios.SetRowSize( 6, 21 )
        self.m_gridUsuarios.AutoSizeRows()
        self.m_gridUsuarios.EnableDragRowSize( True )
        self.m_gridUsuarios.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_gridUsuarios.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        gbSizer9.Add( self.m_gridUsuarios, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        gbSizer4.Add( gbSizer9, wx.GBPosition( 2, 0 ), wx.GBSpan( 5, 5 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


        self.SetSizer( gbSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.listarUsuarios )
        self.m_buttonBuscar.Bind( wx.EVT_BUTTON, self.Buscar )
        self.m_gridUsuarios.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.mostrarDetalle )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def listarUsuarios( self, event ):
        event.Skip()

    def Buscar( self, event ):
        event.Skip()

    def mostrarDetalle( self, event ):
        event.Skip()


###########################################################################
## Class detalleFrame
###########################################################################

class detalleFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detalle", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        self.SetSizer( gbSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


