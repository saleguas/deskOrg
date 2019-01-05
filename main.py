import gi
import os
import shutil

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

filepath = Gtk.Label()

class MainWindow(Gtk.Window):
		
	global filepath

	def __init__(self):
		Gtk.Window.__init__(self, title="Desktop organizer")
		self.set_border_width(30)
		grid = Gtk.Grid()
		self.add(grid)

		dchooser = Gtk.Button("Choose directory")
		gogo = Gtk.Button("Start")
		filepath.set_label("No directory selected.")
		dchooser.connect("clicked", self.on_clicked)
		gogo.connect("clicked", self.sorting_time)
		grid.add(dchooser)

		# grid.attach(filepath, 0, 2, 2, 1)
		grid.attach_next_to(filepath, dchooser, Gtk.PositionType.BOTTOM, 1, 2)
		grid.attach_next_to(gogo, filepath, Gtk.PositionType.BOTTOM, 1, 5)
		# grid.add(dchooser)

		



############################################################################
	def on_clicked(self, widget):

		dialog = Gtk.FileChooserDialog("Select a directory",self,Gtk.FileChooserAction.SELECT_FOLDER,("Cancel", Gtk.ResponseType.CANCEL,"Ok", Gtk.ResponseType.OK))
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			filepath.set_label(dialog.get_filename())
		elif response == Gtk.ResponseType.CANCEL:
			print("Nothing selected")

		dialog.destroy()

	def sorting_time(self, widget):
		if filepath.get_text() != "No directory selected.":
			print("yep")
			for file in os.listdir(filepath.get_text()):
				if "." in file:
					destination = (filepath.get_text() + "/" + "_" + file[file.index(".") + 1:] )
					source = filepath.get_text() + "/" + file
					try:
						os.mkdir(destination)
					except FileExistsError:
						print("it exists")
					print(destination)
					print(source)
					shutil.move(source, destination)





		else:
			dialogg = PopUp(self)
			response = dialogg.run()
			if response == Gtk.ResponseType.OK:
				print("Closed")

			dialogg.destroy()


class PopUp(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Error", parent, Gtk.DialogFlags.MODAL
		, ("OK", Gtk.ResponseType.OK))

		self.set_default_size(200, 100)
		self.set_border_width(30)

		area = self.get_content_area()
		area.add(Gtk.Label("Please select a directory"))
		self.show_all()


window = MainWindow()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
