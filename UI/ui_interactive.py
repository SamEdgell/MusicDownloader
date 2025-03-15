from PySide6.QtCore import QTimer, QCoreApplication, QThread #TODO DEBUG
from PySide6.QtWidgets import QFileDialog

from UI.ui_console import CSS_STYLE, StyleCode, start_style, start_style_end, end_style

"""
Class for the buttons and text boxes.
"""
class UIInteractive:
    def __init__(self):
        print(f"UI Initialised - UIInteractive")
        super(UIInteractive, self).__init__()
        self.append_QRadioButton("youtubeButton")
        self.append_QRadioButton("spotifyButton")
        self.append_QTextEdit("downloadPathText")
        self.append_QPushButton("selectFolderButton")
        self.append_QTextEdit("urlText")
        self.append_QPushButton("downloadButton")
        self.append_QProgressBar("progressBar")

        self.setupTextWidgets()
        self.updateProgressBar(0)

        self.selectFolderButton.clicked.connect(self.openFolder)
        self.downloadButton.clicked.connect(self.download)


    """
    Configures text widget so it can handle plain text correctly and not change formatting when text has been pasted inside.
    """
    def setupTextWidgets(self):
        # Set urlText to accept only plain text.
        self.urlText.setAcceptRichText(False)

        def custom_paste():
            cursor = self.urlText.textCursor()
            clipboard = self.urlText.parent().application.clipboard()
            cursor.insertText(clipboard.text())

        self.urlText.paste = custom_paste


    """
    Acts on user selecting folder to download to.
    """
    def openFolder(self):
        if self.progressBar.value() not in [0, 100]:
            self.logConsoleTimestamp("Wait for current download to finish before changing location!", CSS_STYLE.get(StyleCode.ERROR))
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            folder = QFileDialog.getExistingDirectory(None, "Select Folder", "", options=options)
            if folder:
                self.downloadPathText.setText(folder)


    """
    Attempts to download the requested URL.
    """
    def download(self):
        result = False
        url = self.urlText.toPlainText()
        if self.progressBar.value() not in [0, 100]:
            self.logConsoleTimestamp("Wait for current download to finish before downloading a new file!", CSS_STYLE.get(StyleCode.ERROR))
        else:
            if not self.downloadPathText.toPlainText() or self.downloadPathText.toPlainText() == "Select Download Location":
                self.logConsoleTimestamp("Error! Select a download path first!", CSS_STYLE.get(StyleCode.ERROR))
                return
            else:
                if not self.urlText.toPlainText() or self.urlText.toPlainText() == "Paste URL Here":
                    self.logConsoleTimestamp("Error! Provide URL first!", CSS_STYLE.get(StyleCode.ERROR))
                    return
                else:
                    source = "Spotify" if self.spotifyButton.isChecked() else "YouTube"
                    source_format = CSS_STYLE.get(StyleCode.SPOTIFY_FORMAT) if source == "Spotify" else CSS_STYLE.get(StyleCode.YOUTUBE_FORMAT)
                    url_format = CSS_STYLE.get(StyleCode.URL_FORMAT)
                    string = f"Downloading URL: {start_style}{url_format}{start_style_end}{url}{end_style} from {start_style}{source_format}{start_style_end}{source}{end_style}"
                    self.logConsoleTimestamp(string)
                    self.updateProgressBar(0) # Reset progress bar for new download.

                    # TODO DEBUG
                    self.progress_value = 0
                    self.progressTimer = QTimer()
                    self.progressTimer.timeout.connect(self.progessTest)
                    self.progressTimer.start(50)
                    # TODO DEBUG END

                    # TODO Add your download logic here
                    result = False

                    # Wait here until progress has completed
                    while self.progressBar.value() != 100:
                        QCoreApplication.processEvents()  # Allow the event loop to process events
                        QThread.msleep(50)  # Sleep for a short period to avoid high CPU usage

                    file_name = "Sam"
                    if result:
                        self.logConsoleTimestamp(f"Download complete. Filename: {file_name}", CSS_STYLE.get(StyleCode.SUCCESS))
                    else:
                        self.logConsoleTimestamp(f"Error downloading: {url}", CSS_STYLE.get(StyleCode.ERROR))


    """
    Updates the progress bar when downloading.

    @param value: New value to update to.
    """
    def updateProgressBar(self, value):
        self.progressBar.setValue(value)




    # TODO DEBUG
    def progessTest(self):
        self.progress_value += 1
        self.updateProgressBar(self.progress_value)

        if self.progress_value >= 100:
            self.progressTimer.stop()
    # TODO DEBUG END

