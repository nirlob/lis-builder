#!/usr/bin/env python3
"""
LIS Builder - Generador de instaladores .lis
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GLib

from pages.home import HomePage
from pages.files import FilesPage
from pages.settings import SettingsPage
from pages.installer import InstallerPage
from pages.advanced import AdvancedPage
from pages.build import BuildPage

import json
import os


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("LIS Builder")
        self.set_default_size(900, 650)
        
        # Estado del proyecto
        self.current_project_file = None
        self.project_data = {}
        
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
        
        # Submenú File
        file_menu = Gio.Menu.new()
        file_menu.append("New", "app.new")
        file_menu.append("Open...", "app.open")
        file_menu.append("Save", "app.save")
        file_menu.append("Save As...", "app.save_as")
        # No hay separador en GTK 4, se puede usar un item vacío o simplemente omitirlo
        file_menu.append("Quit", "app.quit")
        menu_model.append_submenu("File", file_menu)
        
        # Submenú Help
        help_menu = Gio.Menu.new()
        help_menu.append("About", "app.about")
        menu_model.append_submenu("Help", help_menu)
        
        menu_button.set_menu_model(menu_model)
        header_bar.pack_end(menu_button)
        
        # Crear un Stack para contener las páginas
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        
        # Crear páginas con referencias
        self.home_page = HomePage()
        self.files_page = FilesPage()
        self.settings_page = SettingsPage()
        self.installer_page = InstallerPage()
        self.advanced_page = AdvancedPage()
        self.build_page = BuildPage()
        
        # Agregar las páginas al stack
        self.stack.add_titled(self.home_page, "home", "Home")
        self.stack.add_titled(self.files_page, "files", "Files")
        self.stack.add_titled(self.settings_page, "settings", "Settings")
        self.stack.add_titled(self.installer_page, "installer", "Installer")
        self.stack.add_titled(self.advanced_page, "advanced", "Advanced")
        self.stack.add_titled(self.build_page, "build", "Build")
        
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
    
    def on_new_project(self):
        """Crear un nuevo proyecto"""
        # Limpiar datos actuales
        self.current_project_file = None
        self.project_data = {}
        
        # Crear diccionario de páginas por nombre
        self.pages = {
            "home": self.home_page,
            "files": self.files_page,
            "settings": self.settings_page,
            "installer": self.installer_page,
            "advanced": self.advanced_page,
            "build": self.build_page
        }
        
        # Limpiar todas las páginas
        for page in self.pages.values():
            if hasattr(page, 'clear_data'):
                page.clear_data()
        
        # Actualizar título
        self.update_title()
    
    def on_open_project(self):
        """Abrir un proyecto existente"""
        dialog = Gtk.FileChooserDialog(
            title="Abrir proyecto",
            action=Gtk.FileChooserAction.OPEN,
            buttons=("_Cancel", Gtk.ResponseType.CANCEL, "_Open", Gtk.ResponseType.ACCEPT)
        )
        
        # Filtro para archivos .lisproject
        filter_lis = Gtk.FileFilter()
        filter_lis.set_name("LIS Project files")
        filter_lis.add_pattern("*.lisproject")
        dialog.add_filter(filter_lis)
        
        # Filtro para todos los archivos
        filter_all = Gtk.FileFilter()
        filter_all.set_name("All files")
        filter_all.add_pattern("*")
        dialog.add_filter(filter_all)
        
        dialog.connect("response", self.on_open_response)
        dialog.present()
    
    def on_open_response(self, dialog, response):
        """Manejar respuesta del diálogo de abrir"""
        if response == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_file().get_path()
            self.load_project(filename)
        dialog.destroy()
    
    def on_save_project(self):
        """Guardar el proyecto actual"""
        if self.current_project_file:
            self.save_project(self.current_project_file)
        else:
            self.on_save_as_project()
    
    def on_save_as_project(self):
        """Guardar el proyecto con nombre"""
        dialog = Gtk.FileChooserDialog(
            title="Guardar proyecto",
            action=Gtk.FileChooserAction.SAVE,
            buttons=("_Cancel", Gtk.ResponseType.CANCEL, "_Save", Gtk.ResponseType.ACCEPT)
        )
        
        # Establecer nombre por defecto
        dialog.set_current_name("mi_proyecto.lisproject")
        
        dialog.connect("response", self.on_save_response)
        dialog.present()
    
    def on_save_response(self, dialog, response):
        """Manejar respuesta del diálogo de guardar"""
        if response == Gtk.ResponseType.ACCEPT:
            filename = dialog.get_file().get_path()
            # Asegurar extensión .lisproject
            if not filename.endswith('.lisproject'):
                filename += '.lisproject'
            self.save_project(filename)
        dialog.destroy()
    
    def collect_project_data(self):
        """Recopilar datos de todas las páginas"""
        data = {}
        
        # Crear diccionario de páginas por nombre
        self.pages = {
            "home": self.home_page,
            "files": self.files_page,
            "settings": self.settings_page,
            "installer": self.installer_page,
            "advanced": self.advanced_page,
            "build": self.build_page
        }
        
        # Recopilar datos de cada página
        for page_name, page in self.pages.items():
            if hasattr(page, 'get_data'):
                data[page_name] = page.get_data()
        
        return data
    
    def load_project_data(self, data):
        """Cargar datos en todas las páginas"""
        # Crear diccionario de páginas por nombre
        self.pages = {
            "home": self.home_page,
            "files": self.files_page,
            "settings": self.settings_page,
            "installer": self.installer_page,
            "advanced": self.advanced_page,
            "build": self.build_page
        }
        
        # Cargar datos en cada página
        for page_name, page_data in data.items():
            if page_name in self.pages and hasattr(self.pages[page_name], 'set_data'):
                self.pages[page_name].set_data(page_data)
    
    def save_project(self, filename):
        """Guardar proyecto a archivo JSON"""
        try:
            self.project_data = self.collect_project_data()
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.project_data, f, indent=2, ensure_ascii=False)
            
            self.current_project_file = filename
            self.update_title()
            print(f"Proyecto guardado: {filename}")
            
        except Exception as e:
            print(f"Error al guardar proyecto: {e}")
    
    def load_project(self, filename):
        """Cargar proyecto desde archivo JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.project_data = json.load(f)
            
            self.load_project_data(self.project_data)
            self.current_project_file = filename
            self.update_title()
            print(f"Proyecto cargado: {filename}")
            
        except Exception as e:
            print(f"Error al cargar proyecto: {e}")
    
    def update_title(self):
        """Actualizar el título de la ventana con el nombre del proyecto"""
        if self.current_project_file:
            basename = os.path.basename(self.current_project_file)
            self.set_title(f"LIS Builder - {basename}")
        else:
            self.set_title("LIS Builder")


class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.lis.builder")
    
    def do_activate(self):
        """Activar la aplicación"""
        win = MainWindow(self)
        self.win = win  # Guardar referencia a la ventana
        win.present()
    
    def do_startup(self):
        """Configurar acciones de la aplicación"""
        Gtk.Application.do_startup(self)
        
        # Crear acciones
        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.on_new)
        self.add_action(new_action)
        
        open_action = Gio.SimpleAction.new("open", None)
        open_action.connect("activate", self.on_open)
        self.add_action(open_action)
        
        save_action = Gio.SimpleAction.new("save", None)
        save_action.connect("activate", self.on_save)
        self.add_action(save_action)
        
        save_as_action = Gio.SimpleAction.new("save_as", None)
        save_as_action.connect("activate", self.on_save_as)
        self.add_action(save_as_action)
        
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit)
        self.add_action(quit_action)
        
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about)
        self.add_action(about_action)
    
    def on_new(self, action, parameter):
        """Nuevo proyecto"""
        if hasattr(self, 'win'):
            self.win.on_new_project()
    
    def on_open(self, action, parameter):
        """Abrir proyecto"""
        if hasattr(self, 'win'):
            self.win.on_open_project()
    
    def on_save(self, action, parameter):
        """Guardar proyecto"""
        if hasattr(self, 'win'):
            self.win.on_save_project()
    
    def on_save_as(self, action, parameter):
        """Guardar proyecto como"""
        if hasattr(self, 'win'):
            self.win.on_save_as_project()
    
    def on_quit(self, action, parameter):
        """Salir de la aplicación"""
        self.quit()
    
    def on_about(self, action, parameter):
        """Mostrar diálogo About"""
        dialog = Gtk.AboutDialog()
        dialog.set_program_name("LIS Builder")
        dialog.set_version("1.0.0")
        dialog.set_comments("Generador de instaladores .lis para Linux")
        dialog.set_website("https://github.com/lis/builder")
        dialog.set_authors(["Jose"])
        dialog.present()


if __name__ == '__main__':
    app = MyApp()
    exit_status = app.run(None)
