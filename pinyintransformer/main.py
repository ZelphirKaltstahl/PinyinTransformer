from gi.repository import Gtk

from pinyintransformer.gui.PinyinTransformerGTKPlusGUI import PinyinTransformerGTKGUI


__author__ = 'Xiaolong'

import sys


def main(args):
	pinyin_transformer_main_window = PinyinTransformerGTKGUI()
	pinyin_transformer_main_window.show_all()
	Gtk.main()

if __name__ == '__main__':
	main(sys.argv)