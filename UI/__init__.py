from PySide6.QtCore import QFile
from PySide6.QtWidgets import (QCheckBox, QComboBox, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QSlider, QTabWidget, QTableWidget, QTextBrowser, QTextEdit)
from PySide6.QtUiTools import QUiLoader

from UI.ui_console import UIConsole
from UI.ui_interactive import UIInteractive


"""
Class for loading the UI and navigating UI elements.
Inherits and initialises all other UI class sections.
"""
class CustomMainWindow(QMainWindow, UIConsole, UIInteractive):
    def __init__(self):
        self.loadUI("UI/mainwindow.ui")
        super().__init__() # Base class is initialised here after loading the UI, doing this before causing errors locating findChild method.
        self.window.raise_()
        self.window.activateWindow()
        self.window.setFixedSize(self.window.size())
        self.window.show()


    """
    Attempts to load the UI file.

    @param file: File path to the UI file.
    """
    def loadUI(self, ui_file_path):
        try:
            print(f"Loading UI")
            ui_file = QFile(ui_file_path)
            ui_file.open(QFile.ReadOnly)
            loader = QUiLoader()
            self.window = loader.load(ui_file)
            self.window.setWindowTitle("Music Pirate")
            ui_file.close()
        except Exception as e:
            print(f"E1: {__file__}: {e}")


    """
    Locates and stores check box as new attribute.

    @param name: Name of the check box.
    """
    def append_QCheckBox(self, name):
        setattr(self, name, self.window.findChild(QCheckBox, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QCheckBox: {name}")


    """
    Locates and stores combo box as new attribute.

    @param name: Name of the combo box.
    """
    def append_QComboBox(self, name):
        setattr(self, name, self.window.findChild(QComboBox, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QComboBox: {name}")


    """
    Locates and stores line edit as new attribute.

    @param name: Name of the line edit.
    """
    def append_QLineEdit(self, name):
        setattr(self, name, self.window.findChild(QLineEdit, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QLineEdit: {name}")


    """
    Locates and stores progress bar as new attribute.

    @p  aram name: Name of the progress bar.
    """
    def append_QProgressBar(self, name):
        setattr(self, name, self.window.findChild(QProgressBar, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QProgressBar: {name}")


    """
    Locates and stores push button as new attribute.

    @p  aram name: Name of the push button.
    """
    def append_QPushButton(self, name):
        setattr(self, name, self.window.findChild(QPushButton, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QPushButton: {name}")


    """
    Locates and stores radio button as new attribute.

    @param name: Name of the radio button.
    """
    def append_QRadioButton(self, name):
        setattr(self, name, self.window.findChild(QRadioButton, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QRadioButton: {name}")


    """
    Locates and stores slider as new attribute.

    @param name: Name of the slider.
    """
    def append_QSlider(self, name):
        setattr(self, name, self.window.findChild(QSlider, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QSlider: {name}")


    """
    Locates and stores tab widget as new attribute.

    @param name: Name of the tab widget.
    """
    def append_QTabWidget(self, name):
        setattr(self, name, self.window.findChild(QTabWidget, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QTabWidget: {name}")


    """
    Locates and stores table widget as new attribute.

    @param name: Name of the table widget.
    """
    def append_QTableWidget(self, name):
        setattr(self, name, self.window.findChild(QTableWidget, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QTableWidget: {name}")


    """
    Locates and stores text browser as new attribute.

    @param name: Name of the text browser.
    """
    def append_QTextBrowser(self, name):
        setattr(self, name, self.window.findChild(QTextBrowser, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QTextBrowser: {name}")


    """
    Locates and stores text edit as new attribute.

    @param name: Name of the text edit.
    """
    def append_QTextEdit(self, name):
        setattr(self, name, self.window.findChild(QTextEdit, name))
        if getattr(self, name) == None:
            print(f"Error! Unable to find QTextEdit: {name}")