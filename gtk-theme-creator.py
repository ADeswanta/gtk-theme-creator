import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio

welcome = Gtk.Builder()
welcome.add_from_file("ui/welcome.ui")

class Handler:
    def destroy(self, *args):
        Gtk.main_quit()
    def hideDialog(self, *args):
        hideDialog()
    def newHide(self, *args):
        welcome.get_object("newProjectDialog").hide()
        return True
    def newProject(self, *args):
        welcome.get_object("newProjectDialog").show_all()
    def openEditor(self, *args):
        welcome.get_object("newProjectDialog").hide()
        welcome.get_object("mainWindow").hide()
        import editor

welcome.connect_signals(Handler())

mainWindow = welcome.get_object("mainWindow")
mainWindow.show_all()

Gtk.main()