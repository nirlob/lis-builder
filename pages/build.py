"""
Página Build - Construir y vista previa del instalador
"""

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class BuildPage(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.set_margin_top(40)
        self.set_margin_bottom(40)
        self.set_margin_start(40)
        self.set_margin_end(40)

        # Título
        title = Gtk.Label()
        title.set_markup("<big><b>Construir Instalador</b></big>")
        self.append(title)

        # Descripción
        description = Gtk.Label()
        description.set_text("Vista previa y construcción del archivo .lis:")
        description.set_wrap(True)
        self.append(description)

        # Panel principal con dos columnas
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        main_box.set_vexpand(True)

        # Columna izquierda: Vista previa
        preview_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        preview_box.set_hexpand(True)

        preview_title = Gtk.Label()
        preview_title.set_markup("<b>Vista Previa</b>")
        preview_title.set_halign(Gtk.Align.START)
        preview_box.append(preview_title)

        # Scrolled window para la vista previa
        preview_scrolled = Gtk.ScrolledWindow()
        preview_scrolled.set_vexpand(True)
        preview_scrolled.set_hexpand(True)

        self.preview_text = Gtk.TextView()
        self.preview_text.set_editable(False)
        self.preview_text.set_wrap_mode(Gtk.WrapMode.WORD)

        # Texto de ejemplo de vista previa
        buffer = self.preview_text.get_buffer()
        preview_content = """[LIS Installer Configuration]
Name=Mi Aplicación
Version=1.0.0
Description=Una aplicación de ejemplo
License=GPL v3
RequireAdmin=false

[Files]
bin/mi_aplicacion
lib/librerias.so
config/config.ini

[Directories]
InstallDir=$HOME/Aplicaciones/MiAplicacion
DataDir=$HOME/.config/MiAplicacion

[Requirements]
MinDistro=Cualquier distribución
Dependencies=gtk3, libssl

[Installer]
OutputFile=setup.lis
InstallerIcon=icon.png
CreateDesktopShortcut=true
CreateMenuEntry=true
RunAfterInstall=false
CreateUninstaller=true
Language=Español

[Environment]
PATH=$INSTALLDIR/bin:$PATH

[PostInstall]
chmod +x $INSTALLDIR/bin/mi_aplicacion
ln -sf $INSTALLDIR/bin/mi_aplicacion $HOME/.local/bin/

[Configuration]
.desktop -> /usr/share/applications/
.service -> $HOME/.config/systemd/user/
"""
        buffer.set_text(preview_content)

        preview_scrolled.set_child(self.preview_text)
        preview_box.append(preview_scrolled)

        main_box.append(preview_box)

        # Columna derecha: Opciones de construcción
        build_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        build_box.set_hexpand(False)
        build_box.set_size_request(250, -1)

        build_title = Gtk.Label()
        build_title.set_markup("<b>Opciones de Construcción</b>")
        build_title.set_halign(Gtk.Align.START)
        build_box.append(build_title)

        # Botón de actualizar vista previa
        update_button = Gtk.Button(label="Actualizar Vista Previa")
        update_button.add_css_class("suggested-action")
        build_box.append(update_button)

        # Separador
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        build_box.append(separator)

        # Opciones de validación
        validate_label = Gtk.Label()
        validate_label.set_text("Validaciones:")
        validate_label.set_halign(Gtk.Align.START)
        build_box.append(validate_label)

        self.validate_files_checkbox = Gtk.CheckButton()
        self.validate_files_checkbox.set_active(True)
        self.validate_files_checkbox.set_label("Verificar archivos")
        build_box.append(self.validate_files_checkbox)

        self.validate_paths_checkbox = Gtk.CheckButton()
        self.validate_paths_checkbox.set_active(True)
        self.validate_paths_checkbox.set_label("Verificar rutas")
        build_box.append(self.validate_paths_checkbox)

        self.validate_icons_checkbox = Gtk.CheckButton()
        self.validate_icons_checkbox.set_active(True)
        self.validate_icons_checkbox.set_label("Verificar iconos")
        build_box.append(self.validate_icons_checkbox)

        # Separador
        separator2 = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        build_box.append(separator2)

        # Botón de construir
        build_final_button = Gtk.Button(label="Construir .lis")
        build_final_button.add_css_class("suggested-action")
        build_final_button.set_size_request(-1, 50)
        build_box.append(build_final_button)

        # Información de progreso
        self.progress_label = Gtk.Label()
        self.progress_label.set_text("Listo para construir")
        self.progress_label.set_wrap(True)
        build_box.append(self.progress_label)

        main_box.append(build_box)

        self.append(main_box)