"""
Página de Administrador para LIS Builder
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import gettext
gettext.bindtextdomain('lis-builder', 'locale')
gettext.textdomain('lis-builder')
_ = gettext.gettext


class AdministratorPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)
        
        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>" + _("Administrator Configuration") + "</b></big>")
        self.append(title)
        
        # Descripción
        description = Gtk.Label()
        description.set_text(_("Enter the system administrator data:"))
        description.set_wrap(True)
        self.append(description)
        
        # Formulario
        form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        
        # Usuario
        user_label = Gtk.Label()
        user_label.set_text(_("User:"))
        user_label.set_halign(Gtk.Align.START)
        form_box.append(user_label)
        
        user_entry = Gtk.Entry()
        user_entry.set_placeholder_text(_("Administrator name"))
        form_box.append(user_entry)
        
        # Contraseña
        password_label = Gtk.Label()
        password_label.set_text(_("Password:"))
        password_label.set_halign(Gtk.Align.START)
        form_box.append(password_label)
        
        password_entry = Gtk.Entry()
        password_entry.set_placeholder_text(_("Password"))
        password_entry.set_visibility(False)
        form_box.append(password_entry)
        
        # Email
        email_label = Gtk.Label()
        email_label.set_text(_("Email:"))
        email_label.set_halign(Gtk.Align.START)
        form_box.append(email_label)
        
        email_entry = Gtk.Entry()
        email_entry.set_placeholder_text("email@example.com")
        form_box.append(email_entry)
        
        self.append(form_box)
        
        # Espaciador
        spacer = Gtk.Box()
        spacer.set_vexpand(True)
        self.append(spacer)
