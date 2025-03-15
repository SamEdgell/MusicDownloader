from enum import Enum, unique

from datetime import datetime


white_space = "&nbsp;"
start_style = "<span style='"
start_style_end = "'>"
end_style = "</span>"

@unique
class StyleCode(Enum):
    TIME_STAMP_ODD       = 0
    TIME_STAMP_EVEN      = 1
    INFO                 = 2
    ERROR                = 3
    SPOTIFY_FORMAT       = 5
    YOUTUBE_FORMAT       = 6
    URL_FORMAT           = 7
    SUCCESS              = 8


CSS_STYLE = {
    StyleCode.TIME_STAMP_ODD:           "color: black; background-color: #B5D7F9",     # Black text, Blue background.
    StyleCode.TIME_STAMP_EVEN:          "color: black; background-color: #FFD700",     # Black text, Gold background.
    StyleCode.INFO:                     "color: black; background-color: #2CEB6C",     # Black text, Green background.
    StyleCode.ERROR:                    "color: black; background-color: #FC6666",     # Black text, Red background.
    StyleCode.SPOTIFY_FORMAT:           "color: #08AA00; font-weight:bold",            # Green text.
    StyleCode.YOUTUBE_FORMAT:           "color: #F42121; font-weight:bold",            # Red text.
    StyleCode.URL_FORMAT:               "color: black; background-color: #E7F00E",     # Black text, Yellow background.
    StyleCode.SUCCESS:                  "color: black; background-color: #2CEB6C",     # Black text, Green background.
}

"""
Class for the console log.
"""
class UIConsole:
    def __init__(self):
        print(f"UI Initialised - UIConsole")
        super(UIConsole, self).__init__()
        self.append_QTextEdit("consoleLog")
        self.logConsole("1) Select Spotify or Youtube button.")
        self.logConsole("2) Select location for your downloaded files to be stored in.")
        self.logConsole("3) Paste URL of song (or playlist) to download.\n")


    """
    Logs information to the console log with the timestamp.

    @param msg: message to display.
    @param format: format of message, defaulted to none.
    """
    def logConsoleTimestamp(self, msg, format=None):
        if msg:
            timestamp = self.formatTimestamp()

            if format:
                string = timestamp + white_space + start_style + format + start_style_end + msg + end_style
            else:
                string = timestamp + white_space + msg

            self.consoleLog.append(string)


    """
    Logs information to the console log without the timestamp.

    @param msg: message to display.
    @param format: format of message, defaulted to none.
    """
    def logConsole(self, msg, format=None):
        if msg:
            if format:
                string = start_style + format + start_style_end + msg + end_style
            else:
                string = msg

            self.consoleLog.append(string)


    """
    Gets the current time and formats it.

    @return formatted timestamp.
    """
    def formatTimestamp(self):
        if not hasattr(self, 'even'):
            self.even = False

        if self.even:
            time_stamp_style = f"{CSS_STYLE.get(StyleCode.TIME_STAMP_EVEN)}"
        else:
            time_stamp_style = f"{CSS_STYLE.get(StyleCode.TIME_STAMP_ODD)}"

        self.even = not self.even
        time = f"{start_style}{time_stamp_style}{start_style_end}{datetime.now().strftime('%H:%M:%S')}{end_style}"

        return time