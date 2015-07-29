from pinyintransformer.PinyinTones2NumbersTransformer import PinyinTones2NumbersTransformer

__author__ = 'Xiaolong'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from pinyintransformer.PinyinNumbers2TonesTransformer import PinyinNumbers2TonesTransformer
from pinyintransformer.exceptions.PinyinParseException import PinyinParseException

class PinyinTransformerMainWindow(QMainWindow):

	# creates a signal closeApp, which is connected to the close function of QtMainWindow
	closeApp = pyqtSignal()

	fileMenu = None
	editMenu = None
	optionsMenu = None

	exitAction = None

	contentWidget = None

	contentLayout = None
	leftLayout = None
	rightLayout = None

	leftQLabel = None
	rightQLabel = None

	leftTextEdit = None
	rightTextEdit = None

	# BUTTONS
	leftButtonHBoxLayout = None
	rightButtonHBoxLayout = None

	leftTransformButton = None
	rightTransformButton = None

	def __init__(self, parent=None): # widgets with no parents are windows
		super(PinyinTransformerMainWindow, self).__init__(parent)
		
		#print(QTextCodec.availableCodecs())
		#QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))
		#QTextCodec.setCodecForCStrings()
		
		self.pinyin_numbers_to_tones_transformer = PinyinNumbers2TonesTransformer()
		self.pinyin_tones_to_numbers_transformer = PinyinTones2NumbersTransformer()
		self.createGUI()

	def createGUI(self):
		self.closeApp.connect(self.close)
		self.setWindowTitle('Pinyin Transformer')

		self.createMenuBar()
		self.addMenuEventHandlers()

		self.createControls()
		self.addControlsEventHandlers()

	def createMenuBar(self):
		# MENUS
		self.fileMenu = QMenu('&File', self)
		self.menuBar().addMenu(self.fileMenu)

		self.editMenu = QMenu('&Edit', self)
		self.menuBar().addMenu(self.editMenu)

		self.optionsMenu = QMenu('&Options', self)
		self.menuBar().addMenu(self.optionsMenu)

		# ACTIONS
		self.exitAction = QAction('E&xit', self)
		self.fileMenu.addAction(self.exitAction)

	def addMenuEventHandlers(self):
		# connect the exit action to the emit function of the closeApp signal
		self.exitAction.triggered.connect(self.closeApp.emit)
		# self.exit_action.triggered.connect(QCoreApplication.instance().quit)

	def createControls(self):
		# CENTRAL WIDGET of QMainWindow
		self.contentWidget = QWidget()

		# LAYOUTS
		self.contentLayout = QHBoxLayout()

		self.leftLayout = QVBoxLayout()
		self.contentLayout.addLayout(self.leftLayout)

		self.rightLayout = QVBoxLayout()
		self.contentLayout.addLayout(self.rightLayout)

		self.contentWidget.setLayout(self.contentLayout)
		self.setCentralWidget(self.contentWidget)

		# CONTROLS LEFT
		self.leftQLabel = QLabel('Pīnyīn (numbers):')
		self.leftTextEdit = QPlainTextEdit('', self)
		self.leftTransformButton = QPushButton('Transform (tones)')

		self.leftLayout.addWidget(self.leftQLabel)
		self.leftLayout.addWidget(self.leftTextEdit)

		# LEFT BUTTON LAYOUT
		self.leftButtonHBoxLayout = QHBoxLayout()
		self.leftButtonHBoxLayout.addWidget(self.leftTransformButton)
		self.leftButtonHBoxLayout.addStretch(1)

		self.leftLayout.addLayout(self.leftButtonHBoxLayout)

		# CONTROLS RIGHT
		self.rightQLabel = QLabel('Pīnyīn (tones):')
		self.rightTextEdit = QPlainTextEdit('', self)
		self.rightTransformButton = QPushButton('Transform (numbers)')

		self.rightLayout.addWidget(self.rightQLabel)
		self.rightLayout.addWidget(self.rightTextEdit)

		# RIGHT BUTTON LAYOUT
		self.rightButtonHBoxLayout = QHBoxLayout()
		self.rightButtonHBoxLayout.addWidget(self.rightTransformButton)
		self.rightButtonHBoxLayout.addStretch(1)

		self.rightLayout.addLayout(self.rightButtonHBoxLayout)

	def addControlsEventHandlers(self):
		self.leftTransformButton.clicked.connect(self.transformToPinyinWithTones)
		self.rightTransformButton.clicked.connect(self.transformToPinyinWithNumbers)
		#qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

	def closeEvent(self, event):
		""" Overrides the close function in QMainWindow. """
		reply = QMessageBox.question(
			self,
			"Exit Confirmation",
			"Are you sure you want to exit Pīnyīn Transformer?",
			QMessageBox.No,
			QMessageBox.Yes
		)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def transformToPinyinWithTones(self):
		# self.rightTextEdit.setPlainText('yóuxiāngdìzhǐ')
		user_input = self.leftTextEdit.toPlainText()#
		# print("User input left:", self.leftTextEdit.toPlainText().encode('utf-8').decode('utf-8'))
		print("Condition:", self.leftTextEdit.toPlainText() == "yóuxiāngdìzhǐ")
		
		try:
			output = self.pinyin_numbers_to_tones_transformer.transform(user_input)
			#print(output)
			self.rightTextEdit.clear()
			self.rightTextEdit.setPlainText(output)
		
		# self.rightTextEdit.insertPlainText(output)
		except PinyinParseException:
			self.showInvalidPinyinErrorMessage()

	def transformToPinyinWithNumbers(self):
		user_input = self.rightTextEdit.toPlainText()#.encode(encoding="utf-8").decode(encoding="utf-8")
		# print("User input right:", userInput)
		print("Condition:", self.leftTextEdit.toPlainText() == "yóuxiāngdìzhǐ")
		
		try:
			output = self.pinyin_tones_to_numbers_transformer.transform(user_input)
			#print(output)
			self.leftTextEdit.clear()
			self.leftTextEdit.setPlainText(output)
		
		# self.rightTextEdit.insertPlainText(output)
		except PinyinParseException:
			self.showInvalidPinyinErrorMessage()

	def showInvalidPinyinErrorMessage(self):
		QMessageBox.question(
			self,
			'Invalid Pīnyīn',
			"The Pīnyīn you entered is not valid.",
			QMessageBox.Ok
		)
