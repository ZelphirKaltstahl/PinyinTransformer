#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This example shows a simple menu
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009

from gi.repository import Gtk


class PyApp(Gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Simple menu")
        self.set_size_request(250, 200)
        #self.modify_bg(Gtk.StateType.NORMAL,  Gtk.Color(6400, 6400, 6440))
        #self.set_position( Gtk.WIN_POS_CENTER)

        mb =  Gtk.MenuBar()

        filemenu =  Gtk.Menu()
        file_menu_item =  Gtk.MenuItem("File")
        file_menu_item.set_submenu(filemenu)
       
        exit_menu_item =  Gtk.MenuItem("Exit")
        exit_menu_item.connect("activate",  Gtk.main_quit)
        filemenu.append(exit_menu_item)

        mb.append(file_menu_item)

        vbox =  Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        
PyApp()
Gtk.main()