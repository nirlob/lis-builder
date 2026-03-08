"""
Página de Finalización para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class FinishPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Espaciador superior
        spacer_top = Gtk.Box()
        self.append(spacer_top)
        self.set_child_packing(spacer_top, True, True, 0, Gtk.PackType.START)
        
        # Icono de éxito (usando emoji)
        success_label = Gtk.Label()
        success_label.set_markup("<span font_size='48000'>✓</span>")
        success_label.set_halign(Gtk.Align.CENTER)
        self.append(success_label)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>¡Instalación Completada!</b></big>")
        title.set_halign(Gtk.Align.CENTER)
        self.append(title)
        
        # Mensaje
        message = Gtk.Label()
        message.set_text("LIS ha sido instalado exitosamente en tu sistema.")
        message.set_wrap(True)
        message.set_justify(Gtk.Justification.CENTER)
        self.append(message)
        
        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>Puedes encontrar la aplicación en el menú de aplicaciones o ejecutar 'lis' desde la terminal.</small>")
        info.set_wrap(True)
        info.set_justify(Gtk.Justification.CENTER)
        self.append(info)
        
        # Espaciador inferior
        spacer_bottom = Gtk.Box()
        self.append(spacer_bottom)
        self.set_child_packing(spacer_bottom, True, True, 0, Gtk.PackType.START)
        
        # Botón de finalización
        finish_button = Gtk.Button(label="Finalizar")
        finish_button.add_css_class("suggested-action")
        self.append(finish_button)
