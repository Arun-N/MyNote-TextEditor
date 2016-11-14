# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myNoteUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QFileDialog
from PyQt4.QtGui import *
from PyQt4.QtCore import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MyNote(object):

    filters = ['All (*.*)', 'Text File (*.txt)', 'Rich Text File (*.rtf)', 'Hyper Text Markup Language (*.html)',
               'PHP Hypertext Preprocessor (*.php)', 'Cascade Style Sheet (*.css)', 'Javascript (*.js)', 'C (*.c)',
               'C++ (*.cpp)']

    font_sizes = ['8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36', '38', '40']

    def setupUi(self, MyNote):
        MyNote.setObjectName(_fromUtf8("MyNote"))
        MyNote.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 103, 103))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        MyNote.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("myNoteIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MyNote.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MyNote)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 537))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Author = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.Author.setObjectName(_fromUtf8("Author"))
        self.gridLayout_2.addWidget(self.Author, 2, 0, 1, 1)
        self.writing_pad = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)

        self.writing_pad.setPalette(palette)
        self.writing_pad.setFrameShape(QtGui.QFrame.StyledPanel)
        self.writing_pad.setFrameShadow(QtGui.QFrame.Sunken)
        self.writing_pad.setObjectName(_fromUtf8("writing_pad"))
        self.writing_pad.setAcceptRichText(True)
        # self.writing_pad.setFontPointSize(14)

        self.gridLayout_2.addWidget(self.writing_pad, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.font_box = QtGui.QFontComboBox(self.scrollAreaWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 196, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 196, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 196, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)

        self.font_box.setPalette(palette)
        self.font_box.setEditable(False)
        self.font_box.setObjectName(_fromUtf8("font_box"))
        self.font_box.activated.connect(self.font_format)

        self.gridLayout_3.addWidget(self.font_box, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.font_size = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.font_size.setEditable(True)
        self.font_size.setObjectName(_fromUtf8("font_size"))
        self.font_size.addItems(self.font_sizes)
        self.font_size.setStyleSheet("QComboBox {background-color : white}")
        self.font_size.activated.connect(self.font_format)
        # self.font_size.setCurrentIndex(3)

        self.gridLayout_3.addWidget(self.font_size, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MyNote.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MyNote)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuFiles = QtGui.QMenu(self.menubar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))

        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))

        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))

        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))

        MyNote.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MyNote)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MyNote.setStatusBar(self.statusbar)

        self.actionNew_File = QtGui.QAction(MyNote)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))

        self.actionSave_File = QtGui.QAction(MyNote)
        self.actionSave_File.setObjectName(_fromUtf8("actionSave_File"))
        self.actionSave_File.triggered.connect(self.save_file)

        self.actionOpen_File = QtGui.QAction(MyNote)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionOpen_File.triggered.connect(self.open_file)

        self.actionExit = QtGui.QAction(MyNote)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.exit_editor)

        self.actionFind = QtGui.QAction(MyNote)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))

        self.actionReplace = QtGui.QAction(MyNote)
        self.actionReplace.setObjectName(_fromUtf8("actionReplace"))

        self.actionSettings = QtGui.QAction(MyNote)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))

        self.actionAbout_MyNote = QtGui.QAction(MyNote)
        self.actionAbout_MyNote.setObjectName(_fromUtf8("actionAbout_MyNote"))

        self.menuFiles.addAction(self.actionNew_File)
        self.menuFiles.addAction(self.actionSave_File)
        self.menuFiles.addAction(self.actionOpen_File)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionExit)
        self.menuTools.addAction(self.actionFind)
        self.menuTools.addAction(self.actionReplace)
        self.menuOptions.addAction(self.actionSettings)
        self.menuAbout.addAction(self.actionAbout_MyNote)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.save_msg_box = QMessageBox()
        self.save_msg_box.setText("Save before exiting ?")
        self.save_msg_box.setWindowTitle("Save ?")
        self.save_icon = QIcon()
        self.save_icon.addPixmap(QtGui.QPixmap(_fromUtf8("save_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_msg_box.setWindowIcon(self.save_icon)
        self.save_msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.save_msg_box.buttonClicked.connect(self.msg_save_file)

        self.retranslateUi(MyNote)
        QtCore.QMetaObject.connectSlotsByName(MyNote)

    def retranslateUi(self, MyNote):
        MyNote.setWindowTitle(_translate("MyNote", "MyNote", None))
        self.Author.setText(_translate("MyNote", "MyNote created by Arun Nair", None))
        self.label_2.setText(_translate("MyNote", "Font Style", None))
        self.label.setText(_translate("MyNote", "Font Size", None))
        self.menuFiles.setTitle(_translate("MyNote", "Files", None))
        self.menuTools.setTitle(_translate("MyNote", "Tools", None))
        self.menuOptions.setTitle(_translate("MyNote", "Options", None))
        self.menuAbout.setTitle(_translate("MyNote", "About", None))
        self.actionNew_File.setText(_translate("MyNote", "New File", None))
        self.actionSave_File.setText(_translate("MyNote", "Save As ...", None))
        self.actionOpen_File.setText(_translate("MyNote", "Open ...", None))
        self.actionExit.setText(_translate("MyNote", "Exit", None))
        self.actionFind.setText(_translate("MyNote", "Find", None))
        self.actionReplace.setText(_translate("MyNote", "Replace", None))
        self.actionSettings.setText(_translate("MyNote", "Settings", None))
        self.actionAbout_MyNote.setText(_translate("MyNote", "About MyNote", None))

    def exit_editor(self):
        retval = self.save_msg_box.exec_()
        self.save_info()
        QApplication.quit()

    def open_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilters(self.filters)

        file_name = list()

        if dlg.exec_():
            file_name = dlg.selectedFiles()
            f = open(file_name[0], 'r')
            with f:
                data = f.read()
                self.writing_pad.setText(data)

    def save_file(self):
        dlg_save = QFileDialog()
        save_file_name, my_filter = QtGui.QFileDialog.getSaveFileNameAndFilter(dlg_save, 'Save File', '', 'All Files (*.*);;Text File (*.txt);;Rich Text File (*.rtf);;Hyper Text Markup Language (*.html *.htm);;PHP Hypertext Preprocessor (*.php);;Python (*.py);;Javascript(*.js);;CSS (*.css);;C (*.c);;C++ (*.cpp);;Convert to HTML (*.html)')
        print(save_file_name)
        print(my_filter)

        if save_file_name != '' and my_filter != '':
            f = open(save_file_name, 'w')
            with f:
                if my_filter == 'Convert to HTML (*.html)':
                    data_wr = self.writing_pad.toHtml()
                else:
                    data_wr = self.writing_pad.toPlainText()
                f.write(data_wr)
        else:
            print("File not saved")

    def msg_save_file(self, opn):
        if opn.text() == 'OK':
            dlg_msg_save = QFileDialog()
            save_file_name, my_filter = QtGui.QFileDialog.getSaveFileNameAndFilter(dlg_msg_save, 'Save File', '', 'All Files (*.*);;Text Files (*.txt);;Rich Text File (*.rtf);;Hyper Text Markup Language (*.html *.htm);;PHP Hypertext Preprocessor (*.php);;Python (*.py);;Javascript(*.js);;CSS (*.css);;C (*.c);;C++ (*.cpp);;Convert to HTML (*.html)')
            print(save_file_name)
            print(my_filter)

            if save_file_name != '' and my_filter != '':
                f = open(save_file_name, 'w')
                with f:
                    if my_filter == 'Convert to HTML (*.html)':
                        data_wr = self.writing_pad.toHtml()
                    else:
                        data_wr = self.writing_pad.toPlainText()
                    f.write(data_wr)
            else:
                print("File not saved")
            print("OK pressed")

        else:
            print("Cancel pressed")

    def font_format(self):
        font = QtGui.QFont()
        f_style = self.font_box.currentText()
        f_size = int(self.font_size.currentText())
        font.setPointSize(f_size)
        font.setFamily(f_style)
        self.writing_pad.setFont(font)

    def save_info(self):
        print("save started")
        q_setting = QSettings("Arun", "MyNote")
        q_setting.setValue("font_style", self.font_box.currentText())
        q_setting.setValue("font_style_index", self.font_box.currentIndex())
        q_setting.setValue("font_size", int(self.font_size.currentText()))
        q_setting.setValue("font_size_index", self.font_size.currentIndex())
        print("save ended")

    def read_info(self):
        print("read entered")
        q_setting = QSettings("Arun", "MyNote")
        f_style = q_setting.value("font_style", type=str)
        f_style_index = q_setting.value("font_style_index", type=int)
        f_size = q_setting.value("font_size", type=int)
        f_size_index = q_setting.value("font_size_index", type=int)
        print(f_style)
        print(f_size)

        if f_size <= 0:
            font = QtGui.QFont()
            font.setPointSize(14)
            self.font_size.setCurrentIndex(3)
            font.setFamily("Arial")
            self.font_box.setCurrentIndex(1)
            self.writing_pad.setFont(font)

        else:
            font = QtGui.QFont()
            font.setPointSize(f_size)
            font.setFamily(f_style)
            self.font_box.setCurrentIndex(f_style_index)
            self.font_size.setCurrentIndex(f_size_index)
            self.writing_pad.setFont(font)

        print("read ended")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MyNote = QtGui.QMainWindow()
    ui = Ui_MyNote()
    ui.setupUi(MyNote)
    ui.read_info()
    MyNote.show()
    sys.exit(app.exec_())
