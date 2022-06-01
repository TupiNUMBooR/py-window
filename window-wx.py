#!/usr/bin/env python3
import text
import wx


def on_button(e):
    label.SetLabelText(text.get())


app = wx.App()
frm = wx.Frame(None, title="window-wx")

label = wx.StaticText(frm, label="empty")
btn = wx.Button(frm, wx.ID_EXECUTE, "Button")
frm.Bind(wx.EVT_BUTTON, on_button, btn)

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(label, 1, wx.EXPAND)
sizer.Add(btn, 1, wx.EXPAND)

frm.SetSizer(sizer)
frm.SetAutoLayout(1)
sizer.Fit(frm)
frm.Show()
app.MainLoop()
