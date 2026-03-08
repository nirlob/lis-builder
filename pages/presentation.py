"""
Página de Presentación para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class PresentationPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>¡Bienvenido a LIS Builder!</b></big>")
        self.append(title)
        
        # Descripción
        description = Gtk.Label()
        description.set_text("Este instalador te guiará a través de los pasos necesarios para instalar LIS.")
        description.set_wrap(True)
        description.set_justify(Gtk.Justification.CENTER)
        self.append(description)
        
        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>Asegúrate de tener los permisos necesarios antes de continuar.</small>")
        info.set_wrap(True)
        self.append(info)
        
        # Espaciador
        spacer = Gtk.Box()
        self.append(spacer)
        self.set_child_packing(spacer, True, True, 0, Gtk.PackType.START)
