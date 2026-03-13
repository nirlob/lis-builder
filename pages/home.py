"""
Home Page - Project Information
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class HomePage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Project Information") + "</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text(_("Configure basic information for your application:"))
        description.set_wrap(True)
        self.append(description)

        # Formulario principal
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Nombre de la aplicación
        name_label = Gtk.Label()
        name_label.set_text(_("Application Name:"))
        name_label.set_halign(Gtk.Align.START)
        form_box.append(name_label)

        self.name_entry = Gtk.Entry()
        self.name_entry.set_placeholder_text(_("My Application"))
        form_box.append(self.name_entry)

        # Versión
        version_label = Gtk.Label()
        version_label.set_text(_("Version:"))
        version_label.set_halign(Gtk.Align.START)
        form_box.append(version_label)

        self.version_entry = Gtk.Entry()
        self.version_entry.set_placeholder_text("1.0.0")
        form_box.append(self.version_entry)

        # Descripción
        desc_label = Gtk.Label()
        desc_label.set_text(_("Description:"))
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
        license_label.set_text(_("License:"))
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
        icon_label.set_text(_("Application Icon:"))
        icon_label.set_halign(Gtk.Align.START)
        form_box.append(icon_label)

        icon_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.icon_entry = Gtk.Entry()
        self.icon_entry.set_placeholder_text(_("Path to .ico or .png file"))
        self.icon_entry.set_hexpand(True)
        icon_box.append(self.icon_entry)

        icon_button = Gtk.Button(label=_("Browse"))
        icon_box.append(icon_button)
        form_box.append(icon_box)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Privilegios de administrador
        admin_label = Gtk.Label()
        admin_label.set_markup("<b>" + _("Administrator Privileges") + "</b>")
        admin_label.set_halign(Gtk.Align.START)
        form_box.append(admin_label)

        self.admin_checkbox = Gtk.CheckButton()
        self.admin_checkbox.set_label(_("Requires administrator installation (sudo)"))
        form_box.append(self.admin_checkbox)

        # Explicación de privilegios
        admin_desc_label = Gtk.Label()
        admin_desc_label.set_text(_("Explanation (why sudo is needed):"))
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
    
    def get_data(self):
        """Obtener datos de la página"""
        # Obtener texto de TextView descripción
        desc_buffer = self.desc_text.get_buffer()
        desc_text = desc_buffer.get_text(desc_buffer.get_start_iter(), desc_buffer.get_end_iter(), False)
        
        # Obtener texto de TextView admin
        admin_buffer = self.admin_text.get_buffer()
        admin_text = admin_buffer.get_text(admin_buffer.get_start_iter(), admin_buffer.get_end_iter(), False)
        
        return {
            "name": self.name_entry.get_text(),
            "version": self.version_entry.get_text(),
            "description": desc_text,
            "license": self.license_combo.get_active_text(),
            "icon": self.icon_entry.get_text(),
            "requires_admin": self.admin_checkbox.get_active(),
            "admin_explanation": admin_text
        }
    
    def set_data(self, data):
        """Cargar datos en la página"""
        if "name" in data:
            self.name_entry.set_text(data["name"])
        if "version" in data:
            self.version_entry.set_text(data["version"])
        if "description" in data:
            buffer = self.desc_text.get_buffer()
            buffer.set_text(data["description"])
        if "license" in data:
            # Buscar el índice del texto de licencia
            for i in range(self.license_combo.get_n_items()):
                if self.license_combo.get_item_text(i) == data["license"]:
                    self.license_combo.set_active(i)
                    break
        if "icon" in data:
            self.icon_entry.set_text(data["icon"])
        if "requires_admin" in data:
            self.admin_checkbox.set_active(data["requires_admin"])
        if "admin_explanation" in data:
            buffer = self.admin_text.get_buffer()
            buffer.set_text(data["admin_explanation"])
    
    def clear_data(self):
        """Limpiar todos los campos"""
        self.name_entry.set_text("")
        self.version_entry.set_text("")
        buffer = self.desc_text.get_buffer()
        buffer.set_text("")
        self.license_combo.set_active(0)
        self.icon_entry.set_text("")
        self.admin_checkbox.set_active(False)
        buffer = self.admin_text.get_buffer()
        buffer.set_text("")