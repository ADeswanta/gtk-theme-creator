import gi, json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

settingEditor_command = ""

def loadSetings(ui):
    settingsData = json.loads(open("settings.json", "r").read())
    ui.get_object("settingDirLabel").set_text(settingsData["settingDir"])
    ui.get_object("settingEditorLabel").set_text(settingsData["settingEditor"]["name"])

def saveSettings(ui):
    settingsData = json.loads(open("settings.json", "r").read())
    settingsData["settingDir"] = ui.get_object("settingDirLabel").get_text()
    settingsData["settingEditor"]["name"] = ui.get_object("settingEditorLabel").get_text()
    settingsData["settingEditor"]["command"] = settingEditor_command
    json.dump(settingsData, open("settings.json", "w"), indent=4)

def getSettings():
    settingsData = json.loads(open("settings.json", "r").read())
    return settingsData

def settingDir(parent, output):
    dialog = Gtk.FileChooserDialog(
        title="Please choose a location", parent=parent, action=Gtk.FileChooserAction.SELECT_FOLDER)
    dialog.add_buttons(
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK)
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        output.set_text(dialog.get_filename())
    dialog.destroy()

def settingEditor(parent, output):
    global settingEditor_command
    dialog = Gtk.AppChooserDialog(
        title="Please choose default text editor", parent=parent, content_type="text/plain")
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        output.set_text(dialog.get_app_info().get_display_name())
        settingEditor_command = dialog.get_app_info().get_commandline()
    dialog.destroy()