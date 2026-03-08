"""
Página Advanced - Opciones avanzadas
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class AdvancedPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Opciones Avanzadas</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text("Configuraciones avanzadas para usuarios experimentados:")
        description.set_wrap(True)
        self.append(description)

        # Notebook para organizar las opciones avanzadas
        notebook = Gtk.Notebook()
        notebook.set_vexpand(True)
        notebook.set_hexpand(True)

        # Pestaña 1: Variables de entorno
        env_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        env_tab.set_margin_top(20)
        env_tab.set_margin_bottom(20)
        env_tab.set_margin_start(20)
        env_tab.set_margin_end(20)

        env_title = Gtk.Label()
        env_title.set_markup("<b>Variables de Entorno</b>")
        env_title.set_halign(Gtk.Align.START)
        env_tab.append(env_title)

        env_desc = Gtk.Label()
        env_desc.set_text("Variables que se agregarán al PATH del sistema:")
        env_desc.set_wrap(True)
        env_desc.set_halign(Gtk.Align.START)
        env_tab.append(env_desc)

        # Lista de variables de entorno
        env_scrolled = Gtk.ScrolledWindow()
        env_scrolled.set_vexpand(True)

        self.env_list = Gtk.ListBox()
        self.env_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Variables de ejemplo
        example_env = ["%INSTALLDIR%\\bin", "%INSTALLDIR%\\lib"]
        for env_var in example_env:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            hbox.set_margin_top(5)
            hbox.set_margin_bottom(5)
            hbox.set_margin_start(10)
            hbox.set_margin_end(10)

            label = Gtk.Label()
            label.set_text(env_var)
            label.set_halign(Gtk.Align.START)
            label.set_hexpand(True)
            hbox.append(label)

            remove_button = Gtk.Button()
            remove_icon = Gtk.Image()
            remove_icon.set_from_icon_name("user-trash-symbolic")
            remove_button.set_child(remove_icon)
            remove_button.set_tooltip_text("Remover variable")
            hbox.append(remove_button)

            row.set_child(hbox)
            self.env_list.append(row)

        env_scrolled.set_child(self.env_list)
        env_tab.append(env_scrolled)

        add_env_button = Gtk.Button(label="Agregar Variable")
        add_env_button.add_css_class("suggested-action")
        env_tab.append(add_env_button)

        notebook.append_page(env_tab, Gtk.Label(label="Variables"))

        # Pestaña 2: Comandos post-instalación
        post_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        post_tab.set_margin_top(20)
        post_tab.set_margin_bottom(20)
        post_tab.set_margin_start(20)
        post_tab.set_margin_end(20)

        post_title = Gtk.Label()
        post_title.set_markup("<b>Comandos Post-Instalación</b>")
        post_title.set_halign(Gtk.Align.START)
        post_tab.append(post_title)

        post_desc = Gtk.Label()
        post_desc.set_text("Comandos que se ejecutarán después de la instalación:")
        post_desc.set_wrap(True)
        post_desc.set_halign(Gtk.Align.START)
        post_tab.append(post_desc)

        # Lista de comandos
        post_scrolled = Gtk.ScrolledWindow()
        post_scrolled.set_vexpand(True)

        self.post_list = Gtk.ListBox()
        self.post_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Comandos de ejemplo
        example_commands = ["regsvr32 /s %INSTALLDIR%\\bin\\mi_dll.dll", "net start \"Mi Servicio\""]
        for cmd in example_commands:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            hbox.set_margin_top(5)
            hbox.set_margin_bottom(5)
            hbox.set_margin_start(10)
            hbox.set_margin_end(10)

            label = Gtk.Label()
            label.set_text(cmd)
            label.set_halign(Gtk.Align.START)
            label.set_hexpand(True)
            hbox.append(label)

            remove_button = Gtk.Button()
            remove_icon = Gtk.Image()
            remove_icon.set_from_icon_name("user-trash-symbolic")
            remove_button.set_child(remove_icon)
            remove_button.set_tooltip_text("Remover comando")
            hbox.append(remove_button)

            row.set_child(hbox)
            self.post_list.append(row)

        post_scrolled.set_child(self.post_list)
        post_tab.append(post_scrolled)

        add_post_button = Gtk.Button(label="Agregar Comando")
        add_post_button.add_css_class("suggested-action")
        post_tab.append(add_post_button)

        notebook.append_page(post_tab, Gtk.Label(label="Post-Instalación"))

        # Pestaña 3: Registro de Windows
        reg_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        reg_tab.set_margin_top(20)
        reg_tab.set_margin_bottom(20)
        reg_tab.set_margin_start(20)
        reg_tab.set_margin_end(20)

        reg_title = Gtk.Label()
        reg_title.set_markup("<b>Registro de Windows</b>")
        reg_title.set_halign(Gtk.Align.START)
        reg_tab.append(reg_title)

        reg_desc = Gtk.Label()
        reg_desc.set_text("Entradas del registro que se crearán durante la instalación:")
        reg_desc.set_wrap(True)
        reg_desc.set_halign(Gtk.Align.START)
        reg_tab.append(reg_desc)

        # Lista de entradas de registro
        reg_scrolled = Gtk.ScrolledWindow()
        reg_scrolled.set_vexpand(True)

        self.reg_list = Gtk.ListBox()
        self.reg_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Entradas de ejemplo
        example_reg = ["HKLM\\SOFTWARE\\MiApp\\Version = \"1.0\"", "HKCU\\Software\\MiApp\\InstallDir = \"%INSTALLDIR%\""]
        for reg_entry in example_reg:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            hbox.set_margin_top(5)
            hbox.set_margin_bottom(5)
            hbox.set_margin_start(10)
            hbox.set_margin_end(10)

            label = Gtk.Label()
            label.set_text(reg_entry)
            label.set_halign(Gtk.Align.START)
            label.set_hexpand(True)
            hbox.append(label)

            remove_button = Gtk.Button()
            remove_icon = Gtk.Image()
            remove_icon.set_from_icon_name("user-trash-symbolic")
            remove_button.set_child(remove_icon)
            remove_button.set_tooltip_text("Remover entrada")
            hbox.append(remove_button)

            row.set_child(hbox)
            self.reg_list.append(row)

        reg_scrolled.set_child(self.reg_list)
        reg_tab.append(reg_scrolled)

        add_reg_button = Gtk.Button(label="Agregar Entrada")
        add_reg_button.add_css_class("suggested-action")
        reg_tab.append(add_reg_button)

        notebook.append_page(reg_tab, Gtk.Label(label="Registro"))

        self.append(notebook)