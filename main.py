#!/usr/bin/env python3
"""
LIS Builder - Generador de instaladores .lis
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
        self.set_title("LIS Builder")
        self.set_default_size(900, 650)
        
        # Crear HeaderBar
        header_bar = Gtk.HeaderBar()
        self.set_titlebar(header_bar)
        
        # Botón Build (izquierda)
        build_button = Gtk.Button()
        build_icon = Gtk.Image()
        build_icon.set_from_icon_name("system-run-symbolic")
        build_button.set_child(build_icon)
        build_button.set_tooltip_text("Generar archivo .lis")
        build_button.connect("clicked", self.on_build_clicked)
        header_bar.pack_start(build_button)
        
        # Menú (derecha)
        menu_button = Gtk.MenuButton()
        menu_icon = Gtk.Image()
        menu_icon.set_from_icon_name("open-menu-symbolic")
        menu_button.set_child(menu_icon)
        
        # Crear menú
        menu_model = Gio.Menu.new()
        menu_model.append("About", "app.about")
        menu_model.append("Settings", "app.settings")
        menu_model.append("Quit", "app.quit")
        
        menu_button.set_menu_model(menu_model)
        header_bar.pack_end(menu_button)
        
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
        
        # Hacer que el stack ocupe más espacio
        self.stack.set_hexpand(True)
        hbox.append(self.stack)
        
        # Establecer la caja como contenido de la ventana
        self.set_child(hbox)
    
    def on_build_clicked(self, widget):
        """Generar el archivo .lis"""
        print("Build clicked - Generando archivo .lis...")
        # TODO: Implementar generación de .lis


class MyApp(Gtk.Application):
    def do_activate(self):
        """Activar la aplicación"""
        win = MainWindow(self)
        win.present()


if __name__ == '__main__':
    app = MyApp()
    exit_status = app.run(None)
