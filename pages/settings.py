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
        self.install_dir_entry.set_text("~/Aplicaciones/MiAplicacion")
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
        self.data_dir_entry.set_text("~/.config/MiAplicacion")
        form_box.append(self.data_dir_entry)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Requisitos del sistema
        req_label = Gtk.Label()
        req_label.set_markup("<b>Requisitos del Sistema</b>")
        req_label.set_halign(Gtk.Align.START)
        form_box.append(req_label)

        # Versión mínima de distribución Linux
        distro_label = Gtk.Label()
        distro_label.set_text("Distribución Linux mínima:")
        distro_label.set_halign(Gtk.Align.START)
        form_box.append(distro_label)

        self.distro_combo = Gtk.ComboBoxText()
        linux_distros = ["Ubuntu 18.04+", "Ubuntu 20.04+", "Ubuntu 22.04+", "Fedora 30+", "Debian 10+", "Arch Linux", "Cualquier distribución"]
        for distro in linux_distros:
            self.distro_combo.append_text(distro)
        self.distro_combo.set_active(6)  # Cualquier distribución por defecto
        form_box.append(self.distro_combo)

        # Dependencias requeridas
        deps_label = Gtk.Label()
        deps_label.set_text("Dependencias del sistema:")
        deps_label.set_halign(Gtk.Align.START)
        form_box.append(deps_label)

        self.deps_entry = Gtk.Entry()
        self.deps_entry.set_placeholder_text("gtk3, libssl, etc. (separadas por comas)")
        form_box.append(self.deps_entry)

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