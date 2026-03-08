"""
Página Installer - Configuración del instalador
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class InstallerPage(Gtk.Box):
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
        description.set_text("Personaliza el comportamiento y apariencia del instalador:")
        description.set_wrap(True)
        self.append(description)

        # Formulario
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # Nombre del archivo de salida
        output_label = Gtk.Label()
        output_label.set_text("Nombre del archivo .lis:")
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
        installer_icon_label.set_text("Icono del instalador:")
        installer_icon_label.set_halign(Gtk.Align.START)
        form_box.append(installer_icon_label)

        icon_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.installer_icon_entry = Gtk.Entry()
        self.installer_icon_entry.set_placeholder_text("Ruta al archivo .ico")
        self.installer_icon_entry.set_hexpand(True)
        icon_box.append(self.installer_icon_entry)

        icon_button = Gtk.Button(label="Examinar")
        icon_box.append(icon_button)
        form_box.append(icon_box)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator)

        # Opciones del instalador
        options_label = Gtk.Label()
        options_label.set_markup("<b>Opciones del Instalador</b>")
        options_label.set_halign(Gtk.Align.START)
        form_box.append(options_label)

        # Crear accesos directos
        self.shortcuts_checkbox = Gtk.CheckButton()
        self.shortcuts_checkbox.set_active(True)
        self.shortcuts_checkbox.set_label("Crear accesos directos en el escritorio")
        form_box.append(self.shortcuts_checkbox)

        self.startmenu_checkbox = Gtk.CheckButton()
        self.startmenu_checkbox.set_active(True)
        self.startmenu_checkbox.set_label("Crear entrada en el menú Inicio")
        form_box.append(self.startmenu_checkbox)

        # Iniciar después de instalar
        self.run_after_checkbox = Gtk.CheckButton()
        self.run_after_checkbox.set_active(False)
        self.run_after_checkbox.set_label("Ejecutar la aplicación después de instalar")
        form_box.append(self.run_after_checkbox)

        # Crear desinstalador
        self.uninstaller_checkbox = Gtk.CheckButton()
        self.uninstaller_checkbox.set_active(True)
        self.uninstaller_checkbox.set_label("Crear desinstalador")
        form_box.append(self.uninstaller_checkbox)

        # Separador
        separator2 = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        form_box.append(separator2)

        # Idiomas
        lang_label = Gtk.Label()
        lang_label.set_text("Idiomas soportados:")
        lang_label.set_halign(Gtk.Align.START)
        form_box.append(lang_label)

        self.lang_combo = Gtk.ComboBoxText()
        languages = ["Español", "Inglés", "Francés", "Alemán", "Italiano", "Portugués"]
        for lang in languages:
            self.lang_combo.append_text(lang)
        self.lang_combo.set_active(0)  # Español por defecto
        form_box.append(self.lang_combo)

        self.append(form_box)

        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)