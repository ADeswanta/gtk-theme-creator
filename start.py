import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk

preview = Gtk.Builder()
preview.add_from_file("ui/preview.ui")

window = preview.get_object("main")
window.show_all()

Gtk.main()