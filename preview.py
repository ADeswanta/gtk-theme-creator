import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib

preview = Gtk.Builder()
preview.add_from_file("ui/preview.ui")

def updateCSS():
    provider.load_from_path("gtk.css")
    return GLib.SOURCE_CONTINUE

class Handler:
    def destroy(self, *args):
        Gtk.main_quit()

preview.connect_signals(Handler())

Gtk.Settings.get_default().set_property("gtk-theme-name", "Empty")
provider = Gtk.CssProvider()
provider.load_from_path("gtk.css")
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

window = preview.get_object("previewWindow")
window.show_all()

GLib.timeout_add(100,updateCSS)

Gtk.main()