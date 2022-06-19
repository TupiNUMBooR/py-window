#!/usr/bin/env python3
import text
import wx


def on_button(e):
    label.SetLabelText(text.get())
    if not hasattr(app, 'im'):
        im = wx.Image("./240.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        app.im = wx.StaticBitmap(frm, -1, im)
        sizer.Add(app.im)
    sizer.Fit(frm)


app = wx.App()
frm = wx.Frame(None, title="window-wx")

label = wx.StaticText(frm, label="empty")
btn = wx.Button(frm, wx.ID_EXECUTE, "Button")
frm.Bind(wx.EVT_BUTTON, on_button, btn)

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.AddMany([label, btn])
frm.SetSizer(sizer)
frm.SetAutoLayout(1)
sizer.Fit(frm)

frm.Show()
app.MainLoop()
