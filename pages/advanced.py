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
        example_env = ["$HOME/.local/bin", "$INSTALLDIR/bin"]
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
        example_commands = ["chmod +x $INSTALLDIR/bin/mi_aplicacion", "ln -sf $INSTALLDIR/bin/mi_aplicacion /usr/local/bin/", "update-desktop-database"]
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

        # Pestaña 3: Archivos de configuración
        config_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        config_tab.set_margin_top(20)
        config_tab.set_margin_bottom(20)
        config_tab.set_margin_start(20)
        config_tab.set_margin_end(20)

        config_title = Gtk.Label()
        config_title.set_markup("<b>Archivos de Configuración</b>")
        config_title.set_halign(Gtk.Align.START)
        config_tab.append(config_title)

        config_desc = Gtk.Label()
        config_desc.set_text("Archivos de configuración que se crearán durante la instalación:")
        config_desc.set_wrap(True)
        config_desc.set_halign(Gtk.Align.START)
        config_tab.append(config_desc)

        # Lista de archivos de configuración
        config_scrolled = Gtk.ScrolledWindow()
        config_scrolled.set_vexpand(True)

        self.config_list = Gtk.ListBox()
        self.config_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Archivos de ejemplo
        example_configs = [".desktop -> /usr/share/applications/", ".service -> /usr/lib/systemd/user/", ".conf -> /etc/"]
        for config_entry in example_configs:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            hbox.set_margin_top(5)
            hbox.set_margin_bottom(5)
            hbox.set_margin_start(10)
            hbox.set_margin_end(10)

            label = Gtk.Label()
            label.set_text(config_entry)
            label.set_halign(Gtk.Align.START)
            label.set_hexpand(True)
            hbox.append(label)

            remove_button = Gtk.Button()
            remove_icon = Gtk.Image()
            remove_icon.set_from_icon_name("user-trash-symbolic")
            remove_button.set_child(remove_icon)
            remove_button.set_tooltip_text("Remover archivo")
            hbox.append(remove_button)

            row.set_child(hbox)
            self.config_list.append(row)

        config_scrolled.set_child(self.config_list)
        config_tab.append(config_scrolled)

        add_config_button = Gtk.Button(label="Agregar Archivo de Configuración")
        add_config_button.add_css_class("suggested-action")
        config_tab.append(add_config_button)

        notebook.append_page(config_tab, Gtk.Label(label="Configuración"))

        self.append(notebook)