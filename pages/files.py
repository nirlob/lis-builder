"""
Página Files - Archivos a incluir en el instalador
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class FilesPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Archivos del Proyecto</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text("Selecciona los archivos y carpetas que se incluirán en el instalador:")
        description.set_wrap(True)
        self.append(description)

        # Lista de archivos (usando ListBox por simplicidad)
        files_label = Gtk.Label()
        files_label.set_text("Archivos incluidos:")
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
            "bin/mi_aplicacion.exe",
            "lib/librerias.dll",
            "config/config.ini",
            "docs/README.txt",
            "resources/iconos/"
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
            remove_button.set_tooltip_text("Remover archivo")
            hbox.append(remove_button)

            row.set_child(hbox)
            self.files_list.append(row)

        scrolled.set_child(self.files_list)
        self.append(scrolled)

        # Botones de acción
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        add_file_button = Gtk.Button(label="Agregar Archivo")
        add_file_button.add_css_class("suggested-action")
        buttons_box.append(add_file_button)

        add_folder_button = Gtk.Button(label="Agregar Carpeta")
        buttons_box.append(add_folder_button)

        clear_button = Gtk.Button(label="Limpiar Todo")
        clear_button.add_css_class("destructive-action")
        buttons_box.append(clear_button)

        self.append(buttons_box)

        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>Los archivos se copiarán al directorio de instalación especificado en Settings.</small>")
        info.set_wrap(True)
        self.append(info)