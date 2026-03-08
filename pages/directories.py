"""
Página de Directorios para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class DirectoriesPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Seleccionar Directorios de Instalación</b></big>")
        self.append(title)
        
        # Descripción
        description = Gtk.Label()
        description.set_text("Especifica dónde deseas instalar los componentes:")
        description.set_wrap(True)
        self.append(description)
        
        # Directorio principal
        main_dir_label = Gtk.Label()
        main_dir_label.set_text("Directorio de instalación:")
        main_dir_label.set_halign(Gtk.Align.START)
        self.append(main_dir_label)
        
        main_dir_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        main_dir_entry = Gtk.Entry()
        main_dir_entry.set_text("/opt/lis")
        main_dir_entry.set_hexpand(True)
        main_dir_box.append(main_dir_entry)
        
        browse_button = Gtk.Button(label="Examinar")
        main_dir_box.append(browse_button)
        self.append(main_dir_box)
        
        # Directorio de datos
        data_dir_label = Gtk.Label()
        data_dir_label.set_text("Directorio de datos:")
        data_dir_label.set_halign(Gtk.Align.START)
        self.append(data_dir_label)
        
        data_dir_entry = Gtk.Entry()
        data_dir_entry.set_text("/var/lis")
        self.append(data_dir_entry)
        
        # Directorio de configuración
        config_dir_label = Gtk.Label()
        config_dir_label.set_text("Directorio de configuración:")
        config_dir_label.set_halign(Gtk.Align.START)
        self.append(config_dir_label)
        
        config_dir_entry = Gtk.Entry()
        config_dir_entry.set_text("/etc/lis")
        self.append(config_dir_entry)
        
        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)
