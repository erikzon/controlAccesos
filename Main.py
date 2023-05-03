import wx
import wx.xrc
import UI


class autenticacionFrameOverride(UI.autenticacionFrame):
    def iniciarSesion(self, event):
        self.Close()
        frame = UI.listadoFrame(None)
        frame.Show(True)


if __name__ == "__main__":
    app = wx.App()
    frame = autenticacionFrameOverride(None)
    frame.Show(True)
    app.MainLoop()
