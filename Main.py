import wx
import wx.xrc
from ControlAccesosautenticacionFrame import ControlAccesosautenticacionFrame


if __name__ == "__main__":
    app = wx.App()
    frame = ControlAccesosautenticacionFrame(None)
    frame.Show(True)
    app.MainLoop()
