#!/usr/bin/env python3
"""
LIS Builder - Aplicación instaladora con GTK 4
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

from pages.presentation import PresentationPage
from pages.license import LicensePage
from pages.administrator import AdministratorPage
from pages.directories import DirectoriesPage
from pages.options import OptionsPage
from pages.finish import FinishPage


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("LIS Builder - Instalador")
        self.set_default_size(800, 600)
        
        # Crear un Stack para contener las páginas
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        
        # Agregar las páginas al stack
        self.stack.add_titled(PresentationPage(), "presentation", "Presentation")
        self.stack.add_titled(LicensePage(), "license", "License")
        self.stack.add_titled(AdministratorPage(), "administrator", "Administrator")
        self.stack.add_titled(DirectoriesPage(), "directories", "Directories")
        self.stack.add_titled(OptionsPage(), "options", "Options")
        self.stack.add_titled(FinishPage(), "finish", "Finish")
        
        # Crear un StackSidebar
        sidebar = Gtk.StackSidebar()
        sidebar.set_stack(self.stack)
        
        # Crear una caja horizontal con el sidebar y el stack
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox.append(sidebar)
        hbox.append(self.stack)
        
        # Hacer que el stack ocupe más espacio
        hbox.set_child_packing(self.stack, True, True, 0, Gtk.PackType.START)
        
        # Establecer la caja como contenido de la ventana
        self.set_child(hbox)


class MyApp(Gtk.Application):
    def do_activate(self):
        """Activar la aplicación"""
        win = MainWindow(self)
        win.present()


if __name__ == '__main__':
    app = MyApp()
    exit_status = app.run(None)
