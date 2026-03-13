"""
Installer Page - Installer Configuration
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class InstallerPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Installer Configuration") + "</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text(_("Customize the installer behavior and appearance:"))
        description.set_wrap(True)
        self.append(description)

        # Formulario
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Nombre del archivo de salida
        output_label = Gtk.Label()
        output_label.set_text(_(".lis File Name:"))
        output_label.set_halign(Gtk.Align.START)
        form_box.append(output_label)

        output_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.output_entry = Gtk.Entry()
        self.output_entry.set_text("setup")
        output_box.append(self.output_entry)

        output_ext = Gtk.Label()
        output_ext.set_text(".lis")
        output_box.append(output_ext)
        form_box.append(output_box)

        # Icono del instalador
        installer_icon_label = Gtk.Label()
        installer_icon_label.set_text(_("Installer Icon:"))
        installer_icon_label.set_halign(Gtk.Align.START)
        form_box.append(installer_icon_label)

        icon_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.installer_icon_entry = Gtk.Entry()
        self.installer_icon_entry.set_placeholder_text(_("Path to .ico file"))
        self.installer_icon_entry.set_hexpand(True)
        icon_box.append(self.installer_icon_entry)

        icon_button = Gtk.Button(label=_("Browse"))
        icon_box.append(icon_button)
        form_box.append(icon_box)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Opciones del instalador
        options_label = Gtk.Label()
        options_label.set_markup("<b>" + _("Installer Options") + "</b>")
        options_label.set_halign(Gtk.Align.START)
        form_box.append(options_label)

        # Crear accesos directos
        self.shortcuts_checkbox = Gtk.CheckButton()
        self.shortcuts_checkbox.set_active(True)
        self.shortcuts_checkbox.set_label(_("Create desktop shortcut"))
        form_box.append(self.shortcuts_checkbox)

        self.startmenu_checkbox = Gtk.CheckButton()
        self.startmenu_checkbox.set_active(True)
        self.startmenu_checkbox.set_label(_("Create application menu entry"))
        form_box.append(self.startmenu_checkbox)

        # Iniciar después de instalar
        self.run_after_checkbox = Gtk.CheckButton()
        self.run_after_checkbox.set_active(False)
        self.run_after_checkbox.set_label(_("Run application after installation"))
        form_box.append(self.run_after_checkbox)

        # Crear desinstalador
        self.uninstaller_checkbox = Gtk.CheckButton()
        self.uninstaller_checkbox.set_active(True)
        self.uninstaller_checkbox.set_label(_("Create uninstaller script"))
        form_box.append(self.uninstaller_checkbox)

        # Separador
        separator2 = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator2)

        # Idiomas
        lang_label = Gtk.Label()
        lang_label.set_text(_("Supported Languages:"))
        lang_label.set_halign(Gtk.Align.START)
        form_box.append(lang_label)

        self.lang_combo = Gtk.ComboBoxText()
        languages = [_("Spanish"), _("English"), _("French"), _("German"), _("Italian"), _("Portuguese")]
        for lang in languages:
            self.lang_combo.append_text(lang)
        self.lang_combo.set_active(1)  # English por defecto
        form_box.append(self.lang_combo)

        self.append(form_box)

        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)
    
    def get_data(self):
        """Obtener configuración del instalador"""
        return {
            "output_name": self.output_entry.get_text(),
            "installer_icon": self.installer_icon_entry.get_text(),
            "create_shortcuts": self.shortcuts_checkbox.get_active(),
            "create_startmenu": self.startmenu_checkbox.get_active(),
            "run_after_install": self.run_after_checkbox.get_active(),
            "create_uninstaller": self.uninstaller_checkbox.get_active(),
            "language": self.lang_combo.get_active_text()
        }
    
    def set_data(self, data):
        """Cargar configuración del instalador"""
        if "output_name" in data:
            self.output_entry.set_text(data["output_name"])
        if "installer_icon" in data:
            self.installer_icon_entry.set_text(data["installer_icon"])
        if "create_shortcuts" in data:
            self.shortcuts_checkbox.set_active(data["create_shortcuts"])
        if "create_startmenu" in data:
            self.startmenu_checkbox.set_active(data["create_startmenu"])
        if "run_after_install" in data:
            self.run_after_checkbox.set_active(data["run_after_install"])
        if "create_uninstaller" in data:
            self.uninstaller_checkbox.set_active(data["create_uninstaller"])
        if "language" in data:
            # Buscar el índice del idioma
            for i in range(self.lang_combo.get_n_items()):
                if self.lang_combo.get_item_text(i) == data["language"]:
                    self.lang_combo.set_active(i)
                    break
    
    def clear_data(self):
        """Limpiar configuración del instalador"""
        self.output_entry.set_text("setup")
        self.installer_icon_entry.set_text("")
        self.shortcuts_checkbox.set_active(True)
        self.startmenu_checkbox.set_active(True)
        self.run_after_checkbox.set_active(False)
        self.uninstaller_checkbox.set_active(True)
        self.lang_combo.set_active(0)  # Español