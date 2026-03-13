"""
Página de Finalización para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class FinishPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Espaciador superior
        spacer_top = Gtk.Box()
        spacer_top.set_vexpand(True)
        self.append(spacer_top)
        
        # Icono de éxito (usando emoji)
        success_label = Gtk.Label()
        success_label.set_markup("<span font_size='48000'>✓</span>")
        success_label.set_halign(Gtk.Align.CENTER)
        self.append(success_label)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Installation Completed!") + "</b></big>")
        title.set_halign(Gtk.Align.CENTER)
        self.append(title)
        
        # Mensaje
        message = Gtk.Label()
        message.set_text(_("LIS has been successfully installed on your system."))
        message.set_wrap(True)
        message.set_justify(Gtk.Justification.CENTER)
        self.append(message)
        
        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>" + _("You can find the application in the applications menu or run 'lis' from the terminal.") + "</small>")
        info.set_wrap(True)
        info.set_justify(Gtk.Justification.CENTER)
        self.append(info)
        
        # Espaciador inferior
        spacer_bottom = Gtk.Box()
        spacer_bottom.set_vexpand(True)
        self.append(spacer_bottom)
        
        # Botón de finalización
        finish_button = Gtk.Button(label=_("Finish"))
        finish_button.add_css_class("suggested-action")
        self.append(finish_button)
