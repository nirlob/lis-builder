"""
Página Settings - Configuración del instalador
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class SettingsPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Configuración del Instalador</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text("Configura los directorios y requisitos del sistema:")
        description.set_wrap(True)
        self.append(description)

        # Formulario
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Directorio de instalación por defecto
        install_dir_label = Gtk.Label()
        install_dir_label.set_text("Directorio de instalación por defecto:")
        install_dir_label.set_halign(Gtk.Align.START)
        form_box.append(install_dir_label)

        install_dir_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.install_dir_entry = Gtk.Entry()
        self.install_dir_entry.set_text("C:\\Program Files\\Mi Aplicacion")
        self.install_dir_entry.set_hexpand(True)
        install_dir_box.append(self.install_dir_entry)

        browse_button = Gtk.Button(label="Examinar")
        install_dir_box.append(browse_button)
        form_box.append(install_dir_box)

        # Directorio de datos
        data_dir_label = Gtk.Label()
        data_dir_label.set_text("Directorio de datos:")
        data_dir_label.set_halign(Gtk.Align.START)
        form_box.append(data_dir_label)

        self.data_dir_entry = Gtk.Entry()
        self.data_dir_entry.set_text("C:\\ProgramData\\Mi Aplicacion")
        form_box.append(self.data_dir_entry)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Requisitos del sistema
        req_label = Gtk.Label()
        req_label.set_markup("<b>Requisitos del Sistema</b>")
        req_label.set_halign(Gtk.Align.START)
        form_box.append(req_label)

        # Versión mínima de Windows
        win_version_label = Gtk.Label()
        win_version_label.set_text("Versión mínima de Windows:")
        win_version_label.set_halign(Gtk.Align.START)
        form_box.append(win_version_label)

        self.win_version_combo = Gtk.ComboBoxText()
        windows_versions = ["Windows 7", "Windows 8", "Windows 8.1", "Windows 10", "Windows 11"]
        for version in windows_versions:
            self.win_version_combo.append_text(version)
        self.win_version_combo.set_active(3)  # Windows 10 por defecto
        form_box.append(self.win_version_combo)

        # .NET Framework
        dotnet_label = Gtk.Label()
        dotnet_label.set_text(".NET Framework mínimo:")
        dotnet_label.set_halign(Gtk.Align.START)
        form_box.append(dotnet_label)

        self.dotnet_combo = Gtk.ComboBoxText()
        dotnet_versions = ["Ninguno", ".NET Framework 4.0", ".NET Framework 4.5", ".NET Framework 4.6", ".NET Framework 4.8", ".NET 5.0+", ".NET 6.0+", ".NET 7.0+", ".NET 8.0+"]
        for version in dotnet_versions:
            self.dotnet_combo.append_text(version)
        self.dotnet_combo.set_active(0)  # Ninguno por defecto
        form_box.append(self.dotnet_combo)

        # Espacio requerido
        space_label = Gtk.Label()
        space_label.set_text("Espacio en disco requerido (MB):")
        space_label.set_halign(Gtk.Align.START)
        form_box.append(space_label)

        self.space_entry = Gtk.Entry()
        self.space_entry.set_text("100")
        form_box.append(self.space_entry)

        self.append(form_box)

        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)