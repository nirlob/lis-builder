#!/usr/bin/env python3
"""
Aplicación simple con GTK 4
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Mi Aplicación GTK 4")
        self.set_default_size(400, 300)
        
        # Crear una caja vertical para contener los elementos
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        vbox.set_margin_start(20)
        vbox.set_margin_end(20)
        
        # Crear un label
        label = Gtk.Label()
        label.set_text("¡Hola desde GTK 4!")
        label.set_markup("<big>¡Hola desde GTK 4!</big>")
        vbox.append(label)
        
        # Crear un entry (campo de texto)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Escribe algo aquí...")
        vbox.append(entry)
        
        # Crear un botón
        button = Gtk.Button(label="Saludar")
        button.connect("clicked", self.on_button_clicked, entry, label)
        vbox.append(button)
        
        # Crear un botón de salida
        quit_button = Gtk.Button(label="Salir")
        quit_button.connect("clicked", lambda x: app.quit())
        vbox.append(quit_button)
        
        # Establecer la caja como contenido de la ventana
        self.set_child(vbox)
    
    def on_button_clicked(self, widget, entry, label):
        """Manejador del click del botón"""
        text = entry.get_text()
        if text:
            label.set_markup(f"<big>¡Hola {text}!</big>")
        else:
            label.set_text("Por favor, escribe algo en el campo de texto.")


class MyApp(Gtk.Application):
    def do_activate(self):
        """Activar la aplicación"""
        win = MainWindow(self)
        win.present()


if __name__ == '__main__':
    app = MyApp()
    exit_status = app.run(None)
