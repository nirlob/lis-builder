"""
Página de Opciones para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class OptionsPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Opciones de Instalación</b></big>")
        self.append(title)
        
        # Descripción
        description = Gtk.Label()
        description.set_text("Selecciona los componentes que deseas instalar:")
        description.set_wrap(True)
        self.append(description)
        
        # Checkboxes de componentes
        components_label = Gtk.Label()
        components_label.set_text("Componentes:")
        components_label.set_halign(Gtk.Align.START)
        self.append(components_label)
        
        # Core
        core_checkbox = Gtk.CheckButton()
        core_checkbox.set_active(True)
        core_checkbox.set_label("Core (Obligatorio)")
        self.append(core_checkbox)
        
        # Herramientas
        tools_checkbox = Gtk.CheckButton()
        tools_checkbox.set_active(True)
        tools_checkbox.set_label("Herramientas")
        self.append(tools_checkbox)
        
        # Documentación
        docs_checkbox = Gtk.CheckButton()
        docs_checkbox.set_active(False)
        docs_checkbox.set_label("Documentación")
        self.append(docs_checkbox)
        
        # Ejemplos
        examples_checkbox = Gtk.CheckButton()
        examples_checkbox.set_active(False)
        examples_checkbox.set_label("Ejemplos")
        self.append(examples_checkbox)
        
        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        self.append(separator)
        
        # Opciones adicionales
        additional_label = Gtk.Label()
        additional_label.set_text("Opciones adicionales:")
        additional_label.set_halign(Gtk.Align.START)
        self.append(additional_label)
        
        # Crear acceso directo
        shortcut_checkbox = Gtk.CheckButton()
        shortcut_checkbox.set_active(True)
        shortcut_checkbox.set_label("Crear acceso directo en el escritorio")
        self.append(shortcut_checkbox)
        
        # Iniciar al arrancar
        autostart_checkbox = Gtk.CheckButton()
        autostart_checkbox.set_active(False)
        autostart_checkbox.set_label("Iniciar al arrancar el sistema")
        self.append(autostart_checkbox)
        
        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)
