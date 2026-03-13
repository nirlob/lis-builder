"""
Files Page - Project Files
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class FilesPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Project Files") + "</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text(_("Select the files and folders to include in the installer:"))
        description.set_wrap(True)
        self.append(description)

        # Lista de archivos (usando ListBox por simplicidad)
        files_label = Gtk.Label()
        files_label.set_text(_("Included Files:"))
        files_label.set_halign(Gtk.Align.START)
        self.append(files_label)

        # Scrolled window para la lista
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        scrolled.set_hexpand(True)

        self.files_list = Gtk.ListBox()
        self.files_list.set_selection_mode(Gtk.SelectionMode.MULTIPLE)

        # Agregar algunos archivos de ejemplo
        example_files = [
            "bin/my_application",
            "lib/libraries.so",
            "config/config.ini",
            "docs/README.txt",
            "resources/icons/"
        ]

        for file_path in example_files:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            hbox.set_margin_top(5)
            hbox.set_margin_bottom(5)
            hbox.set_margin_start(10)
            hbox.set_margin_end(10)

            label = Gtk.Label()
            label.set_text(file_path)
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
            self.files_list.append(row)

        scrolled.set_child(self.files_list)
        self.append(scrolled)

        # Botones de acción
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        add_file_button = Gtk.Button(label=_("Add File"))
        add_file_button.add_css_class("suggested-action")
        buttons_box.append(add_file_button)

        add_folder_button = Gtk.Button(label=_("Add Folder"))
        buttons_box.append(add_folder_button)

        clear_button = Gtk.Button(label=_("Clear All"))
        clear_button.add_css_class("destructive-action")
        buttons_box.append(clear_button)

        self.append(buttons_box)

        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>" + _("Files will be copied to the installation directory specified in Settings.") + "</small>")
        info.set_wrap(True)
        self.append(info)
    
    def get_data(self):
        """Obtener lista de archivos"""
        files = []
        # Recorrer todas las filas de la lista
        row = self.files_list.get_first_child()
        while row is not None:
            if isinstance(row, Gtk.ListBoxRow):
                hbox = row.get_child()
                if isinstance(hbox, Gtk.Box):
                    # El primer hijo debería ser el label con el path
                    child = hbox.get_first_child()
                    if isinstance(child, Gtk.Label):
                        files.append(child.get_text())
            row = row.get_next_sibling()
        return files
    
    def set_data(self, data):
        """Cargar lista de archivos"""
        # Limpiar lista actual
        self.clear_data()
        
        # Agregar archivos del data
        if isinstance(data, list):
            for file_path in data:
                self.add_file_row(file_path)
    
    def clear_data(self):
        """Limpiar todos los archivos"""
        # Remover todas las filas
        while True:
            row = self.files_list.get_first_child()
            if row is None:
                break
            self.files_list.remove(row)
    
    def add_file_row(self, file_path):
        """Agregar una fila de archivo a la lista"""
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox.set_margin_top(5)
        hbox.set_margin_bottom(5)
        hbox.set_margin_start(10)
        hbox.set_margin_end(10)

        label = Gtk.Label()
        label.set_text(file_path)
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        hbox.append(label)

        remove_button = Gtk.Button()
        remove_icon = Gtk.Image()
        remove_icon.set_from_icon_name("user-trash-symbolic")
        remove_button.set_child(remove_icon)
        remove_button.set_tooltip_text(_("Remove file"))
        remove_button.connect("clicked", self.on_remove_file, row)
        hbox.append(remove_button)

        row.set_child(hbox)
        self.files_list.append(row)
    
    def on_remove_file(self, button, row):
        """Remover un archivo de la lista"""
        self.files_list.remove(row)