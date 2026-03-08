"""
Página Home - Información del proyecto LIS
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class HomePage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Información del Proyecto</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text("Configura la información básica de tu aplicación:")
        description.set_wrap(True)
        self.append(description)

        # Formulario principal
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Nombre de la aplicación
        name_label = Gtk.Label()
        name_label.set_text("Nombre de la aplicación:")
        name_label.set_halign(Gtk.Align.START)
        form_box.append(name_label)

        self.name_entry = Gtk.Entry()
        self.name_entry.set_placeholder_text("Mi Aplicación")
        form_box.append(self.name_entry)

        # Versión
        version_label = Gtk.Label()
        version_label.set_text("Versión:")
        version_label.set_halign(Gtk.Align.START)
        form_box.append(version_label)

        self.version_entry = Gtk.Entry()
        self.version_entry.set_placeholder_text("1.0.0")
        form_box.append(self.version_entry)

        # Descripción
        desc_label = Gtk.Label()
        desc_label.set_text("Descripción:")
        desc_label.set_halign(Gtk.Align.START)
        form_box.append(desc_label)

        self.desc_text = Gtk.TextView()
        self.desc_text.set_wrap_mode(Gtk.WrapMode.WORD)
        desc_scrolled = Gtk.ScrolledWindow()
        desc_scrolled.set_child(self.desc_text)
        desc_scrolled.set_vexpand(True)
        desc_scrolled.set_hexpand(True)
        desc_scrolled.set_min_content_height(80)
        form_box.append(desc_scrolled)

        # Licencia
        license_label = Gtk.Label()
        license_label.set_text("Licencia:")
        license_label.set_halign(Gtk.Align.START)
        form_box.append(license_label)

        self.license_combo = Gtk.ComboBoxText()
        self.license_combo.append_text("GPL v3")
        self.license_combo.append_text("MIT")
        self.license_combo.append_text("Apache 2.0")
        self.license_combo.append_text("BSD")
        self.license_combo.append_text("LGPL v3")
        self.license_combo.set_active(0)
        form_box.append(self.license_combo)

        # Icono
        icon_label = Gtk.Label()
        icon_label.set_text("Icono de la aplicación:")
        icon_label.set_halign(Gtk.Align.START)
        form_box.append(icon_label)

        icon_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.icon_entry = Gtk.Entry()
        self.icon_entry.set_placeholder_text("Ruta al archivo .ico o .png")
        self.icon_entry.set_hexpand(True)
        icon_box.append(self.icon_entry)

        icon_button = Gtk.Button(label="Examinar")
        icon_box.append(icon_button)
        form_box.append(icon_box)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Privilegios de administrador
        admin_label = Gtk.Label()
        admin_label.set_markup("<b>Privilegios de Administrador</b>")
        admin_label.set_halign(Gtk.Align.START)
        form_box.append(admin_label)

        self.admin_checkbox = Gtk.CheckButton()
        self.admin_checkbox.set_label("Requiere instalación como administrador (sudo)")
        form_box.append(self.admin_checkbox)

        # Explicación de privilegios
        admin_desc_label = Gtk.Label()
        admin_desc_label.set_text("Explicación (por qué necesita sudo):")
        admin_desc_label.set_halign(Gtk.Align.START)
        form_box.append(admin_desc_label)

        self.admin_text = Gtk.TextView()
        self.admin_text.set_wrap_mode(Gtk.WrapMode.WORD)
        admin_scrolled = Gtk.ScrolledWindow()
        admin_scrolled.set_child(self.admin_text)
        admin_scrolled.set_vexpand(True)
        admin_scrolled.set_hexpand(True)
        admin_scrolled.set_min_content_height(60)
        form_box.append(admin_scrolled)

        self.append(form_box)

        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)