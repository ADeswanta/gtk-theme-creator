import gi, settings, fileManager

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

welcome = Gtk.Builder()
welcome.add_from_file("ui/welcome.ui")

editor = Gtk.Builder()
editor.add_from_file("ui/editor.ui")

def hide_window(window, event):
    window.hide()
    return True

def settingAction(listbox, listboxrow):
    if listboxrow.get_index() == 0:
        settings.settingDir(editor.get_object("settingsDialog"), editor.get_object("settingDirLabel"))
    elif listboxrow.get_index() == 1:
        settings.settingEditor(editor.get_object("settingsDialog"), editor.get_object("settingEditorLabel"))
    settings.saveSettings(editor)

class welcomeHandler:
    def init(self, *args):
        editor.get_object("aboutDialog").set_transient_for(welcome.get_object("mainWindow"))
        editor.get_object("aboutDialog").connect("delete-event", hide_window)
        editor.get_object("settingsDialog").set_transient_for(welcome.get_object("mainWindow"))
        editor.get_object("settingsDialog").connect("delete-event", hide_window)
        editor.get_object("settingsList").connect("row-activated", settingAction)
    def destroy(self, *args):
        Gtk.main_quit()
    def newHide(self, *args):
        welcome.get_object("newProjectDialog").hide()
        return True
    def settings(self, *args):
        editor.get_object("settingsDialog").show_all()
        settings.loadSetings(editor)
    def about(self, *args):
        editor.get_object("aboutDialog").show_all()
    def newProject(self, *args):
        welcome.get_object("newProjectDialog").show_all()
        welcome.get_object("projectDir").set_text(settings.getSettings()["settingDir"])
    def openProject(self, *args):
        dialog = Gtk.FileChooserDialog(
            title="Open Project", parent=welcome.get_object("mainWindow"), action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            welcome.get_object("mainWindow").hide()
            import editor
            editor.setInfo(str(dialog.get_filename()).split('/')[-1], "/".join(str(dialog.get_filename()).split('/')[:-1]))
        dialog.destroy()
    def cancelNew(self, *args):
        welcome.get_object("projectName").set_text("Untitled Theme")
    def openEditor(self, *args):
        welcome.get_object("newProjectDialog").hide()
        welcome.get_object("mainWindow").hide()
        welcome.get_object("projectName").set_text(str(welcome.get_object("projectName").get_text()).replace(" ", "-"))
        if welcome.get_object("gtk3Check").get_active():
           fileManager.createGTK3(welcome.get_object("projectName").get_text(), welcome.get_object("projectDir").get_text())
        if welcome.get_object("gtk4Check").get_active():
           fileManager.createGTK4(welcome.get_object("projectName").get_text(), welcome.get_object("projectDir").get_text())
        import editor
        editor.setInfo(welcome.get_object("projectName").get_text(), welcome.get_object("projectDir").get_text())
    def browseDir(self, *args):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a location", parent=welcome.get_object("newProjectDialog"), action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            welcome.get_object("projectDir").set_text(dialog.get_filename()) 
        dialog.destroy()

welcome.connect_signals(welcomeHandler())

mainWindow = welcome.get_object("mainWindow")
mainWindow.show_all()

Gtk.main()