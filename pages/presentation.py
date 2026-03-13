"""
Página de Presentación para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class PresentationPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Welcome to LIS Builder!") + "</b></big>")
        self.append(title)
        
        # Descripción
        description = Gtk.Label()
        description.set_text(_("This installer will guide you through the necessary steps to install LIS."))
        description.set_wrap(True)
        description.set_justify(Gtk.Justification.CENTER)
        self.append(description)
        
        # Información adicional
        info = Gtk.Label()
        info.set_markup("<small>" + _("Make sure you have the necessary permissions before continuing.") + "</small>")
        info.set_wrap(True)
        self.append(info)
        
        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)
