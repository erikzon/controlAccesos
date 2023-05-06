import wx
import wx.xrc


if __name__ == "__main__":
    app = wx.App()
    from ControlAccesosautenticacionFrame import ControlAccesosautenticacionFrame

    frame = ControlAccesosautenticacionFrame(None)
    frame.Show(True)
    app.MainLoop()
