#!/usr/bin/env python3
"""
LIS Builder - Generador de instaladores .lis
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

from pages.home import HomePage
from pages.files import FilesPage
from pages.settings import SettingsPage
from pages.installer import InstallerPage
from pages.advanced import AdvancedPage
from pages.build import BuildPage


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("LIS Builder")
        self.set_default_size(900, 650)
        
        # Crear HeaderBar
        header_bar = Gtk.HeaderBar()
        self.set_titlebar(header_bar)
        
        # Botón Build (izquierda, antes del menú)
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
        self.stack.add_titled(HomePage(), "home", "Home")
        self.stack.add_titled(FilesPage(), "files", "Files")
        self.stack.add_titled(SettingsPage(), "settings", "Settings")
        self.stack.add_titled(InstallerPage(), "installer", "Installer")
        self.stack.add_titled(AdvancedPage(), "advanced", "Advanced")
        self.stack.add_titled(BuildPage(), "build", "Build")
        
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
