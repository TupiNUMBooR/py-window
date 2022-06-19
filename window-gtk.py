#!/usr/bin/env python3
import text
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Button")
        self.button.connect("clicked", self.on_button_clicked)

        self.label = Gtk.Label(label="123")

        self.image = Gtk.Image()

        self.box.pack_start(self.button, True, True, 0)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.image, True, True, 0)
        self.add(self.box)

    def on_button_clicked(self, widget):
        self.label.set_text(text.get())
        self.image.set_from_file('240.avif')


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()