"""
Settings Page - Installer Settings
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class SettingsPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Installer Settings") + "</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text(_("Configure installation directories and system requirements:"))
        description.set_wrap(True)
        self.append(description)

        # Formulario
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Directorio de instalación por defecto
        install_dir_label = Gtk.Label()
        install_dir_label.set_text(_("Default Installation Directory:"))
        install_dir_label.set_halign(Gtk.Align.START)
        form_box.append(install_dir_label)

        install_dir_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.install_dir_entry = Gtk.Entry()
        self.install_dir_entry.set_text("~/Applications/MyApplication")
        self.install_dir_entry.set_hexpand(True)
        install_dir_box.append(self.install_dir_entry)

        browse_button = Gtk.Button(label=_("Browse"))
        install_dir_box.append(browse_button)
        form_box.append(install_dir_box)

        # Directorio de datos
        data_dir_label = Gtk.Label()
        data_dir_label.set_text(_("Data Directory:"))
        data_dir_label.set_halign(Gtk.Align.START)
        form_box.append(data_dir_label)

        self.data_dir_entry = Gtk.Entry()
        self.data_dir_entry.set_text("~/.config/MyApplication")
        form_box.append(self.data_dir_entry)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Requisitos del sistema
        req_label = Gtk.Label()
        req_label.set_markup("<b>" + _("System Requirements") + "</b>")
        req_label.set_halign(Gtk.Align.START)
        form_box.append(req_label)

        # Versión mínima de distribución Linux
        distro_label = Gtk.Label()
        distro_label.set_text(_("Minimum Linux Distribution:"))
        distro_label.set_halign(Gtk.Align.START)
        form_box.append(distro_label)

        self.distro_combo = Gtk.ComboBoxText()
        linux_distros = ["Ubuntu 18.04+", "Ubuntu 20.04+", "Ubuntu 22.04+", "Fedora 30+", "Debian 10+", "Arch Linux", _("Any distribution")]
        for distro in linux_distros:
            self.distro_combo.append_text(distro)
        self.distro_combo.set_active(6)  # Cualquier distribución por defecto
        form_box.append(self.distro_combo)

        # Dependencias requeridas
        deps_label = Gtk.Label()
        deps_label.set_text(_("System Dependencies:"))
        deps_label.set_halign(Gtk.Align.START)
        form_box.append(deps_label)

        self.deps_entry = Gtk.Entry()
        self.deps_entry.set_placeholder_text(_("gtk3, libssl, etc. (comma separated)"))
        form_box.append(self.deps_entry)

        # Espacio requerido
        space_label = Gtk.Label()
        space_label.set_text(_("Required Disk Space (MB):"))
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
    
    def get_data(self):
        """Obtener datos de configuración"""
        return {
            "install_dir": self.install_dir_entry.get_text(),
            "data_dir": self.data_dir_entry.get_text(),
            "min_distro": self.distro_combo.get_active_text(),
            "dependencies": self.deps_entry.get_text(),
            "required_space": self.space_entry.get_text()
        }
    
    def set_data(self, data):
        """Cargar datos de configuración"""
        if "install_dir" in data:
            self.install_dir_entry.set_text(data["install_dir"])
        if "data_dir" in data:
            self.data_dir_entry.set_text(data["data_dir"])
        if "min_distro" in data:
            # Buscar el índice del texto de distribución
            for i in range(self.distro_combo.get_n_items()):
                if self.distro_combo.get_item_text(i) == data["min_distro"]:
                    self.distro_combo.set_active(i)
                    break
        if "dependencies" in data:
            self.deps_entry.set_text(data["dependencies"])
        if "required_space" in data:
            self.space_entry.set_text(data["required_space"])
    
    def clear_data(self):
        """Limpiar configuración"""
        self.install_dir_entry.set_text("~/Applications/MyApplication")
        self.data_dir_entry.set_text("~/.config/MyApplication")
        self.distro_combo.set_active(6)  # Cualquier distribución
        self.deps_entry.set_text("")
        self.space_entry.set_text("100")