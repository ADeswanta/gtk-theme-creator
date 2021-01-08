import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def preview(self, *args):
        showPreview()

def showPreview():
    preview = Gtk.Builder()
    preview.add_from_file("ui/preview.ui")
    provider = Gtk.CssProvider()
    provider.load_from_path("gtk.css")
    previewWindow = preview.get_object("main")
    previewWindow.show_all()
    Gtk.StyleContext.add_provider(Gtk.Widget.get_style_context(previewWindow), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

editor = Gtk.Builder()
editor.add_from_file("ui/editor.ui")
editor.connect_signals(Handler())

window = editor.get_object("main")
window.show_all()

Gtk.main()