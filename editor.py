import gi, settings

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio, GLib

editor = Gtk.Builder()
editor.add_from_file("ui/editor.ui")

previewProc = Gio.Subprocess.new(["python3", "preview.py"], 0)

def getPreviewStatus():
    if previewProc.get_if_exited():
        editor.get_object("previewButton").set_sensitive(True)
    return GLib.SOURCE_CONTINUE

def setTitle(projectName, projectDir):
    editor.get_object("editorTitle").set_title(projectName)
    editor.get_object("editorTitle").set_subtitle(projectDir)

class editorHandler:
    def init(self, *args):
        editor.get_object("aboutDialog").set_transient_for(editor.get_object("editorWindow"))
        editor.get_object("settingsDialog").set_transient_for(editor.get_object("editorWindow"))
    def destroy(self, *args):
        previewProc.force_exit()
        Gtk.main_quit()
    def settings(self, *args):
        editor.get_object("settingsDialog").show_all()
        settings.loadSetings(editor)
    def settingsHide(self, *args):
        editor.get_object("settingsDialog").hide()
        return True
    def about(self, *args):
        editor.get_object("aboutDialog").show_all()
    def aboutHide(self, *args):
        editor.get_object("aboutDialog").hide()
        return True
    def preview(self, *args):
        global previewProc
        previewProc = Gio.Subprocess.new(["python3", "preview.py"], 0)
        editor.get_object("previewButton").set_sensitive(False)
    def settingAction(self, listbox, listboxrow):
        if listboxrow.get_index() == 0:
            settings.settingDir(editor.get_object("settingsDialog"), editor.get_object("settingDirLabel"))
        elif listboxrow.get_index() == 1:
            settings.settingEditor(editor.get_object("settingsDialog"), editor.get_object("settingEditorLabel"))
        settings.saveSettings(editor)

editor.connect_signals(editorHandler())

window = editor.get_object("editorWindow")
window.show_all()

GLib.timeout_add(100,getPreviewStatus)