import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio, GLib

editor = Gtk.Builder()
editor.add_from_file("ui/editor.ui")

previewProc = Gio.Subprocess.new(["python3", "preview.py"], 0)

def getPreviewStatus():
    if previewProc.get_if_exited():
        editor.get_object("previewButton").set_sensitive(True)
    return GLib.SOURCE_CONTINUE

class Handler:
    def destroy(self, *args):
        previewProc.force_exit()
        Gtk.main_quit()
    def aboutHide(self, *args):
        editor.get_object("aboutDialog").hide()
        return True
    def preview(self, *args):
        global previewProc
        previewProc = Gio.Subprocess.new(["python3", "preview.py"], 0)
        editor.get_object("previewButton").set_sensitive(False)
    def about(self, *args):
        editor.get_object("aboutDialog").show_all()

editor.connect_signals(Handler())

window = editor.get_object("editorWindow")
window.show_all()

GLib.timeout_add(100,getPreviewStatus)