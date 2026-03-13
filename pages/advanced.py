"""
Advanced Page - Advanced Options
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class AdvancedPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Advanced Options") + "</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text(_("Advanced configurations for experienced users:"))
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
        env_title.set_markup("<b>" + _("Environment Variables") + "</b>")
        env_title.set_halign(Gtk.Align.START)
        env_tab.append(env_title)

        env_desc = Gtk.Label()
        env_desc.set_text(_("Variables that will be added to the system PATH:"))
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

        add_env_button = Gtk.Button(label=_("Add Variable"))
        add_env_button.add_css_class("suggested-action")
        env_tab.append(add_env_button)

        notebook.append_page(env_tab, Gtk.Label(label=_("Variables")))

        # Pestaña 2: Comandos post-instalación
        post_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        post_tab.set_margin_top(20)
        post_tab.set_margin_bottom(20)
        post_tab.set_margin_start(20)
        post_tab.set_margin_end(20)

        post_title = Gtk.Label()
        post_title.set_markup("<b>" + _("Post-Installation Commands") + "</b>")
        post_title.set_halign(Gtk.Align.START)
        post_tab.append(post_title)

        post_desc = Gtk.Label()
        post_desc.set_text(_("Commands that will be executed after installation:"))
        post_desc.set_wrap(True)
        post_desc.set_halign(Gtk.Align.START)
        post_tab.append(post_desc)

        # Lista de comandos
        post_scrolled = Gtk.ScrolledWindow()
        post_scrolled.set_vexpand(True)

        self.post_list = Gtk.ListBox()
        self.post_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Comandos de ejemplo
        example_commands = ["chmod +x $INSTALLDIR/bin/my_application", "ln -sf $INSTALLDIR/bin/my_application $HOME/.local/bin/", "update-desktop-database"]
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
            remove_button.set_tooltip_text(_("Remove command"))
            hbox.append(remove_button)

            row.set_child(hbox)
            self.post_list.append(row)

        post_scrolled.set_child(self.post_list)
        post_tab.append(post_scrolled)

        add_post_button = Gtk.Button(label=_("Add Command"))
        add_post_button.add_css_class("suggested-action")
        post_tab.append(add_post_button)

        notebook.append_page(post_tab, Gtk.Label(label=_("Post-Installation")))

        # Pestaña 3: Archivos de configuración
        config_tab = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        config_tab.set_margin_top(20)
        config_tab.set_margin_bottom(20)
        config_tab.set_margin_start(20)
        config_tab.set_margin_end(20)

        config_title = Gtk.Label()
        config_title.set_markup("<b>" + _("Configuration Files") + "</b>")
        config_title.set_halign(Gtk.Align.START)
        config_tab.append(config_title)

        config_desc = Gtk.Label()
        config_desc.set_text(_("Configuration files that will be created during installation:"))
        config_desc.set_wrap(True)
        config_desc.set_halign(Gtk.Align.START)
        config_tab.append(config_desc)

        # Lista de archivos de configuración
        config_scrolled = Gtk.ScrolledWindow()
        config_scrolled.set_vexpand(True)

        self.config_list = Gtk.ListBox()
        self.config_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Archivos de ejemplo
        example_configs = [".desktop -> /usr/share/applications/", ".service -> $HOME/.config/systemd/user/", ".conf -> /etc/"]
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
            remove_button.set_tooltip_text(_("Remove file"))
            hbox.append(remove_button)

            row.set_child(hbox)
            self.config_list.append(row)

        config_scrolled.set_child(self.config_list)
        config_tab.append(config_scrolled)

        add_config_button = Gtk.Button(label=_("Add Configuration File"))
        add_config_button.add_css_class("suggested-action")
        config_tab.append(add_config_button)

        notebook.append_page(config_tab, Gtk.Label(label=_("Configuration")))

        self.append(notebook)
    
    def get_data(self):
        """Obtener datos avanzados"""
        return {
            "environment_vars": self.get_list_data(self.env_list),
            "post_install_commands": self.get_list_data(self.post_list),
            "config_files": self.get_list_data(self.config_list)
        }
    
    def set_data(self, data):
        """Cargar datos avanzados"""
        if "environment_vars" in data and isinstance(data["environment_vars"], list):
            self.set_list_data(self.env_list, data["environment_vars"])
        if "post_install_commands" in data and isinstance(data["post_install_commands"], list):
            self.set_list_data(self.post_list, data["post_install_commands"])
        if "config_files" in data and isinstance(data["config_files"], list):
            self.set_list_data(self.config_list, data["config_files"])
    
    def clear_data(self):
        """Limpiar datos avanzados"""
        self.clear_list(self.env_list)
        self.clear_list(self.post_list)
        self.clear_list(self.config_list)
    
    def get_list_data(self, listbox):
        """Obtener datos de una lista"""
        items = []
        row = listbox.get_first_child()
        while row is not None:
            if isinstance(row, Gtk.ListBoxRow):
                hbox = row.get_child()
                if isinstance(hbox, Gtk.Box):
                    child = hbox.get_first_child()
                    if isinstance(child, Gtk.Label):
                        items.append(child.get_text())
            row = row.get_next_sibling()
        return items
    
    def set_list_data(self, listbox, data):
        """Cargar datos en una lista"""
        self.clear_list(listbox)
        for item in data:
            self.add_list_item(listbox, item)
    
    def clear_list(self, listbox):
        """Limpiar una lista"""
        while True:
            row = listbox.get_first_child()
            if row is None:
                break
            listbox.remove(row)
    
    def add_list_item(self, listbox, text):
        """Agregar un elemento a una lista"""
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox.set_margin_top(5)
        hbox.set_margin_bottom(5)
        hbox.set_margin_start(10)
        hbox.set_margin_end(10)

        label = Gtk.Label()
        label.set_text(text)
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        hbox.append(label)

        remove_button = Gtk.Button()
        remove_icon = Gtk.Image()
        remove_icon.set_from_icon_name("user-trash-symbolic")
        remove_button.set_child(remove_icon)
        remove_button.set_tooltip_text("Remover")
        hbox.append(remove_button)

        row.set_child(hbox)
        listbox.append(row)