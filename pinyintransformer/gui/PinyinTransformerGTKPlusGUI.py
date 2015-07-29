from gi.repository import Gtk

from pinyintransformer.PinyinNumbers2TonesTransformer import PinyinNumbers2TonesTransformer
from pinyintransformer.PinyinTones2NumbersTransformer import PinyinTones2NumbersTransformer
from pinyintransformer.exceptions.PinyinParseException import PinyinParseException
from pinyintransformer.parser.PinyinParserMixed import PinyinParserMixed

from pinyintransformer.gui.GTKSignal import GTKSignal
from pinyintransformer.parser.SpecialCharacters import SpecialCharacters

__author__ = 'xiaolong'

class PinyinTransformerGTKGUI(Gtk.Window):
	
	fileMenu = None
	editMenu = None
	optionsMenu = None

	topLevelGridLayoutContainer = None
	
	gridLayout = None
	
	pinyinNumberLabel = None
	pinyinTonesLabel = None

	transform_to_tones_pinyin_button = None
	transform_to_numbers_pinyin_button = None
	
	
	
	def __init__(self):
		self.pinyin_numbers_to_tones_transformer = PinyinNumbers2TonesTransformer()
		self.pinyin_tones_to_numbers_transformer = PinyinTones2NumbersTransformer()
		
		self.pinyin_syllable_parser_mixed = PinyinParserMixed()
		
		Gtk.Window.__init__(self, title="Pīnyīn Transformer")
		
		self.topLevelGridLayoutContainer = Gtk.Grid()
		
		self.numberedPinyinScrolledWindow = Gtk.ScrolledWindow()
		self.numberedPinyinTextView = Gtk.TextView()
		self.numberedPinyinTextBuffer = self.numberedPinyinTextView.get_buffer()
		
		self.tonedPinyinScrolledWindow = Gtk.ScrolledWindow()
		self.tonedPinyinTextView = Gtk.TextView()
		self.tonedPinyinTextBuffer = self.tonedPinyinTextView.get_buffer()
		
		self.initialize()
		
	def initialize(self):
		self.create_gui()
		self.add_signal_listeners()
		self.add_window_signal_listeners()
	
	def create_gui(self):
		self.initialize_controls()
		self.add_controls()
		self.createMenuBar()
	
	def initialize_controls(self):
		# WINDOW
		self.set_default_size(400, 300)
		
		# LAYOUT
		self.gridLayout = Gtk.Grid()
		self.gridLayout.set_margin_left(5)
		self.gridLayout.set_margin_top(5)
		self.gridLayout.set_margin_right(5)
		self.gridLayout.set_margin_bottom(5)
		
		self.gridLayout.set_column_spacing(5)
		self.gridLayout.set_row_spacing(5)
		self.gridLayout.set_column_homogeneous(False)
		self.gridLayout.set_row_homogeneous(False)
		
		# LABELS
		self.pinyinNumberLabel = Gtk.Label()
		self.pinyinNumberLabel.set_label("Pīnyīn (numbers):")
		self.pinyinNumberLabel.set_halign(Gtk.Align.START)
		self.pinyinNumberLabel.set_vexpand(False)
		self.pinyinNumberLabel.set_hexpand(False)
		
		self.pinyinTonesLabel = Gtk.Label()
		self.pinyinTonesLabel.set_label("Pīnyīn (tones):")
		self.pinyinTonesLabel.set_halign(Gtk.Align.START)
		self.pinyinTonesLabel.set_vexpand(False)
		self.pinyinTonesLabel.set_hexpand(False)
		
		# TEXT VIEW
		self.numberedPinyinScrolledWindow.set_hexpand(True)
		self.numberedPinyinScrolledWindow.set_vexpand(True)
		self.numberedPinyinScrolledWindow.set_border_width(2)
		self.numberedPinyinScrolledWindow.set_resize_mode(Gtk.ResizeMode.QUEUE)
		self.numberedPinyinScrolledWindow.set_shadow_type(Gtk.ShadowType.IN)

		self.numberedPinyinTextView.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
		self.numberedPinyinTextView.set_border_width(2)
		self.numberedPinyinTextView.set_accepts_tab(False)
		self.numberedPinyinTextBuffer.set_text("Pin1yin1 ...")
		
		self.tonedPinyinScrolledWindow.set_hexpand(True)
		self.tonedPinyinScrolledWindow.set_vexpand(True)
		self.tonedPinyinScrolledWindow.set_border_width(2)
		self.tonedPinyinScrolledWindow.set_resize_mode(Gtk.ResizeMode.QUEUE)
		self.tonedPinyinScrolledWindow.set_shadow_type(Gtk.ShadowType.IN)

		self.tonedPinyinTextView.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
		self.tonedPinyinTextView.set_border_width(2)
		self.tonedPinyinTextView.set_accepts_tab(False)
		self.tonedPinyinTextBuffer.set_text("Pīnyīn ...")
		
		# BUTTONS
		self.transform_to_tones_pinyin_button = Gtk.Button(label="Transform (tones)")
		self.transform_to_tones_pinyin_button.set_halign(Gtk.Align.START)
		self.transform_to_tones_pinyin_button.set_hexpand(False)
		self.transform_to_tones_pinyin_button.set_vexpand(False)
		
		self.transform_to_numbers_pinyin_button = Gtk.Button(label="Transform (numbers)")
		self.transform_to_numbers_pinyin_button.set_halign(Gtk.Align.START)
		self.transform_to_numbers_pinyin_button.set_hexpand(False)
		self.transform_to_numbers_pinyin_button.set_vexpand(False)
	
	def add_controls(self):
		
		#self.gridLayout.attach(self.menubar, 0, 0, 4, 1)
		
		self.gridLayout.attach(self.pinyinNumberLabel, 0, 1, 1, 1)
		self.gridLayout.attach(self.pinyinTonesLabel, 2, 1, 1, 1)
		
		self.numberedPinyinScrolledWindow.add(self.numberedPinyinTextView)
		self.tonedPinyinScrolledWindow.add(self.tonedPinyinTextView)
		self.gridLayout.attach(self.numberedPinyinScrolledWindow, 0, 2, 2, 4)
		self.gridLayout.attach(self.tonedPinyinScrolledWindow, 2, 2, 2, 4)
		
		self.gridLayout.attach(self.transform_to_tones_pinyin_button, 0, 6, 1, 1)
		self.gridLayout.attach(self.transform_to_numbers_pinyin_button, 2, 6, 1, 1)
		
		self.topLevelGridLayoutContainer.attach(self.gridLayout, 0, 1, 1, 1)
		
		self.add(self.topLevelGridLayoutContainer)
	
	def createMenuBar(self):
		file_menu = Gtk.Menu()
		exit_menu_item = Gtk.MenuItem("Exit")
		exit_menu_item.connect(GTKSignal.ACTIVATE.value, Gtk.main_quit)
		file_menu.append(exit_menu_item)
		
		file_menu_bar_item = Gtk.MenuItem("File")
		file_menu_bar_item.set_submenu(file_menu)
		
		
		edit_menu = Gtk.Menu()
		unnamed_menu_item = Gtk.MenuItem("Unnamed")
		unnamed_menu_item.connect(GTKSignal.ACTIVATE.value, Gtk.main_quit)
		edit_menu.append(unnamed_menu_item)
		
		edit_menu_bar_item = Gtk.MenuItem("Edit")
		edit_menu_bar_item.set_submenu(edit_menu)
		
		
		menu_bar = Gtk.MenuBar()
		menu_bar.append(file_menu_bar_item)
		menu_bar.append(edit_menu_bar_item)
		
		
		self.topLevelGridLayoutContainer.attach(menu_bar, 0, 0, 1, 1)
	
	def add_signal_listeners(self):
		self.transform_to_tones_pinyin_button.connect(GTKSignal.CLICKED.value, self.transform_to_tones_pinyin_button_clicked)
		self.transform_to_numbers_pinyin_button.connect(GTKSignal.CLICKED.value, self.transform_to_numbers_pinyin_button_clicked)
		
	def add_window_signal_listeners(self):
		self.connect(GTKSignal.DELETE_EVENT.value, Gtk.main_quit)
		self.connect(GTKSignal.DESTROY.value, Gtk.main_quit)
	
	def transform_to_tones_pinyin_button_clicked(self, widget):
		start = self.numberedPinyinTextBuffer.get_start_iter()
		end = self.numberedPinyinTextBuffer.get_end_iter()
		hidden_chars = False
		user_input = self.numberedPinyinTextBuffer.get_text(start, end, hidden_chars)
		
		if self.containsTonedVowels(user_input):
			try:
				print("contains tones")
				self.pinyin_syllable_parser_mixed.fastParse(user_input)
				output = self.pinyin_syllable_parser_mixed.getTonedPinyinText()
				self.tonedPinyinTextBuffer.set_text(output)
			except PinyinParseException:
				self.show_invalid_pinyin_error_message()
		else:
			print("does not contain tones")
			try:
				# uses newer faster parser
				self.pinyin_syllable_parser_mixed.fastParse(user_input)
				output = self.pinyin_syllable_parser_mixed.getTonedPinyinText()
				self.tonedPinyinTextBuffer.set_text(output)
				
				# uses slower strict parser 
				# output = self.pinyin_numbers_to_tones_transformer.transform(user_input)
				# self.tonedPinyinTextBuffer.set_text(output)
			except PinyinParseException:
				self.show_invalid_pinyin_error_message()
	
	def transform_to_numbers_pinyin_button_clicked(self, widget):
		start = self.tonedPinyinTextBuffer.get_start_iter()
		end = self.tonedPinyinTextBuffer.get_end_iter()
		hidden_chars = False
		user_input = self.tonedPinyinTextBuffer.get_text(start, end, hidden_chars)
		
		if self.containsDigits(user_input):
			print("contains digits")
			try:
				self.pinyin_syllable_parser_mixed.fastParse(user_input)
				output = self.pinyin_syllable_parser_mixed.getNumberedPinyinText()
				self.numberedPinyinTextBuffer.set_text(output)
			except PinyinParseException:
				self.show_invalid_pinyin_error_message()
		else:
			print("does not contain digits")
			try:
				# uses slower strict parser:
				# output = self.pinyin_tones_to_numbers_transformer.transform(user_input)
				# self.numberedPinyinTextBuffer.set_text(output)
				
				# uses new fast parser
				self.pinyin_syllable_parser_mixed.fastParse(user_input)
				output = self.pinyin_syllable_parser_mixed.getNumberedPinyinText()
				self.numberedPinyinTextBuffer.set_text(output)
				
			except PinyinParseException:
				self.show_invalid_pinyin_error_message()
	
	@staticmethod
	def show_invalid_pinyin_error_message():
		print("invalid pinyin")
	
	@staticmethod
	def containsTonedVowels(text):
		for toned_vowel in SpecialCharacters.TONED_VOWELS.value:
			if toned_vowel in text:
				return True
		return False
	
	@staticmethod
	def containsDigits(text):
		for digit in [x for x in range(0, 9)]:
			if str(digit) in text:
				return True
		return False
	
if __name__ == '__main__':
	window = PinyinTransformerGTKGUI()
	window.show_all()
	Gtk.main()