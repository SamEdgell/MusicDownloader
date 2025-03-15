import sys

from PySide6 import QtWidgets
from UI import CustomMainWindow


class Downloader(CustomMainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application

if __name__ == "__main__":
    print(f"Starting Application\n")
    application = QtWidgets.QApplication(sys.argv)
    downloader = Downloader(application)
    exit_code = application.exec()
    print("Application Closed")
    sys.exit(exit_code)
